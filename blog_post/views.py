from django import urls
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.template import loader
from django.shortcuts import render

from blog_post.models import Post, Rubric
# Create your views here.

def index(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    context = {'posts': posts, 'rubrics': rubrics}
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    posts = Post.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'posts': posts, 'rubrics':rubrics,
                'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)

def by_post(request, post_id):
    # do the same as by_rubric to render the html with one post
    posts = Post.objects.all()
    current_post = Post.objects.get(pk=post_id)
    # how to get the rubric of the post????
    current_rubric = current_post.rubric
    context = {'current_post': current_post, 'current_rubric': current_rubric}
    return render(request, 'by_post.html', context)

def about(request):
    return render(request, 'about.html')