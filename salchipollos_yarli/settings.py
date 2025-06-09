# salchipollos_yarli/settings.py
import os
from pathlib import Path
import dj_database_url # ¡Importar dj_database_url!

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Usa una variable de entorno para SECRET_KEY en producción
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-clave-secreta-aqui') # Usará la env var en Render, sino tu clave local

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG debe ser False en producción. Usa una variable de entorno.
DEBUG = os.environ.get('DEBUG_VALUE', 'False') == 'True' 

# ALLOWED_HOSTS para Render.com
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant', # Tu app 'restaurant' ya está aquí
    # Agrega Whitenoise a INSTALLED_APPS si no lo has hecho. Es una buena práctica, aunque el middleware es lo principal.
    # 'whitenoise.runserver_nostatic', # Descomenta si tienes problemas con static files en desarrollo con runserver
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- Agrega esto DESPUÉS de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salchipollos_yarli.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Ruta correcta para templates globales
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'salchipollos_yarli.wsgi.application'

# Database
# Usa dj_database_url para configurar la base de datos de Render
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3', # Valor por defecto para desarrollo local
        conn_max_age=600 # Opcional: Reconexión de base de datos para evitar timeouts
    )
}

# Configuración de validación de contraseñas (sin cambios)
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directorio donde Django recolecta los estáticos en producción
STATICFILES_DIRS = [ # Directorios donde Django buscará tus archivos estáticos en desarrollo
    BASE_DIR / 'static',
]

# Whitenoise configuration for serving static files in production
# Esto es esencial para que Render sirva tus archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 

# Configuración para archivos de medios (imágenes subidas por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'