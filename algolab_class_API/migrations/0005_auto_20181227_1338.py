# Generated by Django 2.1.4 on 2018-12-27 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algolab_class_API', '0004_auto_20181226_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='서로게이트키')),
                ('name', models.CharField(db_column='Name', max_length=30, unique=True, verbose_name='문제 이름')),
                ('limit_time', models.IntegerField(db_column='LimitTime', verbose_name='제한시간')),
                ('limit_memory', models.IntegerField(db_column='LimitMemory', verbose_name='제한메모리')),
                ('judge_type', models.CharField(choices=[('SOLUTION', 'Solution'), ('CHECKER', 'Checker')], db_column='JudgeType', default='SOLUTION', max_length=10, verbose_name='채점타입')),
                ('judge_code', models.TextField(blank=True, db_column='JudgeCode', null=True, verbose_name='채점코드')),
            ],
            options={
                'verbose_name': '문제: 기본 정보',
                'verbose_name_plural': '문제: 기본 정보',
                'db_table': 'Problem',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProblemInCourse',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='서로게이트키')),
                ('start_date', models.DateTimeField(db_column='StartDate', verbose_name='시작일')),
                ('end_date', models.DateTimeField(db_column='EndDate', verbose_name='종료일')),
                ('course', models.ForeignKey(db_column='Course', on_delete=django.db.models.deletion.CASCADE, to='algolab_class_API.Course', verbose_name='수업')),
                ('problem', models.ForeignKey(db_column='Problem', on_delete=django.db.models.deletion.CASCADE, to='algolab_class_API.Problem', verbose_name='문제 키')),
            ],
            options={
                'verbose_name': '문제: 수업 내 문제',
                'verbose_name_plural': '문제: 수업 내 문제',
                'db_table': 'ProblemInCourse',
                'ordering': ['course__id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ProblemTestCase',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='서로게이트키')),
                ('test_case', models.TextField(db_column='TestCase', verbose_name='테스트 케이스')),
                ('problem', models.ForeignKey(db_column='Problem', on_delete=django.db.models.deletion.CASCADE, to='algolab_class_API.Problem', verbose_name='문제 키')),
            ],
            options={
                'verbose_name': '문제: 테스트케이스',
                'verbose_name_plural': '문제: 테스트케이스',
                'db_table': 'ProblemTestCase',
                'ordering': ['problem__name'],
            },
        ),
        migrations.RenameField(
            model_name='board',
            old_name='contextType',
            new_name='context_type',
        ),
    ]