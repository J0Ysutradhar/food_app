from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    form=UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('hotel:homepage')
    context={
        'form':form,
    }

    return render(request, 'users/signup.html', context)
