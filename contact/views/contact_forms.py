from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import *



@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Novo Contato',
        }
        
        if form.is_valid():
            contact = form.save(commit=False) #Assim não salvo e posso fazer alterações e só depois salvar
            contact.show = True
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(request, template_name='contact/create.html', context=context)
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'site_title': 'Novo Contato',
    }

    return render(request, template_name='contact/create.html', context=context)


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST,  request.FILES, instance=contact)
        
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


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 'contact/contact.html', {'contact': contact, 'confirmation': confirmation})
    
 
