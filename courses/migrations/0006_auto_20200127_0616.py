# Generated by Django 3.0.2 on 2020-01-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200127_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='length',
            field=models.IntegerField(default=0, verbose_name='Длительность, мес'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0, verbose_name='Стоимость курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата старта'),
        ),
    ]
