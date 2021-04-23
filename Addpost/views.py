from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DetailView
import forum
from forum.models import Post


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

