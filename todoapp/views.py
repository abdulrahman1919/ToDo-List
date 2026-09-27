from django.shortcuts import render,redirect
from todoapp.models import Todo
from datetime import *

# Create your views here.
def addtodo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        disc=request.POST.get('description') or 'no discription'
        todo=Todo(title=title,discript=disc,addtime=datetime.now())
        todo.save()
        return redirect('/')
def index(request):
    return render(request, 'index.html')