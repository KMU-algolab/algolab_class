from rest_framework import serializers

from .. import models
from .language import LanguageSerializer
from .user import UserSerializer


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = ['id', 'name', 'limit_time', 'limit_memory', 'problem_file', 'judge_type', 'judge_code']


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = ['id', 'name']


class ProblemInCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProblemInCourse
        fields = ['id', 'course', 'problem', 'start_date', 'end_date']

