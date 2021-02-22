from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (SignUpView, EditProfileSuccessView, UserEditView,
                    ChangePasswordView, ChangePasswordSuccessView, ShowProfileView)


app_name = "members"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_profile_success/",
         EditProfileSuccessView.as_view(), name="edit_success"),
    path("user/<int:pk>/",
         ShowProfileView.as_view(), name="profile"),
]
