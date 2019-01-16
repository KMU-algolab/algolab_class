from . import mixins

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
        user_info = models.UserInfo.objects.get(user=self.request.user)

        if sq and user_info.authority != models.AuthorityType.SERVER_MANAGER:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = models.UserInfo.objects.get(user=self.request.user)

        instance = models.Problem.objects.get(id=kwargs['id'])
        if instance and user_info != models.AuthorityType.SERVER_MANAGER:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if instance:
            instance.name = data['name']
            instance.problem_file = data['problem_file']
            instance.limit_time = data['limit_time']
            instance.limit_memory = data['limit_memory']
            instance.judge_code = data['judge_code']
            instance.judge_type = data['judge_type']
            instance.save()

        return self.get_response_for(instance, False, serializers.ProblemSerializer)


class ServerAdminUserViewSet(mixins.VersionedSchemaMixin,
                             viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    # serializer_class = serializers.
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return

