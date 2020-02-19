from django import forms
from django.contrib.auth.forms import AuthenticationForm


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(BaseForm):
    username = forms.CharField(widget=forms.TextInput, label= 'Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label= 'Пароль')
    email = forms.CharField(widget=forms.TextInput, label= 'Email')
    bio = forms.CharField(widget=forms.Textarea, label= 'О себе')
    location = forms.CharField(widget=forms.TextInput, label= 'Ваш город')


class LoginForm(AuthenticationForm, BaseForm):
    pass
