from django.db import models
from django.contrib.auth.models import User


AUTHORITY_TYPE_CHOICES = (
    ("STUDENT", "학생"),
    ("MENTOR", "멘토"),
    ("CLASS_MANAGER", "과목관리자"),
    ("SERVER_MANAGER", "서버관리자"),
)


class UserInfo(models.Model):
    """
    유저 정보
    """
    user = models.OneToOneField(
        User,
        verbose_name='유저',
        primary_key=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    authority = models.CharField(
        '권한',
        db_column='Authority',
        null=False,
        choices=AUTHORITY_TYPE_CHOICES,
        max_length=20,
    )

    class Meta:
        db_table = 'UserInfo'
        ordering = ['user__username']
        verbose_name = '유저: 기본 정보'
        verbose_name_plural = '유저: 기본 정보'
