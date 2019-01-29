from . import mixins
from . import jwt

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from algolab_class_API import models, serializers


class ProblemViewSet(mixins.VersionedSchemaMixin,
                     viewsets.ModelViewSet):
    """

    """
    lookup_url_kwarg = 'id'
    serializer_class = serializers.ProblemSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.ProblemInCourse.objects.filter(course_id=kwargs['id']),
                                          serializers.ProblemInCourseSerializer)



