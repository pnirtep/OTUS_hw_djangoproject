from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from accounts.forms import LoginForm, SignUpForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('courses')
    def get_success_url(self):
        return self.success_url


def logout_view(request):
    logout(request)
    return redirect('courses')


def register_user(request):
    form = SignUpForm
    if request.method == 'POST':
        username = request.POST.get('username')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        password = request.POST.get('password')
        location = request.POST.get('location')
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        user.student.bio = bio
        user.student.location = location
        user.save()
        login(request, user)
        return redirect('courses')

    return render(request, 'accounts/register_form.html', {'form': form})
