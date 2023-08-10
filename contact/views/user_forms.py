from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm
from contact.models import *

def register(request):
    
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuário registrado com sucesso!')
            return redirect('contacts:index')
            
    context = {
        'form': form
    }
    
    return render(request, 'contact/register.html', context)

def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f"Ola {user.username} seja bem vindo(a) novamente")
            return redirect('contact:index')
        else:
            messages.error(request, 'Login inválido')
            
    context = {
        'form': form
    }
    
    return render(request, 'contact/login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('contact:index')
    
