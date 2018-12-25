from django import forms

from .. import models


class LanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'language': '프로그래밍 언어(버전)을 입력하세요.',
            'compile_message': '컴파일 메세지를 입력하세요.',
            'run_message': '실행 메세지를 입력하세요.',
        }
