from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'diary/post_list.html'
    paginate_by = 9

class PostDetail(DetailView):
    model = Post
