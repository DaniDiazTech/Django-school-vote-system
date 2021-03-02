from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

# from django.http import HttpResponseRedirect

# from django.urls import reverse_lazy

from .models import *

# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
    
    model = Candidate

    # queryset = Candidate.objects.filter(level=self.request.user.level)

    template_name = "voting/home.html"
    context_object_name = "candidates"
    login_url = 'members:signup'

    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.filter(level=self.request.user.grade.level)
    


class CandidateDetailView(DetailView):
    model = Candidate
    template_name = "voting/details.html"


class SuccessView(TemplateView):
    template_name = "voting/success.html"


def VoteCandidateView(request, pk):
    candidate = Candidate.objects.get(id=pk)

    if candidate.votes.filter(id=request.user.id).exists():
        return HttpResponseRedirect(reverse('vote:success'))
    else:
        candidate.votes.add(request.user)
        return HttpResponseRedirect(reverse('vote:success'))
    return HttpResponseRedirect(reverse('vote:home'))

    # if post.upvotes.filter(id=request.user.id).exists():
    #     post.upvotes.remove(request.user)
    # else:
    #     post.upvotes.add(request.user)
    # return HttpResponseRedirect(reverse('blog:article_page', args=[str(pk)]))