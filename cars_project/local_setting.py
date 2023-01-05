# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^z98qpu*=5l-bdf711__lvoz*%87@hu1ecq2w3*uryr)^b*0g!'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}