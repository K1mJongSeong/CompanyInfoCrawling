DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'searchcom', 
        'USER': 'search', 
        'PASSWORD': 'rldjqwjdqh', 
        'HOST': '116.124.133.159', 
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    } 
}
SECRET_KEY = 'django-insecure-f6gtxue2eu3s13jnzwwqv-h1hd#+)4=s5ey1!p%@kiet^7mam9'