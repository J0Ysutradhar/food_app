from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import item
from .forms import add_item
# Create your views here.

def homepage(request):
    return render(request, 'food/index.html')

def menu(request):
    items=item.objects.all()
    context={
        'items':items,
    }
    return render(request, 'food/menu.html', context)

def add_food(request):
    form=add_item(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('food:menu')
    
    context={
        'form':form, 
    }
    return render(request, 'food/add_item.html', context=context)

def detail(request, id):
    food_item=item.objects.get(id=id)
    context ={
        'food_item':food_item,
    }
    return render(request, 'food/detail.html', context)

def edit_item(request, id):
    instance= item.objects.get(id=id)    
    form=add_item(request.POST or None, instance=instance)

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('food:menu')
    
    context={
        'form':form,
    }
    return render(request, 'food/add_item.html', context)