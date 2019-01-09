from rest_framework import serializers

from .. import models


class BoardQuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardQuestion
        fields = ['id', 'title', 'writer', 'problem', 'contents_type', 'write_time']


class BoardReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardReply
        fields = ['id', 'writer', 'contents', 'question', 'write_time']


class BoardContentsSerializer(serializers.ModelSerializer):
    replies = BoardReplySerializer(source='boardreply_set', many=True)

    class Meta:
        model = models.BoardQuestion
        fields = ['id', 'title', 'writer', 'problem', 'contents', 'contents_type', 'write_time', 'replies']


class BoardQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardQuestion
        fields = ['id', 'title', 'writer', 'problem', 'contents', 'contents_type', 'write_time']


