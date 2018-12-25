from rest_framework import serializers

from .. import models
from .language import LanguageSerializer
from .user import UserSerializer


class CourseMiniSerializer(serializers.ModelSerializer):
    languages = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'start_date', 'end_date', 'languages']


class LanguageOfCourseSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='language.language')

    class Meta:
        model = models.LanguageOfCourse
        fields = ['id', 'course', 'language', 'language_name']


class StudentInCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LanguageOfCourse
        fields = ['id', 'course', 'student']


class CourseSerializer(serializers.ModelSerializer):
    languages = LanguageOfCourseSerializer(source='languageofcourse_set', many=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'start_date', 'end_date', 'languages']
