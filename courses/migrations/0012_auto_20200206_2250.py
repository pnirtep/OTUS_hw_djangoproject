# Generated by Django 3.0.2 on 2020-02-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20200206_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='start_date',
            field=models.DateTimeField(verbose_name='Дата проведения'),
        ),
    ]