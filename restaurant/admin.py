# restaurant/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto, Informacion, Testimonio

# Configuración global del admin
admin.site.site_header = "🔥 Salchipollos Yarli - Admin"
admin.site.site_title = "Yarli Admin"
admin.site.index_title = "Panel de Control"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'productos_count')
    search_fields = ('nombre',)
    
    def productos_count(self, obj):
        count = obj.producto_set.count()
        return f"{count} productos"
    productos_count.short_description = "Total"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_simple', 'destacado', 'especial', 'disponible')
    list_filter = ('categoria', 'destacado', 'especial', 'disponible')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('destacado', 'especial', 'disponible')
    list_per_page = 20
    ordering = ('-destacado', '-especial', 'nombre')
    
    def precio_simple(self, obj):
        return f"S/ {obj.precio}"
    precio_simple.short_description = "Precio"

@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_restaurante', 'telefono')
    
    def has_add_permission(self, request):
        return not Informacion.objects.exists()

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puntuacion', 'fecha', 'activo', 'comentario_corto')
    list_filter = ('puntuacion', 'activo', 'fecha')
    search_fields = ('nombre', 'comentario')
    list_editable = ('activo',)
    ordering = ('-fecha',)
    
    def comentario_corto(self, obj):
        return obj.comentario[:50] + "..." if len(obj.comentario) > 50 else obj.comentario
    comentario_corto.short_description = "Comentario"