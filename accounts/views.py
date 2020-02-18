from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View

from accounts.forms import StudentProfileForm, SignUpForm
from courses.models import Student


# class RegisterUserView(CreateView):
#     form_class = SignUpForm
#
#     template_name = 'accounts/register_form.html'
#     success_url = reverse_lazy('index.html')

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

