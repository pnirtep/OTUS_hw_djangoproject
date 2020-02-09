from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description','price', 'course_teacher', 'lesson_quantity', 'start_date')
