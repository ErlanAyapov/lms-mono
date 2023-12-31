# Generated by Django 3.2.3 on 2023-08-15 09:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20230815_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectLection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='Лекция тақырыбы')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Лекция мәтіні')),
                ('youtube_iframe_tag', models.CharField(max_length=1000, verbose_name='Видео ролик (Iframe)')),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекциялар',
            },
        ),
    ]
