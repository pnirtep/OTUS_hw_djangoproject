from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from accounts.forms import StudentProfileForm, SignUpForm, LoginForm


class RegisterUserView(View):
    user_form_class = SignUpForm
    student_form_class = StudentProfileForm
    template_name = 'accounts/register_form.html'

    def get(self, request):
        user_form = self.user_form_class
        student_form = self.student_form_class
        return render(request, self.template_name, {'user_form': user_form, 'student_form': student_form})

    def post(self, request):
        user_form = SignUpForm(request.POST)
        student_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return render(request, 'courses/index.html')

# def register_user(request):
#     if request.method == 'POST':
#         user_form = SignUpForm(request.POST, instance=request.user)
#         student_form = StudentProfileForm(request.POST, instance=request.user)
#         if user_form.is_valid() and student_form.is_valid():
#             user_form.save()
#             student_form.save()
#             return redirect('courses')
#         else:
#             context = {
#                 'user_form': user_form,
#                 'student_form': student_form,
#             }
#     else:
#         context = {
#             'user_form': SignUpForm(),
#             'student_form': StudentProfileForm(),
#         }
    # return render(request, 'accounts/register_form.html', context)

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
