from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.BoardQuestion)
class BoardQuestionAdmin(admin.ModelAdmin):
    """
    게시판 질문 관리
    """
    list_display = ['id', 'title', 'writer', 'problem', 'context', 'context_type', 'write_time']
    form = forms.BoardQuestionForm

    class Meta:
        model = models.BoardQuestion


@admin.register(models.BoardReply)
class BoardReplyAdmin(admin.ModelAdmin):
    """
    게시판 질문 관리
    """
    list_display = ['id', 'writer', 'context', 'question', 'write_time']
    form = forms.BoardReplyForm

    class Meta:
        model = models.BoardReply

