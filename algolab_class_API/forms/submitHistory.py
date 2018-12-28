from django import forms

from .. import models


class SubmitHistoryForm(forms.ModelForm):
    class Meta:
        model = models.SubmitHistory
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'user': '제출자를 선택하세요.',
            'problem': '문제를 선택하세요.',
            'language': '언어를 선택하세요.',
            'status': '제출 결과를 선택하세요.',
            'code': '제출 코드를 입력하세요.',
            'submit_time': '제출 시간을 입력하세요.',
        }