from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = []
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ROOT_URLCONF = 'dateentry.urls'
WSGI_APPLICATION = 'dateentry.wsgi.application'


# Application definition

INSTALLED_APPS = [
	'django.contrib.sessions',

	'dateentry.frontend',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
]


TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
			],
		},
	},
]



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

DATE_FORMAT = 'N j, Y'
LANGUAGE_CODE = 'en-us'
TIME_FORMAT = 'g:i A'
TIME_INPUT_FORMATS = [
	"%H:%M:%S",  # '14:30:59'
	"%H:%M:%S.%f",  # '14:30:59.000200'
	"%H:%M",  # '14:30'
	"%I:%M %p",  # '10:30 AM'
]
TIME_ZONE = 'America/New_York'
USE_I18N = False
USE_TZ = True

LANGUAGES = [
	('en', 'English'),
]
