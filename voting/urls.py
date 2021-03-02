from django.urls import path

from .views import *

app_name = "vote"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("success/", SuccessView.as_view(), name="success"),
    path("candidate/<int:pk>", CandidateDetailView.as_view(), name="home"),
    path("voting/<int:pk>", VoteCandidateView, name="home"),
]
