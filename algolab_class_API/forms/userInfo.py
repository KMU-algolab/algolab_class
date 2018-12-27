from django import forms

from .. import models


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'user': '유저를 선택하세요',
            'authority': '권한을 선택하세요',
        }