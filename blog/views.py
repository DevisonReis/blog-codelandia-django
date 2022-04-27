from django.views.generic import DetailView, ListView
from .models import Post
from django.core.paginator import Paginator
from django.shortcuts import render

class PostListView(ListView):
    paginate_by = 3
    model = Post

class PostDetailView(DetailView):
    model = Post
