from . import mixins
from . import jwt

from django.contrib.auth.models import User

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers


class ServerAdminProblemViewSet(mixins.VersionedSchemaMixin,
                                viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    serializer_class = serializers.ProblemSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.Problem.objects.all(),
                                          serializers.ProblemSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        sq = models.Problem.objects.create(name=data['name'],
                                           problem_file=data['problem_file'],
                                           limit_time=data['limit_time'],
                                           limit_memory=data['limit_memory'],
                                           judge_type=data['judge_type'],
                                           judge_code=data['judge_code'])

        return self.get_response_list_for(models.Problem.objects.all(),
                                          serializers.ProblemSerializer)

    def retrieve(self, request, *args, **kwargs):
        return self.get_response_for(models.Problem.objects.get(id=kwargs['id']), False,
                                     serializers.ProblemSerializer)

    def destroy(self, request, *args, **kwargs):
        sq = models.Problem.objects.get(id=kwargs['id'])
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if not sq and user_info['group'] != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        sq = models.Problem.objects.get(id=kwargs['id'])
        if not sq and user_info['group'] != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if sq:
            sq.name = data['name']
            sq.problem_file = data['problem_file']
            sq.limit_time = data['limit_time']
            sq.limit_memory = data['limit_memory']
            sq.judge_code = data['judge_code']
            sq.judge_type = data['judge_type']
            sq.save()

        return self.get_response_for(sq, False, serializers.ProblemSerializer)


class ServerAdminUserViewSet(mixins.VersionedSchemaMixin,
                             viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    serializer_class = serializers.UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if user_info['group'] != 'SERVER_MANAGER':
            print(user_info['group'])
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return self.get_response_list_for(User.objects.all(), serializers.UserSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if user_info['group'] != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance = User.objects.create_user(username=data['username'],
                                            password=data['password'],
                                            groups=data['group'])

        return self.get_response_for(instance, True, serializers.UserSerializer)

    def retrieve(self, request, *args, **kwargs):
        return self.get_response_for(User.objects.filter(id=kwargs['id']), False, serializers.UserSerializer)

    def destroy(self, request, *args, **kwargs):
        sq = User.objects.get(id=kwargs['id'])
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if not sq and user_info['group'] != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        sq = User.objects.get(id=kwargs['id'])
        if not sq and user_info != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if sq:
            sq.username = data['username']
            sq.password = data['password']
            sq.groups = data['password']

        return self.get_response_for(sq, False, serializers.ProblemSerializer)
