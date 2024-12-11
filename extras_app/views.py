# https://fly.io/django-beats/running-tasks-concurrently-in-django-asynchronous-views/
import time
import asyncio

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

from orm_app.models import Task
from forms_and_views_app.models import Message


# Ciasteczka i sesjsa

def cookies(request):
    print(request.COOKIES)
    res = HttpResponse("OK")
    res.set_cookie("ciasteczko1", 5)
    # res.set_cookie("ciasteczko2", 10, max_age=100)  # liczba sekund do wygaśnięcia
    return res


def home_view(request):
    msg = request.COOKIES.get('msg')
    res = render(
        request,
        'extras_app/home.html',
        {
            'msg': msg
        }
    )
    res.delete_cookie('msg')

    return res


# Zastosowanie ciasteczek. Przekazywanie danych przy redirect.
def form_view(request):
    if request.method == "GET":
        return render(
            request,
            'extras_app/form.html'
        )
    elif request.method == "POST":
        data = request.POST

        # save data

        res = redirect('extras_app:home')
        res.set_cookie("msg", "Pomyslnie zapisano nowy post id=xxx")

        return res


# build-in messages frameworks
# https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
def home_view2(request):
    msg = request.COOKIES.get('msg')
    res = render(
        request,
        'extras_app/home2.html',
        {
            'msg': msg
        }
    )
    res.delete_cookie('msg')

    return res


def form_view2(request):
    if request.method == "GET":
        return render(
            request,
            'extras_app/form.html'
        )
    elif request.method == "POST":
        data = request.POST

        # save data
        # ...

        messages.add_message(request, messages.SUCCESS, "Pomyslnie zapisano nowy post id=xxx")
        # messages.debug(request, "%s SQL statements were executed." % count)
        # messages.info(request, "Three credits remain in your account.")
        # messages.success(request, "Profile details updated.")
        # messages.warning(request, "Your account expires in three days.")
        # messages.error(request, "Document deleted.")

        return redirect('extras_app:home2')


# Sesja - mechanizm opierający się na ciasteczkach.
def session(request):
    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit
    return HttpResponse(f'Liczba odwiedzin: {num_visit}')


### Widoki asynchroniczne

# helper functions
def get_tasks_sync():
    print('Fetching tasks started.')
    time.sleep(2)
    qs = Task.objects.all()
    print(qs)
    print("Fetching tasks completed.")

def get_messages_sync():
    print('Fetching messages started.')
    time.sleep(5)
    qs = Message.objects.all()
    print(qs)
    print("Fetching messages completed.")


# widok synchroniczny
def main_sync_view(request):
    start_time = time.time()
    get_messages_sync()
    get_tasks_sync()
    total = time.time() - start_time
    print(f"Total: {total}")
    return HttpResponse(f"sync")

# Mamy dwie operacje blokujące: sleep i operacje bazodanową.
# od wersji Django 4.1 wywołania orm można używać bez użcie
# dekorator sync_to_async, za pomocą składni async for
# https://docs.djangoproject.com/en/5.1/releases/4.1/#asynchronous-orm-interface

async def get_tasks_async():
    print('Fetching tasks started.')
    await asyncio.sleep(5)
    qs = [task async for task in Task.objects.all()]
    print(qs)
    print("Fetching tasks completed.")


async def get_messages_async():
    print('Fetching messages started.')
    await asyncio.sleep(2)
    qs = [msg async for msg in Message.objects.all()]
    print(qs)
    print("Fetching messages completed.")


# widok asynchroniczny
async def main_async_view(request):
    start_time = time.time()
    await asyncio.gather(
        get_tasks_async(),
        get_messages_async()
    )
    total = time.time() - start_time
    print(f"Total: {total}")
    return HttpResponse(f"async")

### Uwagi

# 1. serwer nie pracuje w trybie asgi, więc
# poszczególne zapytania które będą wpadały wciąż muszą
# być przetwarzane synchronicznie (np. dapne, uvicorn)
# dyskujsa o wspraciu asynchroniczności przez wbudowany w django
# serwer deweloperski:
# https://forum.djangoproject.com/t/adding-asgi-support-to-runserver/2446/32

# 2. konektor bazodanowy nie jest asynchroniczny,
# więc zapytania do bazy na koniec są synchroniczne.
# Na przykład dla postgresa zamiast psycopg może być asyncpg

# Jeżeli chcielibyśmy coś pobierać z zewnętrznego api
# to potrzebny byłby asynchroniczny klient http,
# np. httpx, aiohttp
