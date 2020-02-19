from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import CoursesApiListView, TeacherApiListView

router = DefaultRouter()
router.register('courses', CoursesApiListView)
router.register('teacher', TeacherApiListView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', views.obtain_auth_token, name = 'auth-token'),

]