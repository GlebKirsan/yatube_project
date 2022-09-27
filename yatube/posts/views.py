from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    return HttpResponse("Главная страница")


def group_posts(request: HttpRequest, slug: str):
    return HttpResponse(f"Посты групп {slug}")
