import datetime

from . import mixins
from . import jwt

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

from ... import models, serializers


class BoardListResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BoardViewSet(mixins.VersionedSchemaMixin,
                   viewsets.ModelViewSet):
    """
    create:
    """
    # lookup_url_kwarg = 'id'
    serializer_class = serializers.BoardContentsSerializer
    http_method_names = ['get', 'post']
    pagination_class = BoardListResultsSetPagination

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.BoardQuestion.objects.filter(problem_id=kwargs['id']),
                                          serializers.BoardQuestionListSerializer)

    def create(self, request, *args, **kwargs):
        serializer = serializers.BoardQuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        instance = models.BoardQuestion.objects.create(title=data['title'],
                                                       writer=User.objects.get(id=user_info['user_id']),
                                                       problem=data['problem'],
                                                       contents=data['contents'],
                                                       contents_type=data['contents_type'],
                                                       write_time=datetime.datetime.now())

        return self.get_response_for(instance, True, serializers.BoardQuestionCreateSerializer)

    def retrieve(self, request, *args, **kwargs):
        return self.get_response_for(models.BoardQuestion.objects.get(id=kwargs['id']), False,
                                     serializers.BoardQuestionListSerializer)

    @action(detail=False, methods=['get', 'put', 'delete'],
            url_name='question',
            url_path='question/(?P<q_id>[0-9]+)',
            serializer_class=serializers.BoardContentsSerializer)
    def board_question(self, request, *args, **kwargs):
        user_info = jwt.decode_jwt(request.META['HTTP_JMT'])

        if request.method.lower() == 'get':
            return self.get_response_for(models.BoardQuestion.objects.get(id=kwargs['q_id']), False,
                                         serializers.BoardContentsSerializer)

        if request.method.lower() == 'delete':
            sq = models.BoardQuestion.objects.get(id=kwargs['q_id'])
            if not sq and user_info['group'] != 'SERVER_MANAGER' and user_info['group'] != 'CLASS_MANAGER' \
                    and sq.writer_id != user_info['user_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            sq.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        if request.method.lower() == 'put':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            sq = models.BoardQuestion.objects.get(id=kwargs['q_id'])
            if not sq and user_info['group'] != 'SERVER_MANAGER' and user_info['group'] != 'CLASS_MANAGER' \
                    and sq.writer_id != user_info['user_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if sq:
                sq.title = data['title']
                sq.writer = data['writer']
                sq.problem = data['problem']
                sq.contents = data['contents']
                sq.contents_type = data['contents_type']
                sq.replies = data['replies']
                sq.write_time = datetime.datetime.now()
                sq.save()

            return self.get_response_for(sq, False, serializers.BoardContentsSerializer)

