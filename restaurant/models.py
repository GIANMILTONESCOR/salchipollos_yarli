# restaurant/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class Informacion(models.Model):
    nombre_restaurante = models.CharField(max_length=200, default="Salchipollos Yarli")
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True)
    horario = models.TextField()
    sobre_nosotros = models.TextField()
    
    def __str__(self):
        return self.nombre_restaurante
    
    class Meta:
        verbose_name_plural = "Información del Restaurante"

