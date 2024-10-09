import os

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from project import settings


class ConditionalTemplateView(TemplateView):
    def get_template_names(self):
        # Check if the React build directory exists
        if os.path.exists(os.path.join(settings.BASE_DIR, 'frontend/index.html')):
            return ['index.html']
        return ['default_template.html']  # Fallback template if React is not built


urlpatterns = [
    path('', include('custom_auth.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('staff.urls')),
    re_path(r'^(?!admin|api).*$', ConditionalTemplateView.as_view(), name='index'),
]
