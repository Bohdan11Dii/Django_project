from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


def index(request):
    return render(request, 'dota/index.html')


def about(request):
    return render(request, 'dota/about/about.html')


def gallery(request):
    return render(request, 'dota/Gallery/gallery.html')


def ourteam(request):
    posts = Dota.objects.all()
    return render(request, 'dota/ourteam/our.html', {'posts': posts, 'title': ''})


def logo(request):
    return render(request, 'dota/index.html')


def show_post(request, post_id):
    post = get_object_or_404(Dota, pk=post_id)

    context = {
        'post': post,
        'title': post.title
    }
    return render(request, 'dota/post.html', context=context)






def login(request):
    return render(request, 'dota/login/login.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
