from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.http import HttpResponseRedirect

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


from django.contrib.auth import logout


# Create your views here.
from .forms import *


class SignUpView(generic.CreateView):
    """
    Allow the User to Create a New Account
    """
    form_class = SignUpForm
    template_name = "registration/singup.html"
    success_url = reverse_lazy('vote:home')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse_lazy('vote:home'))
