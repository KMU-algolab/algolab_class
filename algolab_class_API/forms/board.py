from django import forms

from .. import models


class BoardForm(forms.ModelForm):
    class Meta:
        model = models.Board
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'writer': '작성자를 선택하세요',
            'context': '내용을 입력하세요.',
            'contextType': '글 종류를 선택하세요.',
        }

