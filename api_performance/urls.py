from django.urls import path
from api_performance.views import dashboard_callback  # Assuming this is your custom view

urlpatterns = [
    path('admin/dashboard/', dashboard_callback, name='dashboard_callback'),  # Custom dashboard URL
]