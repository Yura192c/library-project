from .base import *


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = []
