from django.shortcuts import render,redirect,HttpResponse
from .models import Task
from .forms import Taskform
# Create your views here.

# def home(request):
#     return render(request,"list.html")

def Addtask(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()  
        return redirect ('/')
    else:
        form = Taskform()
        return render(request,"list.html",{'form':form ,'tasks':tasks})  
    
def delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')

def update_task(request,pk):
    task = Task.objects.get(pk=pk)    
    if request.method == "POST":
        form = Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Taskform(instance=task)
    return render (request,"update.html",{'form':form})        
            
    
