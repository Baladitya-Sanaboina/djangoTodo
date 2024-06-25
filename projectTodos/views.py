from django.shortcuts import render
from todo.models import todo
def home(request):
    list_todos = todo.objects.filter(is_completed = False)
    context = {
        'todos': list_todos
    }
    return render(request, 'home.html', context)