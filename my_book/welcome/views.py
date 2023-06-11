from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from welcome.forms import MessageForm
from welcome.models import Message
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class homeview(TemplateView):
    template_name = "welcome/home.html"


class listview(LoginRequiredMixin, ListView):
    template_name = "welcome/list.html"
    model = Message
    fields = "__all__"
    context_object_name = "message"


class detailview(LoginRequiredMixin, DetailView):
    template_name = "welcome/detail.html"
    model = Message
    fields = "__all__"
    context_object_name = "post"


class Createview(LoginRequiredMixin, CreateView):
    template_name = "welcome/create.html"
    model = Message
    # fields = "__all__"
    form_class = MessageForm
