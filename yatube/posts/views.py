from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    template = "posts/index.html"
    return render(request, template)


def group_posts(request: HttpRequest, slug: str):
    return HttpResponse(f"Посты групп {slug}")
