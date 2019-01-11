from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.Problem)
class ProblemAdmin(admin.ModelAdmin):
    """
    문제 관리
    """
    list_display = ['id', 'name', 'problem_file', 'limit_time', 'limit_memory', 'judge_type', 'judge_code']
    form = forms.ProblemForm

    class Meta:
        model = models.Problem


@admin.register(models.ProblemTestCase)
class ProblemTestCaseAdmin(admin.ModelAdmin):
    """
    문제 테스트케이스 관리
    """
    list_display = ['id', 'problem', 'test_case']
    form = forms.ProblemTestCaseForm

    class Meta:
        model = models.ProblemTestCase


@admin.register(models.ProblemInCourse)
class ProblemInCourseAdmin(admin.ModelAdmin):
    """
    과목 내 문제 관리
    """
    list_display = ['id', 'course', 'problem', 'start_date', 'end_date']
    form = forms.ProblemInCourseForm

    class Meta:
        model = models.ProblemInCourse
