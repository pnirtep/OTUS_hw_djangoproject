from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from courses.models import Course, Teacher, Lesson, Student


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    teacher_courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Teacher
        fields = 'url', 'id', 'first_name', 'teacher_courses',


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_teacher = TeacherSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = 'id', 'title', 'price', 'start_date', 'course_teacher'


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = 'id', 'title', 'description', 'course'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    accessed_courses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    class Meta:
        model = Student
        fields = 'user', 'bio', 'location', 'accessed_courses'
