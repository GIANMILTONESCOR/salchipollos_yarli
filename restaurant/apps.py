from django.apps import AppConfig

class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'
    verbose_name = '🍗 Restaurante Yarli'
    
    def ready(self):
        # Personalizar el admin
        from django.contrib import admin
        admin.site.site_header = "🔥 Salchipollos Yarli - Panel de Control"
        admin.site.site_title = "Yarli Admin"
        admin.site.index_title = "Bienvenido al Panel de Control"