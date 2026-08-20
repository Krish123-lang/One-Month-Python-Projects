from django.shortcuts import render, get_object_or_404, redirect
from .forms import TodoForm
from todoapp.models import Todo
from django.contrib import messages
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, "todo/index.html", context)


def todo_details(request, pk):
    todo_details = get_object_or_404(Todo, pk=pk)
    return render(request, "todo/todo_details.html", {'todo_details': todo_details})


def create_todo(request):
    if request.method == "GET":
        form = TodoForm()
        context = {'form': form}
        return render(request, "todo/create_todo.html", context)

    elif request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo has been created!")
            return redirect("index")
        else:
            context = {'form': form}
            return render(request, "todo/create_todo.html", context)


def todo_update(request, pk):
    update_todo = get_object_or_404(Todo, pk=pk)

    if request.method == "GET":
        form = TodoForm(instance=update_todo)
        context = {'form': form, 'id': id}
        return render(request, "todo/create_todo.html", context)

    elif request.method == "POST":
        form = TodoForm(request.POST, instance=update_todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully!")
            return redirect('index')
        else:
            messages.error(request, "Something went wrong !")
            return render(request, "todo/create_todo.html", {'form': form})


def todo_delete(request, pk):
    del_todo = get_object_or_404(Todo, pk=pk)
    context = {'del_todo': del_todo}

    if request.method == "GET":
        return render(request, "todo/confirm_delete.html", context)
    elif request.method == "POST":
        del_todo.delete()
        messages.success(request, "The todo has been deleted !")
        return redirect('index')
