from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Course(models.Model):
    title = models.CharField('Название курса', max_length=200)
    description = models.TextField('Описание курса')
    length = models.IntegerField('Длительность, мес', default=0)
    lesson_quantity = models.IntegerField('Количество уроков', default=0)
    course_program = models.TextField('Программа курса', blank=True)
    start_date = models.DateField('Дата старта', default=date.today)
    price = models.FloatField('Стоимость курса', default=0)
    course_teacher = models.ManyToManyField('Teacher', blank=True, verbose_name="Преподаватели курса")
    published = models.BooleanField('Опубликован', default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['title', 'price', 'start_date']


class Lesson(models.Model):
    title = models.CharField('Название урока', max_length=200)
    description = models.TextField('Описание урока', blank=True)
    start_date = models.DateTimeField('Дата проведения', auto_now=False, auto_now_add=False)
    duration = models.IntegerField('Длительность, мин', default=0)
    homework = models.TextField('Домашнее задание к уроку', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = 'lessons')
    lesson_teacher = models.ManyToManyField('Teacher', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ['title', 'start_date', 'course']


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    accessed_courses = models.ManyToManyField(Course, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.student.save()


    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'
        ordering = ['id']


class Teacher(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    biography = models.TextField('Биография', blank=True)
    teacher_courses = models.ManyToManyField(Course)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ['last_name']
