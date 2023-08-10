from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from contact.forms import RegisterForm
from contact.models import *

def register(request):
    
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.isValid():
            form.save()
    
    context = {
        'form': form
    }
    
    return render(request, 'contact/register.html', context)
