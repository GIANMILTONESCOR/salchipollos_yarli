# restaurant/views.py
from django.shortcuts import render
from .models import Producto, Categoria, Informacion

def home(request):
    productos_destacados = Producto.objects.filter(destacado=True)[:6]
    categorias = Categoria.objects.all()
    info = Informacion.objects.first()
    
    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
        'info': info,
    }
    return render(request, 'restaurant/home.html', context)

def menu(request):
    categorias = Categoria.objects.prefetch_related('producto_set').all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'restaurant/menu.html', context)

def nosotros(request):
    info = Informacion.objects.first()
    context = {
        'info': info,
    }
    return render(request, 'restaurant/nosotros.html', context)

