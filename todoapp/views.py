from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def index(request):
    if request.method == 'POST':
        text = request.POST.get("text", "").strip()
        if text:
            Todo.objects.create(text=text)
            print(text)
        return redirect('/')
    
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoapp/index.html', context)


def deleteTodo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')


def about(request):
    return render(request, 'todoapp/about.html')




