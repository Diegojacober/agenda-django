from django.shortcuts import render

def index(request):
    print('vdfd')
    return render(request, template_name='contact/index.html')
