# Generated by Django 3.2.3 on 2023-10-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20231012_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/user/', verbose_name='Изоброжение'),
        ),
    ]