from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import CoursesApiListView, TeacherApiListView, LessonApiListView, StudentApiListView, UserApiListView

router = DefaultRouter()
router.register('courses', CoursesApiListView)
router.register('teacher', TeacherApiListView)
router.register('lessons', LessonApiListView)
router.register('users', UserApiListView)
router.register('students', StudentApiListView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', views.obtain_auth_token, name = 'auth-token'),

]