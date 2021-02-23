from django.urls import path
from django.contrib.auth import views as auth_views

from .views import  *

app_name = "members"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("mylogout/", logout_view, name="mylogout"),
]
