# api_performance/admin.py

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db.models import Count, Q
from .models import APIRequestLog

class ApiPerformanceAdmin(admin.ModelAdmin):
    change_list_template = "api_performance/dashboard.html"  # Custom template for the dashboard

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('api-performance/', self.admin_site.admin_view(self.dashboard_view), name='api_performance_dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Query the database for the performance statistics
        stats = APIRequestLog.objects.values('endpoint').annotate(
            total_requests=Count('id'),
            successful_requests=Count('id', filter=Q(success=True)),
            failed_requests=Count('id', filter=Q(success=False))
        )

        context = {
            'stats': stats,
            'title': "API Performance Dashboard"
        }
        return render(request, 'api_performance/dashboard.html', context)

# Register the APIRequestLog model
admin.site.register(APIRequestLog)  # This allows normal management of APIRequestLog

# Note: Do not register ApiPerformanceAdmin, just use it for the custom view
