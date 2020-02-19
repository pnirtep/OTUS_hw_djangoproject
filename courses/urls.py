from django.urls import path
from . import views



urlpatterns = [path('', views.courses_page, name='courses'),
               path('<int:pk>/', views.course_detail, name='course_detail'),
               path('new/', views.course_new, name='course_new'),
               path('<int:pk>/edit/', views.course_edit, name='course_edit'),
               path('<int:pk>/del/', views.course_delete, name='course_delete'),
               path('<int:pk>/register/', views.course_register, name='course_register'),
               ]
