# restaurant/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from restaurant.models import Categoria, Producto, Informacion, Testimonio

class Command(BaseCommand):
    help = 'Configura datos iniciales para Salchipollos Yarli'

    def handle(self, *args, **options):
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@salchipollosyarli.com',
                password='yarli2025admin'
            )
            self.stdout.write(self.style.SUCCESS('Superusuario creado: admin/yarli2025admin'))

        # Crear categorías
        categoria_principales, created = Categoria.objects.get_or_create(
            nombre="Comidas",
            defaults={'descripcion': 'Deliciosos platos principales de la cocina amazónica'}
        )
        
        categoria_bebidas, created = Categoria.objects.get_or_create(
            nombre="Bebidas Gaseosas",
            defaults={'descripcion': 'Refrescantes bebidas gaseosas'}
        )
        
        categoria_cervezas, created = Categoria.objects.get_or_create(
            nombre="Cervezas",
            defaults={'descripcion': 'Cervezas frías para acompañar'}
        )
        
        categoria_preparadas, created = Categoria.objects.get_or_create(
            nombre="Bebidas Preparadas",
            defaults={'descripcion': 'Bebidas naturales preparadas al momento'}
        )

        # Crear productos - COMIDAS
        comidas = [
            {
                'nombre': 'Salchipollo Plato Grande',
                'descripcion': 'Nuestro plato estrella completo con papas y ensalada',
                'precio': 7.00,
                'categoria': categoria_principales,
                'destacado': True,
                'especial': True
            },
            {
                'nombre': 'Salchipollo Plato Pequeño',
                'descripcion': 'Porción personal, ideal para una persona',
                'precio': 5.00,
                'categoria': categoria_principales,
                'destacado': True
            },
            {
                'nombre': 'Chaufa Especial',
                'descripcion': 'Arroz chaufa con pollo y verduras frescas',
                'precio': 8.00,
                'categoria': categoria_principales,
                'destacado': True
            },
            {
                'nombre': 'Arroz con Pollo',
                'descripcion': 'Tradicional arroz con pollo amazónico',
                'precio': 8.00,
                'categoria': categoria_principales
            },
            {
                'nombre': 'Caldo de Gallina',
                'descripcion': 'Reconfortante caldo casero con gallina criolla',
                'precio': 13.00,
                'categoria': categoria_principales,
                'especial': True
            },
            {
                'nombre': 'Aguadito',
                'descripcion': 'Aguadito de pollo con cilantro fresco',
                'precio': 5.00,
                'categoria': categoria_principales
            },
            {
                'nombre': 'Parrilla Mixta',
                'descripcion': 'Parrilla completa para compartir - Solo por pedido',
                'precio': 20.00,
                'categoria': categoria_principales,
                'especial': True
            },
            {
                'nombre': 'Parrilla de Pollo',
                'descripcion': 'Pollo a la parrilla con guarniciones - Solo por pedido',
                'precio': 15.00,
                'categoria': categoria_principales
            }
        ]

        # Bebidas gaseosas
        bebidas = [
            {'nombre': 'Gaseosa Inka Cola', 'descripcion': 'La bebida del sabor nacional', 'precio': 3.00, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Big Kola', 'descripcion': 'Refrescante sabor a cola', 'precio': 3.00, 'categoria': categoria_bebidas},
            {'nombre': 'Sporade', 'descripcion': 'Bebida energética refrescante', 'precio': 3.00, 'categoria': categoria_bebidas},
            {'nombre': 'Electroligt', 'descripcion': 'Bebida rehidratante', 'precio': 3.00, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Pepsi', 'descripcion': 'Clásica y refrescante', 'precio': 2.50, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Guarana', 'descripcion': 'Sabor único y tropical', 'precio': 2.50, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Fanta', 'descripcion': 'Sabor naranja refrescante', 'precio': 2.50, 'categoria': categoria_bebidas},
            {'nombre': 'Volt', 'descripcion': 'Energía que necesitas', 'precio': 2.50, 'categoria': categoria_bebidas},
            {'nombre': 'Maltin', 'descripcion': 'Bebida nutritiva de malta', 'precio': 2.00, 'categoria': categoria_bebidas},
            {'nombre': 'Cifrut', 'descripcion': 'Refresco de frutas', 'precio': 1.50, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Guaranita', 'descripcion': 'Económica y sabrosa', 'precio': 1.00, 'categoria': categoria_bebidas},
            {'nombre': 'Gaseosa Sensación', 'descripcion': 'Refrescante y económica', 'precio': 1.00, 'categoria': categoria_bebidas},
            {'nombre': 'Agua Mineral', 'descripcion': 'Pura y refrescante', 'precio': 1.00, 'categoria': categoria_bebidas}
        ]

        # Cervezas
        cervezas = [
            {'nombre': 'Cerveza Trigo', 'descripcion': 'Cerveza rubia premium en botella', 'precio': 9.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Negra', 'descripcion': 'Cerveza oscura de sabor intenso', 'precio': 9.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Pilsen', 'descripcion': 'Clásica cerveza peruana', 'precio': 8.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Cristal', 'descripcion': 'Refrescante y ligera', 'precio': 8.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Pilsen Lata', 'descripcion': 'Clásica en presentación lata', 'precio': 6.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Trigo Lata', 'descripcion': 'Rubia premium en lata', 'precio': 6.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Negra Lata', 'descripcion': 'Oscura e intensa en lata', 'precio': 6.00, 'categoria': categoria_cervezas},
            {'nombre': 'Cerveza Cristal Lata', 'descripcion': 'Ligera y refrescante', 'precio': 5.00, 'categoria': categoria_cervezas}
        ]

        # Bebidas preparadas
        preparadas = [
            {'nombre': 'Cocona', 'descripcion': 'Fruta amazónica rica en vitamina C', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Cebada', 'descripcion': 'Bebida nutritiva y refrescante', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Manzana', 'descripcion': 'Jugo natural de manzana', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Chicha Morada', 'descripcion': 'Tradicional bebida antioxidante', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Chicha de Jora', 'descripcion': 'Bebida fermentada tradicional', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Maracuyá', 'descripcion': 'Tropical y refrescante', 'precio': 1.00, 'categoria': categoria_preparadas},
            {'nombre': 'Soya', 'descripcion': 'Nutritiva bebida vegetal', 'precio': 1.00, 'categoria': categoria_preparadas}
        ]

        # Crear todos los productos
        for producto_data in comidas + bebidas + cervezas + preparadas:
            Producto.objects.get_or_create(
                nombre=producto_data['nombre'],
                defaults=producto_data
            )

        # Crear información del restaurante
        info_data = {
            'nombre_restaurante': 'Salchipollos Yarli',
            'slogan': 'El Mejor Sabor de la Amazonía',
            'direccion': '''Centro Poblado Tupad Amaru I
Distrito de Imaza, Provincia de Bagua
Departamento de Amazonas
Al lado de la loza deportiva (coliseo)''',
            'telefono': '+51 943 823 942',
            'horario': 'Abierto todos los días - Horarios flexibles',
            'sobre_nosotros': '''Salchipollos Yarli es más que un restaurante, es el corazón gastronómico del Centro Poblado Tupad Amaru I. 
Ubicados al lado de la loza deportiva (coliseo), nos distinguimos por la rica sazón de nuestra cocinera, reconocida en toda la comunidad.
Ofrecemos un ambiente cálido y familiar, siendo el lugar perfecto para disfrutar con amigos después del partido o en cualquier momento.'''
        }

        Informacion.objects.get_or_create(defaults=info_data)

        # Crear testimonios
        testimonios = [
            {
                'nombre': 'María González',
                'comentario': 'El mejor salchipollo de toda la región. La sazón es increíble y el lugar súper acogedor.',
                'puntuacion': 5
            },
            {
                'nombre': 'Carlos Ruiz',
                'comentario': 'Vengo cada semana con mis amigos. La comida es deliciosa y los precios súper buenos.',
                'puntuacion': 5
            },
            {
                'nombre': 'Ana Torres',
                'comentario': 'La cocinera tiene unas manos mágicas. No hay comparación en toda la zona del coliseo.',
                'puntuacion': 5
            },
            {
                'nombre': 'Luis Mendoza',
                'comentario': 'Después del partido en la loza siempre venimos aquí. El ambiente es familiar y la comida riquísima.',
                'puntuacion': 5
            },
            {
                'nombre': 'Rosa Vásquez',
                'comentario': 'Los precios son súper accesibles y la calidad excelente. Mi familia y yo venimos seguido.',
                'puntuacion': 5
            }
        ]

        for testimonio_data in testimonios:
            Testimonio.objects.get_or_create(
                nombre=testimonio_data['nombre'],
                defaults=testimonio_data
            )

        self.stdout.write(self.style.SUCCESS('¡Datos iniciales cargados exitosamente!'))
        self.stdout.write(self.style.SUCCESS('Productos creados: {}'.format(Producto.objects.count())))
        self.stdout.write(self.style.SUCCESS('Testimonios creados: {}'.format(Testimonio.objects.count())))