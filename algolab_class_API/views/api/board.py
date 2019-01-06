from . import mixins

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action

from ... import models, serializers

class BoardViewSet(mixins.VersionedSchemaMixin,
                   viewsets.ModelViewSet):
    """
    create:
    """
    lookup_url_kwarg = 'id'
    serializer_class = serializers.BoardQuestionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return self.get_response_for(models.BoardQuestion.objects.filter(manager=self.request.user),
                                     serializers.BoardQuestionSerializer)