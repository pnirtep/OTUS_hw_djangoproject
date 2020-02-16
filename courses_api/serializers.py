from rest_framework import serializers

from courses.models import Course, Teacher


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