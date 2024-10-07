from django.urls import path
from rest_framework import permissions

from staff import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from staff.views import generate_staff_code

schema_view = get_schema_view(
   openapi.Info(
      title="Staff API",
      default_version='v1',
      description="It enables staff registration",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('staff/register/', views.register_staff, name='register_staff'),
    path('staff/retrieve/', views.retrieve_staff, name='retrieve_staff'),
    path('staff/retrieve/<str:employee_number>/', views.retrieve_staff, name='retrieve_staff_number'),
    path('staff/update/<str:employee_number>/', views.update_staff, name='update_staff'),
    path('staff/generate_staff_code/', generate_staff_code, name='generate_staff_code'),
]