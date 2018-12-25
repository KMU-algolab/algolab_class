from django.contrib import admin

from .. import models
from .. import forms


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    """
    과목 관리
    """
    list_display = ['id', 'manager', 'name', 'start_date', 'end_date']
    form = forms.CourseForm

    class Meta:
        model = models.Course


@admin.register(models.LanguageOfCourse)
class LanguageOfCourseAdmin(admin.ModelAdmin):
    """
    과목별 사용 언어 관리
    """
    list_display = ['id', 'course', 'language']
    form = forms.LanguageOfCourse

    class Meta:
        model = models.LanguageOfCourse


@admin.register(models.StudentInCourse)
class StudentInCourse(admin.ModelAdmin):
    """
    수강 학생 관리
    """
    list_display = ['id', 'course', 'student']
    form = forms.StudentInCourse

    class Meta:
        model = models.StudentInCourse
