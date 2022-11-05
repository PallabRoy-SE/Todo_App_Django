from django.shortcuts import render, redirect
from django.utils import timezone
from todo_app.models import Todo

# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {"todo_items": todo_items})

def add_todo(request):
    if request.method == "POST":
        todo_items = request.POST.get('todo')
        todo = Todo(text=todo_items, added_date=timezone.now())
        todo.save()
        return redirect('/')
    return redirect('/')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')