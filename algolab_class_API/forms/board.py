from django import forms

from .. import models


class BoardQuestionForm(forms.ModelForm):
    class Meta:
        model = models.BoardQuestion
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'title': '글 제목을 입력하세요.',
            'writer': '작성자를 선택하세요.',
            'problem': '문제를 선택하세요.',
            'contents': '내용을 입력하세요.',
            'contentsType': '글 종류를 선택하세요.',
            'write_time': '글 작성 시간을 입력하세요.',
        }


class BoardReplyForm(forms.ModelForm):
    class Meta:
        model = models.BoardReply
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'writer': '작성자를 선택하세요.',
            'contents': '내용을 입력하세요.',
            'question': '질문을 선택하세요.',
            'write_time': '글 작성 시간을 입력하세요.',
        }