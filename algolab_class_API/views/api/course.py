from . import mixins

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers


class CourseViewSet(mixins.VersionedSchemaMixin,
                    viewsets.ModelViewSet):  # total profile
    """
    create:
    """
    lookup_url_kwarg = 'id'
    serializer_class = serializers.CourseMiniSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.Course.objects.filter(manager=self.request.user),
                                          serializers.CourseSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        sq = models.Course.objects.create(manager=self.request.user,
                                          name=data['name'],
                                          start_date=data['start_date'],
                                          end_date=data['end_date'])

        for id in data['languages']:
            models.LanguageOfCourse.objects.create(course=sq, language_id=id)

        return self.get_response_list_for(models.Course.objects.filter(manager=self.request.user),
                                          serializers.CourseSerializer)

    def retrieve(self, request, *args, **kwargs):
        return self.get_response_for(models.Course.objects.get(id=kwargs['id']), False, serializers.CourseSerializer)

    def destroy(self, request, *args, **kwargs):
        sq = models.Course.objects.get(id=kwargs['id'])

        if sq and sq.manager != self.request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        sq = models.Course.objects.get(id=kwargs['id'])
        if sq and sq.manager != self.request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        models.LanguageOfCourse.objects.filter(course=sq).delete()

        if sq:
            sq.name = data['name']
            sq.start_date = data['start_date']
            sq.end_date = data['end_date']
            sq.save()

            for id in data['languages']:
                models.LanguageOfCourse.objects.create(course=sq, language__id=id)

        return self.get_response_for(sq, False, serializers.CourseSerializer)
