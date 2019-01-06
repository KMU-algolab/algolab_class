from rest_framework import serializers

from .. import models


class BoardQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardQuestion
        fields = ['id', 'title', 'writer', 'problem', 'context', 'context_type', 'write_time']


class BoardReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardReply
        fields = []