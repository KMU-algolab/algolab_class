from django_filters import rest_framework as filterset, rest_framework

from ..models import *


class CourseFilter(rest_framework.FilterSet):
    manager = filterset.NumberFilter(name='manager__id', label='관리자', help_text='관리자')
    name = filterset.CharFilter(name='name', label='과목명', help_text='과목명', lookup_expr='contains')

    order = filterset.OrderingFilter(
        help_text='정렬순서, 관리자(manager), 과목명(course name)',
        fields=[
            ('manager', 'manager__name'),
            ('course', 'name')
        ],
        field_labels={
            'manager': '과목 관리자',
            'course': '과목명',
        }
    )

    class Meta:
        model = Course
        fields = ['manager', 'name']


class LanguageOfCourseFilter(rest_framework.FilterSet):
    course = filterset.NumberFilter(name='course__id', label='과목명', help_text='과목명')

    order = filterset.OrderingFilter(
        help_text='정렬순서, 과목(course)',
        fields=[
            ('course', 'course__name'),
        ],
        field_labels={
            'course': '과목명',
        }
    )

    class Meta:
        model = Course
        fields = ['course']


class StudentInCourseFilter(rest_framework.FilterSet):
    course = filterset.NumberFilter(name='course__id', label='과목', help_text='과목')
    student = filterset.NumberFilter(name='student__id', label='학생', help_text='학생')

    order = filterset.OrderingFilter(
        help_text='정렬순서, 과목(course), 학생(student)',
        fields=[
            ('course', 'course__name'),
            ('student', 'student__name'),
        ],
        field_labels={
            'course': '과목명',
        }
    )

    class Meta:
        model = Course
        fields = ['course']
