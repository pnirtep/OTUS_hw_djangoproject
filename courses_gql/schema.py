import graphene
from graphene_django.types import DjangoObjectType
from courses.models import Course, Teacher, Lesson, Student
from django.contrib.auth.models import User


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson

class UserType(DjangoObjectType):
    class Meta:
        model = User

class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher

class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(object):
    all_courses = graphene.List(CourseType)
    all_lessons = graphene.List(LessonType)
    all_users = graphene.List(UserType)
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.all()

    def resolve_all_lessons(self, info, **kwargs):
        return Lesson.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.all()
