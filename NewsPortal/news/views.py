from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


# class PostList(ListView):
#     model = Post
#     ordering = 'title'
#     template_name = 'posts.html'
#     context_object_name = 'posts'


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'singular_news.html'
    context_object_name = 'singular_news'

