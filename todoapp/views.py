from django.shortcuts import render,redirect
from todoapp.models import Todo
from datetime import *

# Create your views here.
def addtodo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        if title == "":
            print('nodata')
        else:
            title=title.capitalize()
            disc=request.POST.get('description') or 'No discription'
            disc=disc.capitalize()
            todo=Todo(title=title,discript=disc,addtime=datetime.now())
            todo.save()
            return redirect('/')

def statuschange(request):
    if request.method=="POST":
        id=list(request.POST.keys())[1]
        obj=Todo.objects.get(id=id)
        obj.status='Completed'
        obj.save()
        print(obj.status)
    return redirect('/')

def deltodo(request):
    if request.method=="POST":
        id=list(request.POST.keys())[1]
        obj=Todo.objects.get(id=id)
        obj.delete()
    return redirect('/')

def index(request):
    todos=Todo.objects.all()
    return render(request, 'index.html',{'todos':todos})
