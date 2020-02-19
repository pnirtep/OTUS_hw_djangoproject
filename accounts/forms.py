from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from courses.models import Student


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(BaseForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.TextInput)
    bio = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(widget=forms.TextInput)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
