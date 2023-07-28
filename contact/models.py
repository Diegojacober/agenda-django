from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d/')
    
    # Consultas lazy = não vão até a base de dados até que o valor seja requisitado
     
    
    def __str__(self) -> str:
        # Como vejo o usuário
        return f"{self.first_name} {self.last_name}"
