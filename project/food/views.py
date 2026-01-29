from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.

def homepage(request):
    return render(request, 'food/index.html')

def menu(request):
    items=item.objects.all()
    context={
        'items':items,
    }
    return render(request, 'food/menu.html', context)