from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from typing import Any, Dict

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
             attrs={
                'placeholder': 'Nome do contato' #referente aos atributos, placeholder, classe
            }
        ),
        help_text='Digite o nome do novo contato',
        label='Primeiro Nome',
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)
        
       
        
        

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None, ValidationError('Mensagem de erro', code='invalid')
        )
        
        self.add_error(
            None, ValidationError('Mensagem de erro 2', code='invalid')
        )
        
        return super().clean()    