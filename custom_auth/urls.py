from django.urls import path

from custom_auth.views import login, refresh_token_view

urlpatterns = [
    path('login', login, name="login"),
    path('refresh_token', refresh_token_view, name="refresh_token"),
]


