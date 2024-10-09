from django.template.response import TemplateResponse
from django.urls import path
from unfold.admin import ModelAdmin


class APIRequestLogAdmin(ModelAdmin):
    list_display = ['endpoint', 'method', 'status_code', 'timestamp', 'success']
    list_filter = ['success', 'method', 'status_code']
    search_fields = ['endpoint', 'method']
    readonly_fields = ['endpoint', 'method', 'status_code', 'timestamp', 'success']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path("summary_view/", self.admin_site.admin_view(self.summary_view), name="summary_view")]
        return my_urls + urls

    def summary_view(self, request):
        # Fetch summary data from the model (assuming your model is called `APIRequestLog`)
        total_requests = self.model.objects.count()
        successful_requests = self.model.objects.filter(success=True).count()
        failed_requests = self.model.objects.filter(success=False).count()

        context = dict(
            self.admin_site.each_context(request),
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )
        return TemplateResponse(request, "admin/summary_view.html", context)

        # Add a custom button in the admin sidebar to access the summary view
