from unfold.admin import ModelAdmin

class APIRequestLogAdmin(ModelAdmin):
    list_display = ['endpoint', 'method', 'status_code', 'timestamp', 'success']
    list_filter = ['success', 'method', 'status_code']
    search_fields = ['endpoint', 'method']
    readonly_fields = ['endpoint', 'method', 'status_code', 'timestamp', 'success']
