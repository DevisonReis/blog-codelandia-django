from django.views.generic import DetailView, ListView
from .models import Post
from django.views.generic.edit import CreateView

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
