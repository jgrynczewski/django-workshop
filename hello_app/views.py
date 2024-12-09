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
    return render(request, "hello.html", context={"name": name})
