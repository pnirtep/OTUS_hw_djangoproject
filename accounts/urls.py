from django.urls import path

from accounts.views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    # path('register/', register_user, name='register'),
]
