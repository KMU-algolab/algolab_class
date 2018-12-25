from django import forms

from .. import models


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'manager': '과목 관리자의 선택하세요.',
            'name': '과목명을 입력하세요.',
            'start_date': '과목 시작일을 입력하세요.',
            'end_date': '과목 종료일을 입력하세요.',
        }


class LanguageOfCourse(forms.ModelForm):
    class Meta:
        model = models.LanguageOfCourse
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'course': '과목을 선택하세요.',
            'language': '사용 언어를 선택하세요.',
        }


class StudentInCourse(forms.ModelForm):
    class Meta:
        model = models.StudentInCourse
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea
        }
        help_texts = {
            'course': '과목을 선택하세요.',
            'student': '수강 학생을 선택하세요.',
        }
