# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
from support.helpers import env, base_path

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "app"),
        "USER": env("POSTGRES_USER", "app"),
        "PASSWORD": env("POSTGRES_PASSWORD", "app"),
        "HOST": env("POSTGRES_HOST", "postgres"),
        "PORT": env("POSTGRES_PORT", "5432"),
    },
    'sqllite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base_path('db.sqlite3')
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'