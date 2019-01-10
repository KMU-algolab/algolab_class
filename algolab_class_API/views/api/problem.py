from . import mixins

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers


class ProblemViewSet(mixins.VersionedSchemaMixin,
                     viewsets.ModelViewSet):
    """

    """
    lookup_url_kwarg = 'id'
    # serializer_class = serializers.
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        user_info = models.UserInfo.objects.get(user=self.request.user)
        course_info = models.UserInfo.objects.get(student=self.request.user) # 여러 과목을 수강한다면?
        if user_info.authority == 'SERVER_MANAGER':
            return self.get_response_list_for(models.Problem.objects.all(), serializers.ProblemListSerializer)
        else:
            return self.get_response_list_for(models.Problem.objects.filter(course=course_info),
                                              serializers.ProblemInCourseListSerializer)

    def create(self, request, *args, **kwargs):
        serializer = serializers.ProblemSerializer
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = models.UserInfo.objects.get(user=self.request.user)

        if user_info != 'SERVER_MANAGER':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance = models.Problem.objects.create(name=data['name'],
                                                 limit_time=data['limit_time'],
                                                 limit_memory=data['limit_memory'],
                                                 judge_type=data['judge_type'],
                                                 judge_code=data['judge_code'])

        return self.get_response_list_for(models.Problem.objects.all(), serializers.ProblemListSerializer)

