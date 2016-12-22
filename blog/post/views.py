from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'home.html'
    ordering = '-time_created'

    def get_queryset(self):
        qs = self.model.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        qs = qs.order_by(self.get_ordering())
        return qs



class DeleteList(DeleteView):
    model = Post


class CreateList(CreateView):
    model = Post
    fields = ('title', 'content', 'image', 'slug')
    template_name = 'post/create.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post/detail.html'
    fields = ('title', 'content', 'image', 'slug')