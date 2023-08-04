from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

def index(request):
    # filtrando onde show é true e ordena por id crescente
    contacts = Contact.objects.filter(show=True).order_by('id')[:10]
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos',
    }
    
    return render(request, template_name='contact/index.html', context=context)

def contact(request, contact_id):
    # single_contact = Contact.objects.get(pk=contact_id) # Retorna um dado
    # single_contact = Contact.objects.filter(pk=contact_id).last() # Retorna uma queryset (uma lista), por isso o last() para pegar somente o ultimo
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True)) # faz automaticamente e se precisar retorna o 404

    context = {
        'contact': single_contact,
        'site_title': f"{single_contact.first_name} {single_contact.last_name}",
    }
    
    return render(request, template_name='contact/contact.html', context=context)

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
    
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
    # filter(first_name__icontains=search_value, last_name__icontains=search_value) == AND
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) |  Q(email__icontains=search_value)).order_by('id')[:10] # OR
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos',
    }
    
    return render(request, template_name='contact/index.html', context=context)

