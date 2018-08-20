DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fabulous_tracker_psql',
        'USER': 'fabulous',
        'PASSWORD': 'Password is hiden',
        'HOST': 'postgresql-fabulous.alwaysdata.net',
        'PORT': '',
    }                                                                                                                                       
}                                                                                                                                           
                                                                                                                                            
                                                                                                                                            
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }                                                                                                                                       
}
