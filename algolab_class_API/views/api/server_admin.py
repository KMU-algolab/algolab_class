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
                                           problem_file=['problem_file'],
                                           limit_time=['limit_time'],
                                           limit_memory=['limit_memory'],
                                           judge_type=['judge_type'],
                                           judge_code=['judge_code'])

        return self.get_response_list_for(models.Problem.objects.all(),
                                          serializers.ProblemSerializer)

