from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import PostModel
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import *

# Create your views here.

# def homePage(request):
#     return render(request, 'posts/home.html')

class HomePage(generic.ListView):
    model = PostModel
    template_name = 'posts/home.html'
    context_object_name = 'posts'

class DetailPage(generic.DetailView):
    model = PostModel
    template_name = 'posts/detail.html'
    context_object_name = 'post'

class UpdatePage(generic.edit.UpdateView):
    model = PostModel
    success_url = ('/')
    template_name = 'posts/update.html'
    # fields = '__all__'
    form_class = PostForm


class DeletePage(generic.edit.DeleteView):
    model = PostModel
    success_url = ('/')


class CreatePage(LoginRequiredMixin,generic.edit.CreateView):
    model = PostModel
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = ('/')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
