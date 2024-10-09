from project.settings.base import *

CORS_ALLOWED_ORIGINS = decouple.config('CORS_ALLOWED_ORIGINS', default="http://127.0.0.1:3000, http://localhost:3000", cast=decouple.Csv())


