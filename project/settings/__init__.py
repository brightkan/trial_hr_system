from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

if not DEBUG:
    from project.settings.production import *
else:
    from project.settings.development import *