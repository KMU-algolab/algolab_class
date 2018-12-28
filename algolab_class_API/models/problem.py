from django.db import models

from .course import Course

JUDGE_TYPE_CHOICES = (
    ("SOLUTION", "Solution"),
    ("CHECKER", "Checker"),
)


class Problem(models.Model):
    """
    문제
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    name = models.CharField(
        '문제 이름',
        db_column='Name',
        max_length=30,
        null=False,
        unique=True,
    )

    limit_time = models.IntegerField(
        '제한시간',
        db_column='LimitTime',
        null=False,
    )

    limit_memory = models.IntegerField(
        '제한메모리',
        db_column='LimitMemory',
        null=False,
    )

    judge_type = models.CharField(
        '채점타입',
        db_column='JudgeType',
        null=False,
        choices=JUDGE_TYPE_CHOICES,
        default=JUDGE_TYPE_CHOICES[0][0],
        max_length=10,
    )

    judge_code = models.TextField(
        '채점코드',
        db_column='JudgeCode',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'Problem'
        ordering = ['name']
        verbose_name = '문제: 기본 정보'
        verbose_name_plural = '문제: 기본 정보'


class ProblemTestCase(models.Model):
    """
    테스트 케이스
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name='문제',
        db_column='Problem',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    test_case = models.TextField(
        '테스트 케이스',
        db_column='TestCase',
        null=False,
        blank=False,
    )

    def __str__(self):
        return '{}'.format(self.problem.name)

    class Meta:
        db_table = 'ProblemTestCase'
        ordering = ['problem__name']
        verbose_name = '문제: 테스트케이스'
        verbose_name_plural = '문제: 테스트케이스'


class ProblemInCourse(models.Model):
    """
    수업 내 문제
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

    problem = models.ForeignKey(
        Problem,
        verbose_name='문제',
        db_column='Problem',
        primary_key=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
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

    class Meta:
        db_table = 'ProblemInCourse'
        ordering = ['course__id', 'id']
        verbose_name = '문제: 수업 내 문제'
        verbose_name_plural = '문제: 수업 내 문제'

