from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost


# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    context_object_name = 'blog_posts'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    # reverse_lazy doesn't execute the URL redirect until our view has finished deleting the blog post
    success_url = reverse_lazy('blog')
