from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rx4y(xxq+d%h8771ikgap_t^#-&ct$9n*^m76=pb)ucq9@=p#0'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
]

try:
    from .local import *
except ImportError:
    pass
