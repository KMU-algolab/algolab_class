from . import mixins

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers


class CourseAdminProblemViewSet(mixins.VersionedSchemaMixin,
                         viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    serializer_class = serializers.ProblemSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.Course.objects.filter(manager=self.request.user),
                                          serializers.ProblemSerializer)

    @action(methods= ['get', 'post', 'put', 'delete'],detail=False,
            url_name='problem',
            url_path='problem/(?P<id>[0-9]+)',
            serializer_class=serializers.ProblemInCourseSerializer)
    def problem(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return self.get_response_list_for(models.BoardQuestion.objects.filter(id=kwargs['id']),
                                              serializers.BoardQuestionListSerializer)

        if request.method.lower() == 'post':
            serializer = serializers.ProblemInCourseSerializer
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            instance = models.ProblemInCourse.objects.create(course=data['course'],
                                                             problem=data['problem'],
                                                             start_date=data['start_date'],
                                                             end_date=data['end_date']
                                                             )

            return self.get_response_for(instance, True, serializers.ProblemInCourseSerializer)

        sq = models.ProblemInCourse.objects.get(id=kwargs['id'])

        if request.method.lower() == 'put':
            serializer = serializers.ProblemInCourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            user_info = models.UserInfo.objects.get(user=self.request.user)

            if sq and user_info.authority < models.AuthorityType.CLASS_MANAGER:
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

