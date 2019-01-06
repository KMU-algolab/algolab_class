from django.db import models


class Language(models.Model):
    """
    언어
    """
    id = models.AutoField(
        '서로게이트키',
        db_column='ID',
        primary_key=True,
        null=False,
    )

    language = models.CharField(
        '언어(버전)',
        db_column='Language',
        max_length=50,
        primary_key=False,
        unique=True,
    )

    compile_message = models.CharField(
        '컴파일 메세지',
        db_column='CompileMessage',
        max_length=50,
        null=True,
        blank=True
    )

    run_message = models.CharField(
        '실행 메세지',
        db_column='RunMessage',
        max_length=50,
        null=False,
        blank=False,
    )

    def __str__(self):
        return '{}'.format(self.language)

    class Meta:
        db_table = 'Language'
        ordering = ['id']
        verbose_name = '언어: 프로그래밍 언어'
        verbose_name_plural = '언어: 프로그래밍 언어'

