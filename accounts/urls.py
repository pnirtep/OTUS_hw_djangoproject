from django.urls import path

from accounts.views import RegisterUserView, login_view, logout_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
