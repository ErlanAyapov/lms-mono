# Generated by Django 3.2.3 on 2023-10-12 08:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_auto_20220502_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Дополнительный информация', 'verbose_name_plural': 'Дополнительные информаций'},
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='customer',
            name='biography',
            field=models.TextField(null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/user/', verbose_name='Изоброжение'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth_day',
            field=models.IntegerField(verbose_name='День рождение'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth_mounth',
            field=models.CharField(max_length=10, verbose_name='Месяц рождение'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth_year',
            field=models.IntegerField(verbose_name='Год рождение'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teacher_students', to=settings.AUTH_USER_MODEL, verbose_name='Ученики'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_class',
            field=models.CharField(choices=[('Ученик', 'Ученик'), ('Учитель', 'Учитель')], default='Ученик', max_length=100, verbose_name='Статус пользователья'),
        ),
    ]
