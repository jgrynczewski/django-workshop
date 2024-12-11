from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from form_app.models import Task


TASKS = []

# formularz get
def form1(request):
    data = request.GET

    task = data.get('task')
    if task:
        TASKS.append(task)

    return render(request, "form_app/form1.html")

# formularz post
def form2(request):
    if request.method == "GET":
        return render(request, "form_app/form2.html")

    elif request.method == "POST":
        data = request.POST
        task = data.get('task')

        if task:
            TASKS.append(task)
            return redirect("form_app:task_list")

        return render(request, "form_app/form2.html")
    else:
        return HttpResponse(status=405)


def task_list(request):
    return render(
        request,
        "form_app/task_list.html",
        {"tasks": TASKS}
    )


def task_create_view(request):
    if request.method == "GET":
        return render(request, "form_app/task_form.html")

    elif request.method == "POST":
        data = request.POST
        new_task = data.get('task')

        if new_task:
            Task.objects.create(name=new_task)
            return redirect("form_app:task_list_view")

        return render(request, "form_app/task_form.html")
    else:
        return HttpResponse(status=405)


def task_list_view(request):
    return render(
        request,
        "form_app/task_list.html",
        {"tasks": Task.objects.all()}
    )


def task_detail_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    return render(
        request,
        "form_app/task_detail.html",
        {"task": task}
    )


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "GET":
        return render(request, "form_app/task_update.html", {"task": task})

    elif request.method == "POST":
        data = request.POST
        new_task = data.get('task')

        if new_task:
            task.name = new_task
            task.save()
            return redirect("form_app:task_list_view")

        return render(request, "form_app/task_update.html", {"task": task})
    else:
        return HttpResponse(status=405)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "GET":
        return render(
            request,
            "form_app/task_confirm_delete.html",
            {"task": task}
        )
    elif request.method == "POST":
        data = request.POST

        if 'confirm' in data:
            task.delete()

            return redirect("form_app:task_list_view")

        return render(request, "form_app/task_confirm_delete.html", {"task": task})

    else:
        return HttpResponse(status=405)
