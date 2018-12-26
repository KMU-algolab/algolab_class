from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    """
    게시판 관리
    """
    list_display = ['id', 'writer', 'context', 'contextType']
    form = forms.BoardForm

    class Meta:
        model = models.Board

