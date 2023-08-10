from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from contact.forms import RegisterForm
from contact.models import *

def register(request):
    
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'usuário registrado com sucesso!')
            return redirect('contatos:index')
            
    context = {
        'form': form
    }
    
    return render(request, 'contact/register.html', context)
