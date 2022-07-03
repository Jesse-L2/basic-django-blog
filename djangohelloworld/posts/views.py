from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.

class MessageBoardPageView(ListView):
    model = Post
    template_name = 'messageboard.html'
    context_object_name = 'all_posts_list'
