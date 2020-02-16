from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CoursesApiListView, TeacherApiListView

router = DefaultRouter()
router.register('courses', CoursesApiListView)
router.register('teacher', TeacherApiListView)

urlpatterns = [
    path('', include(router.urls))

]