from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignUpForm


def login_view(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'accounts/login.html', {'form': form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses')
        else:
            form = LoginForm
            error = 'Неверные данные пользователя'
            context = {
                'error': error,
                'form': form,
            }
            return render(request, 'accounts/login.html', context=context)


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

    return render(request, 'accounts/register_form.html', {'form':form})
