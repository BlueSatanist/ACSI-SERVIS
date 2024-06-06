from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



categories = Categories.objects.all()  # Получаем все категории

def index(request):


    context = {
         
        'categories': categories, 
        'is_index_page': True,
        'title': 'АКСИ-СЕРВИС',
        'content': "Торгово-сервисная компания АКСИ-СЕРВИС",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'АКСИ-СЕРВИС - О нас',
        'content': "О нас",
        'is_index_page': False,
        'text_on_page': "Мы рады приветствовать вас на нашей онлайн-платформе"
    }

    return render(request, 'main/about.html', context)