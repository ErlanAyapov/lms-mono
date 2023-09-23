# Generated by Django 3.2.8 on 2022-05-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_t_type_course_synup'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskistest',
            name='answer_false_4',
            field=models.CharField(default='Нұсқа (4)', max_length=25, verbose_name='Нұсқа (4)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_false_1',
            field=models.CharField(max_length=25, verbose_name='Нұсқа (1)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_false_2',
            field=models.CharField(max_length=25, verbose_name='Нұсқа (2)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_false_3',
            field=models.CharField(max_length=25, verbose_name='Нұсқа (3)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_true',
            field=models.CharField(max_length=25, verbose_name='Тапсырма жауабы'),
        ),
    ]
