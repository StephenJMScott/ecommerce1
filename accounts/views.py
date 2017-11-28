from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required


def logout(request):
    auth.logout(request)
    return redirect('home')

    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            
            if user is not None:
                auth.login(request, user)
            else:
                form.add_error(None, "Your Username or Password was not recognised")
            
            return redirect('home')
    else:
        form = UserLoginForm()
        
        
    return render(request, "login.html", {'form': form})
    
def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                                     
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        form = UserRegistrationForm()

    
    return render(request, "register.html", {'form':form})


@login_required() 
def profile(request):
     return render(request, 'profile.html')