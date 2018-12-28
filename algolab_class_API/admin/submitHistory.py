from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.submitHistory)
class SubmitHistoryAdmin(admin.ModelAdmin):
    """
    제출 기록 관리
    """
    list_display = ['id', 'user', 'problem', 'language', 'status', 'code', 'submit_time']
    form = forms.SubmitHistoryForm

    class Meta:
        model = models.SubmitHistory
