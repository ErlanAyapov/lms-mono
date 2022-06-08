# Generated by Django 3.2.8 on 2022-06-08 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0012_userresult_user_false_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сабаты қосты'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_1',
            field=models.CharField(max_length=200, verbose_name='Нұсқа (1)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_2',
            field=models.CharField(max_length=200, verbose_name='Нұсқа (2)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_3',
            field=models.CharField(max_length=200, verbose_name='Нұсқа (3)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_4',
            field=models.CharField(default='Нұсқа (4)', max_length=200, verbose_name='Нұсқа (4)'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='answer_true',
            field=models.CharField(max_length=200, verbose_name='Тапсырма жауабы'),
        ),
        migrations.AlterField(
            model_name='taskistest',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Тапсырма тақырыбы'),
        ),
    ]