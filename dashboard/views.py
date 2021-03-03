from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from django.contrib.auth.mixins import UserPassesTestMixin

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from voting.views import CustomLoginRequiredMixin

# Candidate model

from voting.models import Candidate


# path("", DashboardHomeView.as_view(), name="home"),
# path("elementary/", DashboardElementaryView.as_view(), name="elementary"),
# path("high_school/", DashboardHighSchoolView.as_view(), name="high"),
# path("notallowed/", DashboardNotAllowedView.as_view(), name="high"),

class IsStaff(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        '''
        If the user has voted, redirect  to the already_voted view
        '''
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponseRedirect(reverse_lazy('dashboard:not'))
    

class DashboardPermission(CustomLoginRequiredMixin, IsStaff):
    """
    Manage if the user is authenticated, if not it redirects him to the sign up page:
    Then if the user is authenticated, but if he isn't staff shows an error page
    """


class DashboardHomeView(DashboardPermission, TemplateView):
    """
    Home page that allows to choose between high school and elementary
    """
    template_name = "dashboard/home.html"


    
class DashboardNotAllowedView(TemplateView):
    """
    Custom Permision Denied Page
    """
    template_name = "dashboard/not_allowed.html"


class DashboardElementaryView(DashboardPermission, TemplateView):
    template_name = "dashboard/elementary.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidates"] = Candidate.objects.filter(level=1)
        return context
    

class DashboardHighSchoolView(DashboardPermission, TemplateView):
    template_name = "dashboard/high.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidates"] = Candidate.objects.filter(level=2)
        return context
    