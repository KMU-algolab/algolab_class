from django import forms

from .. import models


class ProblemForm(forms.ModelForm):
    class Meta:
        model = models.Problem
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'name': '문제 이름을 입력하세요.',
            'limit_time': '제한 시간을 입력하세요.',
            'limit_memory': '제한 메모리를 입력하세요.',
            'judge_type': '채점 타입을 선택하세요.',
            'judge_code': '채점 코드를 입력하세요.',
        }


class ProblemTestCaseForm(forms.ModelForm):
    class Meta:
        model = models.ProblemTestCase
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'problem': '문제를 선택하세요.',
            'test_case': '테스트 케이스를 입력하세요.',
        }


class ProblemInCourseForm(forms.ModelForm):
    class Meta:
        model = models.ProblemInCourse
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'course': '과목을 선택하세요.',
            'problem': '문제를 선택하세요.',
            'start_date': '시작일을 입력하세요.',
            'end_date': '종료일을 입력하세요.',
        }