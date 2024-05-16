from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Todo
from .forms import TodoForm
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    todos = Todo.objects.filter(user_id=request.user.id)
    return render(request, 'landingpage.html', {'todos': todos})

def addtodo(request):
    todos = Todo.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = TodoForm(request.POST, request=request)

        if form.is_valid():
            new_todo = form.save()
            response = JsonResponse({'id': new_todo.id, 'name': new_todo.name, 'priority': new_todo.priority, 'done': new_todo.done}, status=201)
            return render(request, 'landingpage.html', {'todos': todos})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_todo(request, todo_id):
     todo_item = get_object_or_404(Todo, pk=todo_id)
     todo_item.delete()
    #  return render(request, '', {'todos': todos})
     todos = Todo.objects.all
     render(request, 'landingpage.html', {'todos': todos})
     return redirect('/')

def edit_todo(request, todo_id):
    # newtodoname = request.POST['todo_name']
    name = get_object_or_404(Todo, pk=todo_id)
    todos = Todo.objects.all
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=name, request=request)
        if form.is_valid():
            form.save()
            render(request, 'landingpage.html', {'todos': todos})
            return redirect('/')
    