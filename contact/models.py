from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # Consultas lazy = não vão até a base de dados até que o valor seja requisitado
     
    
    def __str__(self) -> str:
        # Como vejo o usuário
        return f"{self.first_name} {self.last_name}"

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ["id"]
