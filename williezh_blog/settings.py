import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}
if 1:
    from .local_settings import email_conf,DATABASES as local_db
    import pymysql
    pymysql.install_as_MySQLdb()
    DATABASES.update(local_db)
    #  ---------------------------------------------------------
    #  Email ,ref:http://www.cnblogs.com/BeginMan/p/3443158.html
    EMAIL_BACKEND = email_conf["EMAIL_BACKEND"]

    EMAIL_USE_TLS = email_conf["EMAIL_USE_TLS"]
    EMAIL_HOST = email_conf["EMAIL_HOST"]
    EMAIL_PORT = email_conf["EMAIL_PORT"]
    EMAIL_HOST_USER = email_conf["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = email_conf["EMAIL_HOST_PASSWORD"]
    DEFAULT_FROM_EMAIL = email_conf["DEFAULT_FROM_EMAIL"]
    #  ---------------------------------------------------------


ALLOWED_HOSTS = [
    "localhost",'127.0.0.1',
    'williezh.pythonanywhere.com',
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Asia/Shanghai"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "zh-hans"
gettext = lambda s: s  # noqa
LANGUAGES = (
    ('en', gettext('English')),
    ('zh-hans', gettext('Simplified Chinese')),
)

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "tszul*&kuxv_(tut)2mb$6pbsyli+uer6jx$_9-kszmz8cepdp"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": False,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                'zinnia.context_processors.version',                
            ],
            'loaders': [
               'app_namespace.Loader',
               'django.template.loaders.filesystem.Loader',
               'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "williezh_blog.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "williezh_blog.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",
    
    #zinnia
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django_comments',
    'mptt',
    'tagging',  
    'zinnia_bootstrap', 
    'zinnia',    

    # external
    "account",
    "pinax.eventlog",
    "pinax.webanalytics",
    "social_django",

    # project
    "williezh_blog",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True

AUTHENTICATION_BACKENDS = [
    "social_core.backends.twitter.TwitterOAuth",
    "account.auth_backends.UsernameAuthenticationBackend",
]

SOCIAL_AUTH_TWITTER_KEY = ""
SOCIAL_AUTH_TWITTER_SECRET = ""

ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_MARKDOWN_EXTENSIONS = ['markdown.extensions.extra', 
                              'markdown.extensions.codehilite',
                            ]
