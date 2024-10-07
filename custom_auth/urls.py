from django.urls import path

from custom_auth.views import login, refresh_token_view

urlpatterns = [
    path('api/v1/login', login, name="login"),
    path('api/v1/refresh_token', refresh_token_view, name="refresh_token"),
]


