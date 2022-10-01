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