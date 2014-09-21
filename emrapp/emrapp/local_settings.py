# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'feewhpnaz^mimihd_y#^yyvg5go!u=(=%er-lfjz&3xbk0i%^d'

# debug on in testing/local dev but off in production
DEBUG = True

# use the sqlite3 DB for lightweight development
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'django_db_emrapp',
    }
}

# for development, we will be using the static directory in the repository
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static/'), )
#print (STATICFILES_DIRS)
