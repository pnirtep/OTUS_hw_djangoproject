from django.db import models

class Course(models.Model):
    title = models.CharField('Название курса', max_length=200)
    description = models.TextField('Описание курса', blank=True)
    length = models.IntegerField('Длительность, мес', default=0)
    lesson_quantity = models.IntegerField('Количество уроков', default='0')
    course_program = models.TextField(default='Программа курса')
    start_date = models.DateTimeField('Дата старта', null=True, blank=True)
    price = models.FloatField('Стоимость курса', default=0)
    course_teacher = models.ManyToManyField('Teacher')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['title', 'price', 'start_date']

class Lesson(models.Model):
    title = models.CharField('Название урока', max_length=200)
    description = models.TextField('Описание урока', blank=True)
    start_date = models.DateTimeField('Дата проведения')
    durance = models.IntegerField('Длительность, мин', default='0')
    homework = models.TextField ('Домашнее задание к уроку', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_teacher = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ['title', 'start_date', 'course']


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    accessed_courses = models.ManyToManyField(Course)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['last_name']



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
