from django.db import models
from django.contrib.auth.models import User

from .problem import Problem

CONTENTS_TYPE_CHOICES = (
    ("NOTICE", "공지사항"),
    ("QUESTION", "질문"),
)


class BoardQuestion(models.Model):
    """
    게시판 질문
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    title = models.CharField(
        '글 제목',
        db_column='Title',
        null=False,
        blank=False,
        max_length=50,
    )

    writer = models.ForeignKey(
        User,
        verbose_name='작성자',
        db_column='Writer',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name='문제',
        db_column='Problem',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    contents = models.TextField(
        '내용',
        db_column='Contents',
        null=False,
    )

    contents_type = models.CharField(
        '글 종류',
        db_column='ContentsType',
        max_length=10,
        choices=CONTENTS_TYPE_CHOICES,
        default=CONTENTS_TYPE_CHOICES[1][0],
        null=False,
    )

    write_time = models.DateTimeField(
        '작성 시간',
        db_column='WriteTime',
        null=False,
        blank=False,
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        db_table = 'BoardQuestion'
        ordering = ['id']
        verbose_name = '게시판: 질문 정보'
        verbose_name_plural = '게시판: 질문 정보'


class BoardReply(models.Model):
    """
    게시판 답변
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    writer = models.ForeignKey(
        User,
        verbose_name='작성자',
        db_column='Writer',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    contents = models.TextField(
        '내용',
        db_column='Contents',
        null=False,
        blank=False,
    )

    question = models.ForeignKey(
        BoardQuestion,
        verbose_name='질문 문제',
        db_column='Question',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    write_time = models.DateTimeField(
        '작성 시간',
        db_column='WriteTime',
        auto_now_add=True,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'BoardReply'
        ordering = ['id']
        verbose_name = '게시판: 답변 정보'
        verbose_name_plural = '게시판: 답변 정보'

