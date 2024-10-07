from django.contrib import admin

from api_performance.model_admins import APIRequestLogAdmin
from api_performance.models import APIRequestLog

admin.site.register(APIRequestLog, APIRequestLogAdmin)

