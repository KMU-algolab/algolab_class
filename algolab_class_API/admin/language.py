from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    """
    프로그래밍 언어 관리
    """
    list_display = ['id', 'language', 'compile_message', 'run_message']
    form = forms.LanguageForm

    class Meta:
        model = models.Language
