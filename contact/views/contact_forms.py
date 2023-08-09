from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import *

def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Novo Contato',
        }
        
        if form.is_valid():
            contact = form.save(commit=False) #Assim não salvo e posso fazer alterações e só depois salvar
            contact.show = True
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(request, template_name='contact/create.html', context=context)
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'site_title': 'Novo Contato',
    }

    return render(request, template_name='contact/create.html', context=context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Novo Contato',
        }
        
        if form.is_valid():
            contact = form.save(commit=False) #Assim não salvo e posso fazer alterações e só depois salvar
            contact.show = True
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(request, template_name='contact/create.html', context=context)
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'site_title': 'Novo Contato',
    }

    return render(request, template_name='contact/create.html', context=context)