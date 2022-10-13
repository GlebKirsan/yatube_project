from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    template = "posts/index.html"
    return render(request, template)


def group_posts(request: HttpRequest, slug: str):
    template = "posts/group_list.html"
    return render(request, template)
