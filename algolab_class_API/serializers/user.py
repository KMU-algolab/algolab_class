from rest_framework import serializers

from .. import models
from .language import LanguageSerializer

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']