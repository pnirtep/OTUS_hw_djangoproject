# Generated by Django 3.0.2 on 2020-02-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200206_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='start_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата проведения'),
        ),
    ]