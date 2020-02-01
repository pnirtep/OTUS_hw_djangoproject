from django.contrib import admin

from .models import Course, Lesson, Student, Teacher

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'lesson_quantity', 'start_date')
    list_display_links = ('title',)
    search_fields = ('title', 'description')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Teacher)
