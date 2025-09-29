from pathlib import Path
from dotenv import load_dotenv
import os
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(f"{BASE_DIR}/.env")

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

UNFOLD = {
    "SITE_TITLE": "RIML Admin Panel",
    "SITE_HEADER": "RIML - Robust and Interpretable Machine Learning",
    "SITE_SUBHEADER": _("Research Publications & Team Management"),
    "SITE_LOGO": f"{STATIC_URL}riml.svg",
    "SITE_LOGO_WIDTH": "200px",

    "STYLES": [
        lambda request: f"{STATIC_URL}css/admin.css",
    ],

    "COMMAND": {
        "search_models": True,
        "show_history": True,
    },

    "COLORS": {
        "primary": {
            "50": "255, 248, 235",
            "100": "254, 240, 205",
            "200": "252, 225, 158",
            "300": "249, 203, 107",
            "400": "244, 187, 70",
            "500": "244, 187, 70",
            "600": "220, 149, 35",
            "700": "184, 114, 28",
            "800": "147, 91, 22",
            "900": "115, 71, 17",
            "950": "69, 43, 10",
        },
        "base": {
            "50": "249, 250, 251",
            "100": "243, 244, 246",
            "200": "229, 231, 235",
            "300": "209, 213, 219",
            "400": "156, 163, 175",
            "500": "107, 114, 128",
            "600": "75, 85, 99",
            "700": "55, 65, 81",
            "800": "31, 41, 55",
            "900": "17, 24, 39",
            "950": "3, 7, 18",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-base-600)",
            "default-dark": "var(--color-base-300)",
            "important-light": "var(--color-base-900)",
            "important-dark": "var(--color-base-100)",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Authentication & Authorization"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {"title": _("Users"), "icon": "person",
                     "link": reverse_lazy("admin:auth_user_changelist")},
                    {"title": _("Groups"), "icon": "group",
                     "link": reverse_lazy("admin:auth_group_changelist")},
                ],
            },

            {
                "title": _("Team Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {"title": _("Teams"), "icon": "groups",
                     "link": reverse_lazy("admin:core_team_changelist")},
                    {"title": _("Team Members"), "icon": "person_add",
                     "link": reverse_lazy("admin:core_teammember_changelist")},
                ],
            },

            {
                "title": _("Publications"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {"title": _("Publishers"), "icon": "business",
                     "link": reverse_lazy("admin:papers_publisher_changelist")},
                    {"title": _("Publications"), "icon": "article",
                     "link": reverse_lazy("admin:papers_publication_changelist")},
                    {"title": _("Publication Badges"), "icon": "verified",
                     "link": reverse_lazy("admin:papers_publicationbadge_changelist")},
                ],
            },
        ],
    },
}

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(os.environ['DEBUG'] if os.environ['DEBUG'] else True)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'unfold',
    "unfold.contrib.forms",
    "unfold.contrib.filters",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'core',
    'papers',
    'gallery',
    'club'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RIML.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'RIML.wsgi.application'

# Use PostgreSQL in Docker, SQLite for local development
if os.environ.get('POSTGRES_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Spectacular (Swagger) Configuration
SPECTACULAR_SETTINGS = {
    'TITLE': 'RIML API Documentation',
    'DESCRIPTION': 'Robust and Interpretable Machine Learning - API Documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',
    'SERVERS': [
        {
            'url': 'http://localhost:8000',
            'description': 'Development server',
        },
    ],
}

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.environ['AWS_ACCESS_KEY'],
            "secret_key": os.environ['AWS_SECRET_KEY'],
            "bucket_name": os.environ['AWS_STORAGE_BUCKET_NAME'],
            "endpoint_url": "https://s3.ir-tbz-sh1.arvanstorage.ir",
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
