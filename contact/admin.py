from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #Campos que desejo mostrar na listagem dos registros
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'description',)
    #Ordenando por qual campo. Crescente id, descrescente -id
    ordering = ('id',)
    #Filtrar
    list_filter = ('created_at', )
    #Pesquisas
    search_fields = ('id', 'first_name', 'last_name', 'phone', 'email')
    # Paginação
    list_per_page = 10
    list_max_show_all = 100
    #Editar sem entrar no registro
    list_editable = ('first_name', 'last_name',)
    #Link para o registro
    list_display_links = ('id', 'phone',)
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)