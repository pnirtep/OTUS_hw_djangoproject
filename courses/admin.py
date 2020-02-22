from django.contrib import admin

from .models import Course, Lesson, Student, Teacher


class CourseInline(admin.TabularInline):
    model = Lesson
    fields = ('title', 'description',)
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline,
    ]
    list_display = ('title', 'description', 'price', 'lesson_quantity', 'start_date', 'published')
    list_display_links = ('title',)
    search_fields = ('title', 'description')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','bio', 'location')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','description','course')



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
