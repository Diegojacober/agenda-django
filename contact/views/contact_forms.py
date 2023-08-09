from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm


def create(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form
        }
        
        if form.is_valid():
            contact = form.save(commit=False) #Assim não salvo e posso fazer alterações e só depois salvar
            contact.show = True
            contact.save()
            return redirect('contact:index')
    
        return render(request, template_name='contact/create.html', context=context)
    
    context = {
            'form': ContactForm(),
            'site_title': 'Novo Contato',
    }

    return render(request, template_name='contact/create.html', context=context)