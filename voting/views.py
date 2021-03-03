from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, View

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse

from .models import *

# Create your views here.


class Userhasntvoted(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.has_voted 
    
    def handle_no_permission(self):
        '''
        If the user has voted, redirect  to the already_voted view
        '''
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponseRedirect(reverse_lazy('vote:already'))

class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = 'members:signup'


class HomeView(CustomLoginRequiredMixin, Userhasntvoted, ListView):
    
    model = Candidate

    # queryset = Candidate.objects.filter(level=self.request.user.level)

    template_name = "voting/home.html"
    context_object_name = "candidates"

    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.filter(level=self.request.user.grade.level)
    

class AlreadyVoted(TemplateView):
    template_name = "voting/already_voted.html"


# class CandidateDetailView(LoginRequiredMixin, DetailView):
#     model = Candidate
#     template_name = "voting/details.html"
#     login_url = 'members:signup'
#     context_object_name = "candidate"


class SuccessView(TemplateView):
    template_name = "voting/success.html"


def VoteCandidateView(request, pk):
    candidate = Candidate.objects.get(id=pk)

    if candidate.votes.filter(id=request.user.id).exists():
        """
        If the user has already voted, redirect to the success
        """
        return HttpResponseRedirect(reverse('vote:success'))
    else:
        candidate.votes.add(request.user)
        user = request.user
        user.has_voted = True
        user.save()
        return HttpResponseRedirect(reverse('vote:success'))
    return HttpResponseRedirect(reverse('vote:home'))

    # if post.upvotes.filter(id=request.user.id).exists():
    #     post.upvotes.remove(request.user)
    # else:
    #     post.upvotes.add(request.user)
    # return HttpResponseRedirect(reverse('blog:article_page', args=[str(pk)]))