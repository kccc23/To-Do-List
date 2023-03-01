from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm

# Create your views here.

def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_lists": todo_lists,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id=id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect('todo_list_detail', id=todo_list.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo_list.id)
    else:
        form = TodoListForm(instance=todo_list)
    context = {
        "todo_list": todo_list,
        "form": form,
    }
    return render(request, "todos/update.html", context)

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")

def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save()
            return redirect('todo_list_detail', id=todo_item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create_item.html", context)

def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo_item.list.id)
    else:
        form = TodoItemForm(instance=todo_item)
    context = {
        "todo_item": todo_item,
        "form": form,
    }
    return render(request, "todos/update_item.html", context)
