from unfold.admin import ModelAdmin
from django.contrib import admin



class APIRequestLogAdmin(ModelAdmin, admin.ModelAdmin):
    list_display = ['endpoint', 'method', 'status_code', 'timestamp', 'success']
    list_filter = ['success', 'method', 'status_code']
    search_fields = ['endpoint', 'method']
    readonly_fields = ['endpoint', 'method', 'status_code', 'timestamp', 'success']


