from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class DeleteList(DeleteView):
    model = Post


class CreateList(CreateView):
    model = Post
    fields = ('title', 'content', 'image', 'slug')
    template_name = 'post/create.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/detail.html'