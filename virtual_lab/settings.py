from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django, make sure to change this in production
SECRET_KEY = 'your-secret-key'  # Update this for production

# Enable debugging for development
DEBUG = True  # Set to False in production

# Hosts that are allowed to serve the app (for production, this should be updated)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.yourdomain.com']  # Add your production domain here

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lab_simulator',  # Add this if it's a separate app
    # Add other apps here if needed
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration for the root of the project
ROOT_URLCONF = 'virtual_lab.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add path for global templates if any
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

# WSGI application for deployment
WSGI_APPLICATION = 'virtual_lab.wsgi.application'

# Database configuration (SQLite is used here)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings (can be expanded later)
AUTH_PASSWORD_VALIDATORS = [
    # You can add more password validators if needed, for example:
    # 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # 'django.contrib.auth.password_validation.NumericPasswordValidator',
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'  # Correct static URL path

# Directories where static files are stored
STATICFILES_DIRS = [
    BASE_DIR / 'lab_simulator' / 'static',  # Correct path to static folder within your app
    # If you have static files in other apps, add them here, e.g.:
    # BASE_DIR / 'projectile_simulator' / 'static',
]

# Set STATIC_ROOT for collecting static files (for production)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Used when running collectstatic command

# Default field type for auto-generated fields
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
