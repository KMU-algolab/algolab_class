from django.db import models
from django.contrib.auth.models import User

from .language import Language
from .problem import ProblemInCourse

STATUS_TYPE_CHOICES = (
    ("SOLVED", "Solved"),
    ("COMPILE_ERROR", "CompileError"),
    ("TIME_OVER", "TimeOver"),
    ("RUNTIME_ERROR", "RuntimeError"),
)


class SubmitHistory(models.Model):
    """
    제출 기록
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    user = models.ForeignKey(
        User,
        verbose_name='제출자',
        db_column='User',
        primary_key=False,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )

    problem = models.ForeignKey(
        ProblemInCourse,
        verbose_name='문제',
        db_column='Problem',
        primary_key=False,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )

    language = models.ForeignKey(
        Language,
        verbose_name='언어',
        db_column='Language',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    status = models.CharField(
        '제출 결과',
        db_column='Status',
        null=False,
        choices=STATUS_TYPE_CHOICES,
        max_length=10,
    )

    code = models.TextField(
        '제출 코드',
        db_column='Code',
        null=False,
        blank=False,
    )

    submit_time = models.DateTimeField(
        '제출 시간',
        db_column='SubmitTime',
        auto_now_add=True,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'SubmitHistory'
        ordering = ['id']
        verbose_name = '제출 기록'
        verbose_name_plural = '제출 기록'

