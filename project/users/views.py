from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignupForm
from django.contrib import messages
# Create your views here.

def signup(request):
    form=UserSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account created successfully")
            return redirect('users:login')
    context={
        'form':form,
    }

    return render(request, 'users/signup.html', context)
