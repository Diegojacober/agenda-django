from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from typing import Any, Dict

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone',

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None, ValidationError('Mensagem de erro', code='invalid')
        )
        
        self.add_error(
            None, ValidationError('Mensagem de erro 2', code='invalid')
        )
        
        return super().clean()    