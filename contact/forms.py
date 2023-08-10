from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from typing import Any, Dict

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(
             attrs={
                'placeholder': 'Nome do contato' #referente aos atributos, placeholder, classe
            }
        ),
        help_text='Digite o nome do novo contato',
        label='Primeiro Nome',
    )
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture' )
        
       
        
        

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            self.add_error( 'first_name' , ValidationError('Primeiro nome não pode ser igual ao segundo nome', code='Invalid'))
            self.add_error( 'last_name' , ValidationError('Primeiro nome não pode ser igual ao segundo nome', code='Invalid'))
        
        # self.add_error(
        #     None, ValidationError('Mensagem de erro', code='invalid')
        # )
        
        # self.add_error(
        #     None, ValidationError('Mensagem de erro 2', code='invalid')
        # )
        
        return super().clean() 
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            raise ValidationError('Não Digite ABC', code='invalid')
        
        return first_name