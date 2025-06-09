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
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    especial = models.BooleanField(default=False, help_text="Plato especial de la casa")
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-destacado', '-especial', 'nombre']

class Informacion(models.Model):
    nombre_restaurante = models.CharField(max_length=200, default="Salchipollos Yarli")
    slogan = models.CharField(max_length=300, default="El Mejor Sabor de la Amazonía")
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    horario = models.TextField()
    sobre_nosotros = models.TextField()
    mision = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.nombre_restaurante
    
    class Meta:
        verbose_name_plural = "Información del Restaurante"

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)], 
        default=5,
        help_text="Puntuación de 1 a 5 estrellas"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.puntuacion} estrellas"
    
    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = "Testimonios"