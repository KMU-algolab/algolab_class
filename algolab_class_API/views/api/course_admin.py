from . import mixins
from . import jwt

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers
from django.contrib.auth.models import User


class CourseAdminViewSet(mixins.VersionedSchemaMixin,
                                viewsets.ModelViewSet):
    # lookup_url_kwarg = 'id'
    serializer_class = serializers.ProblemInCourseSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if user_info['group'] != 'CLASS_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return self.get_response_list_for(models.Course.objects.filter(manager_id=user_info['user_id']),
                                          serializers.CourseSerializer)

    def create(self, request, *args, **kwargs):
        serializer = serializers.CourseSerializer(data=request.data)
        serializer.validated_data(raise_exception=True)
        data = serializer.validated_data
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if user_info['group'] != 'CLASS_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance = models.Course.objects.create(name=data['name'],
                                                start_date=data['start_date'],
                                                end_date=data['end_date'],
                                                languages=data['languages'])

        return self.get_response_list_for(models.Course.objects.filter(manager_id=user_info['user_id']),
                                          serializers.CourseSerializer)

    @action(methods=['get', 'post', 'put', 'delete'], detail=False,
            url_name='problem',
            url_path='problem/(?P<problem_id>[0-9]+)',
            serializer_class=serializers.ProblemInCourseSerializer)
    def problem_admin(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return self.get_response_list_for(models.ProblemInCourse.objects.filter(course_id=kwargs['course_id']))

        if request.method.lower() == 'post':
            serializer = serializers.ProblemInCourseSerializer
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            instance = models.ProblemInCourse.objects.create(course=data['course'],
                                                             problem=data['problem'],
                                                             start_date=data['start_date'],
                                                             end_date=data['end_date'])

            return self.get_response_for(instance, True, serializers.ProblemInCourseSerializer)

        sq = models.ProblemInCourse.objects.get(id=kwargs['problem_id'])

        if request.method.lower() == 'put':
            serializer = serializers.ProblemInCourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

            if user_info['group'] != 'CLASS_MANAGER':
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if sq:
                sq.course = data['course']
                sq.problem = data['problem']
                sq.start_date = data['start_date']
                sq.end_date = data['end_date']
                sq.save()

                return self.get_response_for(sq, False, serializers.ProblemInCourseSerializer)

        if request.method.lower() == 'delete':
            sq.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.get_response_for(sq, False, serializers.ProblemInCourseSerializer)

    @action(methods=['get', 'post', 'put', 'delete'], detail=False,
            url_name='user',
            url_path='user/(?P<user_id>[0-9]+)',
            serializer_class=serializers.StudentInCourseSerializer)
    def user_admin(self, request, *args, **kwargs):
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])
        if user_info['group'] != 'CLASS_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.method.lower() == 'get':
            return self.get_response_list_for(models.StudentInCourse.objects.filter(course_id=kwargs['course_id']),
                                              serializers.StudentInCourseSerializer)

        if request.method.lower() == 'post':
            serializer = serializers.StudentInCourseSerializer
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            instance = models.ProblemInCourse.objects.create(course=data['course'],
                                                             student=data['student'])

            return self.get_response_for(instance, True, serializers.StudentInCourseSerializer)

        sq = User.objects.get(id=kwargs['user_id'])

        if request.method.lower() == 'put':
            serializer = serializers.UserSerializer
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            if sq:
                sq.course = data['course']
                sq.student = data['student']
                sq.save()

                return self.get_response_for(sq, False, serializers.StudentInCourseSerializer)

        if request.method.lower() == 'delete':
            sq.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.get_response_list_for(models.StudentInCourse.objects.filter(course_id=kwargs['course_id']),
                                          serializers.StudentInCourseSerializer)


