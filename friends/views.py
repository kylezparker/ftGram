from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Share, Profile
from django.urls import reverse
from django.db import models
from django.shortcuts import render, get_object_or_404
from friends.models import Profile
from django.http import HttpResponseRedirect


# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Share, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('share_detail', args=[str(pk)]))


class ShowProfilePageView(DetailView):
    model = Profile
    template_name= "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context ["page_user"] = page_user
        return context

class ShareListView(ListView):
    template_name = "friends/list.html"
    model= Share

class ShareDetailView(DetailView):
    template_name = "friends/detail.html"
    model= Share

class ShareCreateView(LoginRequiredMixin, CreateView):
    template_name = "friends/new.html"
    model= Share
    fields = ["title", "subtitle", "body", "author", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ShareUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "friends/edit.html"
    model= Share
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ShareDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "friends/delete.html"
    model= Share
    success_url = reverse_lazy("share_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
