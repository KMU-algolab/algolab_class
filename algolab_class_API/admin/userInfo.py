from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """
    유저 정보 관리
    """
    list_display = ['user', 'authority']
    form = forms.UserInfoForm

    class Meta:
        model = models.UserInfo

