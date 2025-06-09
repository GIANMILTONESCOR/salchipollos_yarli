# Comandos para configurar y ejecutar el proyecto

# 1. Crear el proyecto Django
# django-admin startproject salchipollos_yarli
# cd salchipollos_yarli
# python manage.py startapp restaurant

# 2. Ejecutar migraciones
# python manage.py makemigrations
# python manage.py migrate

# 3. Crear superusuario
# python manage.py createsuperuser

# 4. Ejecutar el servidor
# python manage.py runserver

# restaurant/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from restaurant.models import Categoria, Producto, Informacion

class Command(BaseCommand):
    help = 'Carga datos iniciales para Salchipollos Yarli'

    def handle(self, *args, **options):
        # Crear categorías
        categoria_principales, created = Categoria.objects.get_or_create(
            nombre="Platos Principales",
            defaults={'descripcion': 'Deliciosos platos principales de la cocina amazónica'}
        )
        
        categoria_bebidas, created = Categoria.objects.get_or_create(
            nombre="Bebidas",
            defaults={'descripcion': 'Refrescantes bebidas naturales de la selva'}
        )
        
        categoria_postres, created = Categoria.objects.get_or_create(
            nombre="Postres",
            defaults={'descripcion': 'Dulces y heladitas para refrescarse'}
        )

        # Crear productos principales
        productos_principales = [
            {
                'nombre': 'Salchipollos Especial',
                'descripcion': 'Nuestro plato estrella preparado con pollo tierno, salchichas de calidad y nuestra sazón secreta que nos distingue. Acompañado de papas fritas y ensalada fresca.',
                'precio': 15.00,
                'destacado': True
            },
            {
                'nombre': 'Aguadito Amazónico',
                'descripcion': 'Delicioso aguadito con pollo, arroz y cilantro fresco. Preparado con ingredientes locales para un sabor único que reconforta el alma.',
                'precio': 12.00,
                'destacado': True
            },
            {
                'nombre': 'Arroz con Pollo Tradicional',
                'descripcion': 'Tradicional arroz con pollo preparado al estilo amazónico, con verduras frescas y el toque especial de la selva que nos caracteriza.',
                'precio': 14.00,
                'destacado': True
            },
            {
                'nombre': 'Pollo a la Brasa',
                'descripcion': 'Jugoso pollo a la brasa con sabor amazónico, acompañado de papas fritas y ensalada criolla.',
                'precio': 16.00,
                'destacado': False
            },
            {
                'nombre': 'Tallarín Saltado',
                'descripcion': 'Tallarines saltados con pollo, verduras frescas y la sazón única de nuestra cocinera.',
                'precio': 13.00,
                'destacado': False
            }
        ]

        for producto_data in productos_principales:
            Producto.objects.get_or_create(
                nombre=producto_data['nombre'],
                categoria=categoria_principales,
                defaults={
                    'descripcion': producto_data['descripcion'],
                    'precio': producto_data['precio'],
                    'destacado': producto_data['destacado']
                }
            )

        # Crear bebidas
        bebidas = [
            {
                'nombre': 'Refresco de Cocona',
                'descripcion': 'Bebida natural de cocona, fruta amazónica rica en vitaminas. Perfecta para combatir el calor de la selva.',
                'precio': 5.00,
                'destacado': True
            },
            {
                'nombre': 'Chicha de Jora',
                'descripcion': 'Bebida tradicional fermentada de maíz, preparada siguiendo la receta ancestral de la región amazónica.',
                'precio': 6.00,
                'destacado': True
            },
            {
                'nombre': 'Chicha Morada',
                'descripcion': 'Refrescante chicha morada preparada con maíz morado, especias y frutas. Dulce, nutritiva y llena de antioxidantes.',
                'precio': 5.50,
                'destacado': True
            },
            {
                'nombre': 'Jugo de Camu Camu',
                'descripcion': 'Jugo natural de camu camu, fruta amazónica con alto contenido de vitamina C.',
                'precio': 7.00,
                'destacado': False
            },
            {
                'nombre': 'Refresco de Aguaje',
                'descripcion': 'Bebida natural preparada con aguaje, fruta típica de la Amazonía peruana.',
                'precio': 6.50,
                'destacado': False
            }
        ]

        for bebida_data in bebidas:
            Producto.objects.get_or_create(
                nombre=bebida_data['nombre'],
                categoria=categoria_bebidas,
                defaults={
                    'descripcion': bebida_data['descripcion'],
                    'precio': bebida_data['precio'],
                    'destacado': bebida_data['destacado']
                }
            )

        # Crear postres/heladitas
        postres = [
            {
                'nombre': 'Heladitas de Cocona',
                'descripcion': 'Refrescantes heladitas preparadas con cocona natural, ideales para el calor amazónico.',
                'precio': 3.00,
                'destacado': True
            },
            {
                'nombre': 'Heladitas de Aguaje',
                'descripcion': 'Deliciosas heladitas de aguaje, con el sabor único de esta fruta amazónica.',
                'precio': 3.50,
                'destacado': False
            },
            {
                'nombre': 'Heladitas de Camu Camu',
                'descripcion': 'Heladitas nutritivas preparadas con camu camu, rica en vitamina C.',
                'precio': 4.00,
                'destacado': False
            },
            {
                'nombre': 'Heladitas Mixtas',
                'descripcion': 'Variedad de heladitas con sabores tropicales amazónicos para refrescarte.',
                'precio': 3.00,
                'destacado': False
            }
        ]

        for postre_data in postres:
            Producto.objects.get_or_create(
                nombre=postre_data['nombre'],
                categoria=categoria_postres,
                defaults={
                    'descripcion': postre_data['descripcion'],
                    'precio': postre_data['precio'],
                    'destacado': postre_data['destacado']
                }
            )

        # Crear información del restaurante
        info_data = {
            'nombre_restaurante': 'Salchipollos Yarli',
            'direccion': '''Centro Poblado Tupad Amaru I
Distrito de Imaza, Provincia de Bagua
Departamento de Amazonas
Al lado de la loza deportiva''',
            'telefono': '943823942',  # Agregar número si está disponible
            'horario': '''Abierto todos los días
Perfecto para disfrutar con amigos
Ideal para combatir el calor de la selva''',
            'sobre_nosotros': '''Salchipollos Yarli es un acogedor restaurante ubicado en el corazón del Centro Poblado Tupad Amaru I, en el distrito de Imaza, provincia de Bagua, departamento de Amazonas.

Nos distinguimos por la rica sazón de nuestra cocinera, reconocida en toda la comunidad por su experiencia y dedicación en la preparación de platos tradicionales amazónicos.

Nuestro ambiente es cálido y amigable, como nuestra gente amazónica. Somos el lugar perfecto para disfrutar con amigos, ofreciendo deliciosos platos como salchipollos, aguadito, arroz con pollo, y refrescantes bebidas como cocona, chicha de jora, chicha morada y heladitas ideales para el calor de la selva.

Ubicados al lado de la loza deportiva del centro poblado, somos fácilmente reconocibles y recomendados por toda la comunidad local.

¡Te esperamos para vivir una auténtica experiencia gastronómica amazónica!'''
        }

        Informacion.objects.get_or_create(
            defaults=info_data
        )

        self.stdout.write(
            self.style.SUCCESS('Datos iniciales cargados exitosamente para Salchipollos Yarli')
        )

