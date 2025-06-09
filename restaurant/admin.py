# restaurant/admin.py
from django.contrib import admin
from .models import Categoria, Producto, Informacion

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'destacado')
    list_filter = ('categoria', 'destacado')
    search_fields = ('nombre', 'descripcion')

@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_restaurante', 'telefono')
    
    def has_add_permission(self, request):
        return not Informacion.objects.exists()

# restaurant/apps.py
from django.apps import AppConfig

class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'