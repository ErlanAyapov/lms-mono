# Generated by Django 3.2.3 on 2023-08-15 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_course_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskisfill',
            options={'verbose_name': 'Тапсырма ', 'verbose_name_plural': 'Тапсырмалар бос орынды толтыр'},
        ),
        migrations.RemoveField(
            model_name='taskisfill',
            name='t_type',
        ),
    ]
