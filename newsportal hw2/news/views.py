from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'news.html'
    context_object_name = 'news'


class ItemDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'
