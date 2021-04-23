from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DetailView
from .models import Post
from .forms import CommentForm

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'forum/frontpage.html',{'posts':posts})

def post_detail(request , slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:

        form = CommentForm()
        

    return render(request, 'forum/post_detail.html',{'post':post , 'form':form })


