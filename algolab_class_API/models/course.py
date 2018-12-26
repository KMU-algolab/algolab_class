from django.db import models
from django.contrib.auth.models import User

from .language import Language


class Course(models.Model):
    """
    과목
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    manager = models.ForeignKey(
        User,
        verbose_name='교수자',
        db_column='Manager',
        primary_key=False,
        on_delete=models.DO_NOTHING,
    )

    name = models.CharField(
        '과목명',
        db_column='Name',
        max_length=50,
        null=False,
        unique=True,
    )

    start_date = models.DateTimeField(
        '시작일',
        db_column='StartDate',
        null=False,
    )

    end_date = models.DateTimeField(
        '종료일',
        db_column='EndDate',
        null=False,
    )

    def __str__(self):
        return '{}, {}'.format(self.manager.username, self.name)

    class Meta:
        db_table = 'Course'
        ordering = ['id', 'manager__id']
        verbose_name = '과목: 기본 정보'
        verbose_name_plural = '과목: 기본 정보'


class LanguageOfCourse(models.Model):
    """
    사용언어
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    course = models.ForeignKey(
        Course,
        verbose_name='수업',
        db_column='Course',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    language = models.ForeignKey(
        Language,
        verbose_name='언어',
        db_column='Language',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'LanguageOfCourse'
        ordering = ['id', 'course__id']
        verbose_name = '과목: 사용 언어'
        verbose_name_plural = '과목: 사용 언어'


class StudentInCourse(models.Model):
    """
    수강학생
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    course = models.ForeignKey(
        Course,
        verbose_name='수업',
        db_column='Course',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    student = models.ForeignKey(
        User,
        verbose_name='학생',
        db_column='Language',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'StudentInCourse'
        ordering = ['id', 'course__id']
        verbose_name = '과목: 수강 학생'
        verbose_name_plural = '과목: 수강 학생'