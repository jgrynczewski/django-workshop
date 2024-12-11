from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.http import require_http_methods

User = get_user_model()


def home(request):
    return render(
        request,
        "accounts/home.html",
    )


def register_view(request):
    if request.method == "GET":
        return render(
            request,
            "accounts/register.html"
        )
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if password1 != password2:
            return HttpResponse("Podane hasła nie pasują do siebie")

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("accounts:home")


def login_view(request):
    if request.method == "GET":
        return render(
            request,
            "accounts/login.html"
        )
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return HttpResponse("Podano nieprawidłowe dane")

        # uwierzytelnienie
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            # logowanie (mechanizm sesji)
            login(request, user)

        return redirect("accounts:home")


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return redirect("accounts:home")
