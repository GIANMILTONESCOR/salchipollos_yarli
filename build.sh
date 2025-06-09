#!/usr/bin/env bash
# exit on error
set -o errexit

# NOTA: Render ya instala los paquetes de requirements.txt automáticamente.
# No es necesario ejecutar 'pip install -r requirements.txt' aquí a menos que tengas requisitos especiales.

# Ejecutar migraciones de Django
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Recopilar archivos estáticos (CSS, JS, imágenes de tus apps y staticfiles_dirs)
python manage.py collectstatic --noinput

# Cargar datos iniciales (¡MUY IMPORTANTE!)
# Este comando 'load_initial_data' solo DEBE ejecutarse UNA VEZ en el primer despliegue.
# Después del primer despliegue exitoso, COMENTA O ELIMINA LA SIGUIENTE LÍNEA para evitar duplicados o errores.
python manage.py load_initial_data --noinput || true

# Si tienes un superusuario que necesitas crear automáticamente una sola vez, puedes usar:
# python manage.py createsuperuser --noinput || true