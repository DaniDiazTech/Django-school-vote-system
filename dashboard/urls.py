from django.urls import path

from .views import *

app_name = "dashboard"

urlpatterns = [
    path("", DashboardHomeView.as_view(), name="home"),
    path("elementary/", DashboardElementaryView.as_view(), name="elementary"),
    path("high_school/", DashboardHighSchoolView.as_view(), name="high"),
    path("notallowed/", DashboardNotAllowedView.as_view(), name="not"),
]
