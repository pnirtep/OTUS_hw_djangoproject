from django import forms


class ContactPostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    name = forms.CharField(max_length=25, label='Ваше имя')
    user_email = forms.EmailField(label='Ваш email')
    message = forms.CharField(required=False, widget=forms.Textarea, label='Ваше сообщение')
