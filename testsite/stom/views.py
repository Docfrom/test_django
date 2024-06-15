from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = [{"title": "О сайте", "url_name": "about"},
        {"title": "Врачи", "url_name": "doctor"},
        {"title": "Услуги", "url_name": "service"},
        {"title": "Войти", "url_name": "login"}]

data_db = [
    {'id': 1, 'title': 'Fedotov', 'content': '''Врач-стоматолог-ортопед-хирург. Операции костной пластики, утановка дентальных имплантов любой сложности, лечение и реабилитация челюстых аномалий и заболеваний ВНЧС ''', 'is_published': True},
    {'id': 2, 'title': 'Immamdinov', 'content': 'Surgeon', 'is_published': False},
    {'id': 3, 'title': 'Pogorelov', 'content': 'Universal', 'is_published': True},
]

def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db
            }
    return render(request, 'stom/index.html', context=data)

def about(request):
    return render(request, 'stom/about.html', {'title': 'О сайте', 'menu': menu})

def doctors(request):
    # return HttpResponse(f"<h1>Наши врачи</h1><p>ФИО: {docsl}</p>")
    return HttpResponse("Наши врачи")

def service(request):
    # return HttpResponse(f"<h1>Список услуг</h1><p>ID: {serv_id}</p>")
    return HttpResponse("Список услуг")

def archive(request, year):
    if year > 2024:
        uri = reverse('doctor', args=('test',))
        return redirect(uri)
    return HttpResponse(f"<h1>Тест регулярки</h1><p>Result: {year}</p>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение ID = {post_id}")

def login(request):
    return HttpResponse('Авторизация')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")