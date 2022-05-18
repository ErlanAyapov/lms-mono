# Generated by Django 3.2.8 on 2022-05-16 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0007_auto_20220514_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_task', models.CharField(max_length=3, verbose_name='Жалпы сұрақ')),
                ('true_task', models.CharField(max_length=3, verbose_name='Дұрыс сұрақ')),
                ('false_task', models.CharField(max_length=3, verbose_name='Қате сұрақ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Қолданушы нәтижесін',
                'verbose_name_plural': 'Қолданушы нәтижелері',
            },
        ),
    ]