# Generated by Django 2.1.4 on 2019-01-10 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algolab_class_API', '0010_submithistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardquestion',
            name='context',
        ),
        migrations.RemoveField(
            model_name='boardquestion',
            name='context_type',
        ),
        migrations.RemoveField(
            model_name='boardreply',
            name='context',
        ),
        migrations.AddField(
            model_name='boardquestion',
            name='contents',
            field=models.TextField(db_column='Contents', default='내용을 입력하세요.', verbose_name='내용'),
        ),
        migrations.AddField(
            model_name='boardquestion',
            name='contents_type',
            field=models.CharField(choices=[('NOTICE', '공지사항'), ('QUESTION', '질문')], db_column='ContentsType', default='QUESTION', max_length=10, verbose_name='글 종류'),
        ),
        migrations.AddField(
            model_name='boardreply',
            name='contents',
            field=models.TextField(db_column='Contents', default='내용을 입력하세요.', verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='boardquestion',
            name='write_time',
            field=models.DateTimeField(db_column='WriteTime', verbose_name='작성 시간'),
        ),
        migrations.AlterField(
            model_name='course',
            name='manager',
            field=models.ForeignKey(db_column='Manager', on_delete=django.db.models.deletion.DO_NOTHING, related_name='courseManager_set', to=settings.AUTH_USER_MODEL, verbose_name='교수자'),
        ),
        migrations.AlterField(
            model_name='submithistory',
            name='status',
            field=models.CharField(choices=[('NOT_SOLVED', 'NotSolved'), ('SOLVED', 'Solved'), ('COMPILE_ERROR', 'CompileError'), ('TIME_OVER', 'TimeOver'), ('RUNTIME_ERROR', 'RuntimeError'), ('SERVER_ERROR', 'ServerError')], db_column='Status', default='NOT_SOLVED', max_length=10, verbose_name='제출 결과'),
        ),
    ]
