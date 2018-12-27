from django.db import models
from django.contrib.auth.models import User


CONTEXT_TYPE_CHOICES = (
    ("NOTICE", "공지사항"),
    ("QUESTION", "질문"),
)


class Board(models.Model):
    """
    게시판
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
        on_delete=models.DO_NOTHING,  # 임시
    )

    # problem = models.problem

    context = models.TextField(
        '내용',
        db_column='Context',
        null=False,
    )

    context_type = models.CharField(
        '글 종류',
        db_column='ContextType',
        max_length=10,
        choices=CONTEXT_TYPE_CHOICES,
        default=CONTEXT_TYPE_CHOICES[1][0],
        null=False,
    )

    class Meta:
        db_table = 'Board'
        ordering = ['id']
        verbose_name = '게시판: 기본 정보'
        verbose_name_plural = '게시판: 기본 정보'
