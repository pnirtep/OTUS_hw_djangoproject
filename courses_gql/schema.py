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


class CourseMutation(graphene.Mutation):
    class Arguments:
        course_id = graphene.Int(required=True)
        new_title = graphene.String(required=True)
        new_description = graphene.String(required=True)
        new_price = graphene.Int(required=False)
    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_id, new_title, new_description, new_price):
        course = Course.objects.get(pk=course_id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()
        return {
            'result': True,
            'course': Course.objects.get(pk=course_id)
        }

class CreateCourseMutation(graphene.Mutation):
    class Arguments:
        new_title = graphene.String(required=True)
        new_description = graphene.String(required=True)
        new_price = graphene.Int(required=False)
    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, new_title, new_description, new_price):
        course = Course(title=new_title, description=new_description, price=new_price)
        course.save()
        return {
            'result': True,
            'course': Course.objects.get(title=new_title)
        }

class Mutation:
    change_course = CourseMutation.Field()
    new_course = CreateCourseMutation.Field()

class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)
    all_lessons = graphene.List(LessonType)
    all_users = graphene.List(UserType)
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)

    course = graphene.Field(CourseType,
                            id=graphene.Int(),
                            title=graphene.String())

    user = graphene.Field(UserType,
                          id=graphene.Int(),
                          username=graphene.String(),
                          first_name=graphene.String(),
                          last_name=graphene.String(),
                          student=graphene.String())

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

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        student = kwargs.get('student')

        if id is not None:
            return User.objects.get(pk=id)
        if username is not None:
            return User.objects.get(username=username)
        if first_name is not None:
            return User.objects.get(first_name=first_name)
        if last_name is not None:
            return User.objects.get(last_name=last_name)
        if student is not None:
            return User.objects.get(student=student)
        return None
