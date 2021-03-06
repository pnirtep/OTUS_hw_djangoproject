# Generated by Django 3.0.2 on 2020-02-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_student_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id'], 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='student',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
