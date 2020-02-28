import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
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


class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)
    all_lessons = graphene.List(LessonType)
    all_users = graphene.List(UserType)
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)

    course = graphene.Field(CourseType,
                              id=graphene.Int(),
                              title=graphene.String())

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

    def resolve_course(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Course.objects.get(pk=id)

        if title is not None:
            return Course.objects.get(title=title)
        return None
