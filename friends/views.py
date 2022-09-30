from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Share
from django.urls import reverse



# Create your views here.

class ShareListView(ListView):
    template_name = "friends/list.html"
    model= Share

class ShareDetailView(DetailView):
    template_name = "friends/detail.html"
    model= Share

class ShareCreateView(LoginRequiredMixin, CreateView):
    template_name = "friends/new.html"
    model= Share
    fields = ["title", "subtitle", "body", "author"]

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
