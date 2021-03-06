import sys

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'humble',
        'USER': 'postgres',
        'PASSWORD': 'humble',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STRIPE_API_SECRET_KEY = "sk_test_EW7riigFBCIUUQqrcik80c8Z"
STRIPE_API_PUBLIC_KEY = "pk_test_SJpgMyQ1sjwHVwGtjbqwaW20"

if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'SUPPORTS_TRANSACTIONS': True,
        },
    }
