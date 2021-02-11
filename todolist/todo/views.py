from django.shortcuts import render,redirect
from .models import *
from .forms import *
def index(request):
    task=list.objects.all()
    form=listform()
    if request.method=='POST':
        form=listform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={
        'task':task,
        'form':form
    }
    return render(request,'index.html',context)


def update(request,pk):
    task=list.objects.get(id=pk)
    form=listform(instance=task)
    if request.method=='POST':
        form=listform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update.html',context)


def delete(request,pk):
    item=list.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request,'delete.html',context)


# Create your views here.
