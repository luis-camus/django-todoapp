from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import todo
from .forms import TodoForm
from django.shortcuts import get_object_or_404
# Create your views here.
todos = todo.objects.all
def home(request):
    
    return render(request, 'landingpage.html', {'todos': todos})

def addtodo(request):
   
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save()
            response = JsonResponse({'id': new_todo.id, 'name': new_todo.name, 'priority': new_todo.priority, 'done': new_todo.done}, status=201)
            
            return render(request, 'landingpage.html', {'todos': todos})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_todo(request, todo_id):
     todo_item = get_object_or_404(todo, pk=todo_id)
     todo_item.delete()
    #  return render(request, '', {'todos': todos})
     todos = todo.objects.all
     render(request, 'landingpage.html', {'todos': todos})
     return redirect('/')