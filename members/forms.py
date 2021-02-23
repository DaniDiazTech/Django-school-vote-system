from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control bg-white border-left-0 border-md'}))
    full_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control bg-white border-left-0 border-md'}))

    class Meta:
        model = get_user_model()
        fields = ("full_name",
                  "email", "password1", "password2", "grade")


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields["username"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'

        # First password
        self.fields["password1"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password1"].widget.attrs["placeholder"] = 'Password'

        # # Password confirmation
        self.fields["password2"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password2"].widget.attrs["placeholder"] = 'Confirm'
    def mylogin(self):
        
        pass
        # def form_valid(self, form):
        # to_return = super().form_valid(form)
        # user = authenticate(
        #     email=form.cleaned_data["email"],
        #     password=form.cleaned_data["password1"],
        # )
        # login(self.request, user)
        # return to_return

