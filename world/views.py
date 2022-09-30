from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Msg
from django.urls import reverse



# Create your views here.

class MsgListView(ListView):
    template_name = "world/list.html"
    model= Msg

class MsgDetailView(DetailView):
    template_name = "world/detail.html"
    model= Msg

class MsgCreateView(LoginRequiredMixin, CreateView):
    template_name = "world/new.html"
    model= Msg
    fields = ["title", "subtitle", "body", "author"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MsgUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "world/edit.html"
    model= Msg
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class MsgDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "world/delete.html"
    model= Msg
    success_url = reverse_lazy("msg_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
