# Generated by Django 3.0.2 on 2020-02-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20200210_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='Длительность, мин'),
        ),
    ]
