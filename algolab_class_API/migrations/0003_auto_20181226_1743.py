# Generated by Django 2.1.4 on 2018-12-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algolab_class_API', '0002_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextTypeOfBoard',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='서로게이트키')),
                ('type', models.CharField(db_column='Type', max_length=10, verbose_name='종류')),
            ],
            options={
                'verbose_name': '게시판: 글 종류',
                'verbose_name_plural': '게시판: 글 종류',
                'db_table': 'ContextTypeOfBoard',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='board',
            name='contextType',
            field=models.ForeignKey(db_column='ContextType', max_length=10, on_delete=django.db.models.deletion.DO_NOTHING, to='algolab_class_API.ContextTypeOfBoard', verbose_name='글 종류'),
        ),
    ]