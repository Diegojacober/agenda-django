from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm


def create(request):
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
    
        return render(request, template_name='contact/create.html', context=context)
    
    context = {
            'form': ContactForm(),
            'site_title': 'Novo Contato',
    }

    return render(request, template_name='contact/create.html', context=context)