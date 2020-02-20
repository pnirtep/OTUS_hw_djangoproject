from django.urls import path

from accounts.views import register_user, UserLoginView, logout_view

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
