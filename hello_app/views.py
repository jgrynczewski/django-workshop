import datetime

from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")


def hello_name(request, name):
    sanitize_name = escape(name)
    return HttpResponse(f"Hello, {sanitize_name}")


def hello_template(request, name):
    # return HttpResponse("<html><head></head><body><h1>Hello, world!</h1></body></html>")
    return render(request, "hello_app/hello.html", context={"name": name})


def is_it_monday(request):
    now = datetime.datetime.now()

    is_monday = now.weekday() == 0

    return render(
        request,
        "hello_app/isitmonday.html",
        context={"is_monday": is_monday}
    )


def dtl(request):
    fruits = [
        "jabłko",
        "banan",
        "winogrono",
    ]
    user = {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 20
    }

    class Cow:
        def __init__(self, name):
            self.name = name

    cow1 = Cow("Mućka")

    return render(
        request,
        "hello_app/dtl.html",
        context={
            "fruits": fruits,
            "user": user,
            "cow1": cow1
        }
    )


def first_view(request):
    return render(
        request, "hello_app/first.html"
    )


def second_view(request):
    return render(
        request, "hello_app/second.html"
    )


def third_view(request, param):
    return render(
        request, "hello_app/third.html", {"param": param}
    )