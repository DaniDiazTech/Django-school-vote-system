from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views

from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, login


MYEMAIL_VALIDATOR = RegexValidator(
    regex='^est\.[a-zA-ZÀ-ÿ\u00f1\u00d10-9]+@liceocarmelita\.edu\.co$',
    message='Lo siento ingresa un correo perteneciente al Liceo Carmelita',
    code='invalid_domain',
)

# email = forms.EmailField(required=True, validators=[MYEMAIL_VALIDATOR], label="Email", widget=forms.EmailInput(
#     attrs={'placeholder': 'Email', 'class': 'form-control bg-white border-left-0 border-md'}))
# full_name = forms.CharField(max_length=150, label="Nombre completo", widget=forms.TextInput(
#     attrs={'placeholder': 'Nombre y apellido', 'class': 'form-control bg-white border-left-0 border-md'}))
# grade = forms.Select(attrs={
#     'class': 'form-control',
# })


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, validators=[MYEMAIL_VALIDATOR], label="Email", widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    full_name = forms.CharField(max_length=150, label="Nombre completo", widget=forms.TextInput(
        attrs={'placeholder': 'Nombre y apellido'}))
    grade = forms.Select(attrs={

    })

    class Meta:
        model = get_user_model()
        fields = ("full_name",
                  "email", "password1", "password2", "grade")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields["username"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'

        # First password
        self.fields["password1"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password1"].widget.attrs["placeholder"] = 'Contraseña'

        # # Password confirmation
        self.fields["password2"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password2"].widget.attrs["placeholder"] = 'Confirmación'

        self.fields["grade"].label = 'Tu grado'
        self.fields["grade"].required = True
