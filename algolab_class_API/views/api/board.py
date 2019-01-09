import datetime

from . import mixins

from rest_framework import viewsets, status, mixins as mx
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

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
    lookup_url_kwarg = 'id'
    serializer_class = serializers.BoardQuestionListSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    pagination_class = BoardListResultsSetPagination

    def list(self, request, *args, **kwargs):
        return self.get_response_list_for(models.BoardQuestion.objects.all(),
                                          serializers.BoardQuestionListSerializer)

    def create(self, request, *args, **kwargs):
        serializer = serializers.BoardQuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        sq = models.BoardQuestion.objects.create(title=data['title'],
                                                 writer=self.request.user,
                                                 problem=data['problem'],
                                                 contents=data['contents'],
                                                 contents_type=data['contents_type'],
                                                 write_time=datetime.datetime.now())

        return self.get_response_list_for(models.BoardQuestion.objects.all(),
                                          serializers.BoardQuestionListSerializer)

    def retrieve(self, request, *arg, **kwargs):
        return self.get_response_for(models.BoardQuestion.objects.get(id=kwargs['id']), False,
                                     serializers.BoardContentsSerializer)

    def destroy(self, request, *args, **kwargs):
        sq = models.BoardQuestion.objects.get(id=kwargs['id'])
        user_info = models.UserInfo.objects.get(user=self.request.user)

        if sq and user_info.authority != 'SERVER_MANAGER' and user_info.authority != 'CLASS_MANAGER' and sq.writer != self.request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_info = models.UserInfo.objects.get(user=self.request.user)

        sq = models.BoardQuestion.objects.get(id=kwargs['id'])
        if sq and user_info.authority != 'SERVER_MANAGER' and user_info.authority != 'CLASS_MANAGER' and sq.writer != self.request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if sq:
            sq.title = data['title']
            sq.writer = data['writer']
            sq.problem = data['problem']
            sq.write_time = datetime.datetime.now()
            sq.save()

        return self.get_response_for(sq, False, serializers.BoardContentsSerializer)

    @action(detail=False, methods=['post', 'put', 'delete'],
            url_name='reply',
            url_path='reply/(?P<id>[0-9]+)',
            serializer_class=serializers.BoardReplySerializer)
    def board_reply(self, request, *args, **kwargs):
        if request.method.lower() == 'post':  # create
            serializer = serializers.BoardReplySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            instance = models.BoardReply.object.create(writer=self.request.user,
                                                       contents=data['contents'],
                                                       question=data['question'],
                                                       write_time=datetime.datetime.now())

            return self.get_response_for(instance, True, serializers.BoardReplySerializer)

        sq = models.BoardReply.objects.get(id=kwargs['id'])

        if request.method.lower() == 'put':  # update
            serializer = serializers.BoardReplySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            user_info = models.UserInfo.objects.get(user=self.request.user)

            if sq and user_info.authority != 'SERVER_MANAGER' and user_info.authority != 'CLASS_MANAGER' and sq.writer != self.request.user:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if sq:
                sq.writer = data['writer']
                sq.contents = data['contents']
                sq.question = data['question']
                sq.write_time = datetime.datetime.now()
                sq.save()

                return self.get_response_for(sq, False, serializers.BoardReplySerializer)

        if request.method.lower() == 'delete':  # delete
            sq.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.get_response_for(sq, False, serializers.BoardReplySerializer)

