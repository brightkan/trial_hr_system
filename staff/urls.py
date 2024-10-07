from django.urls import path
from staff import views

urlpatterns = [
    path('staff/register/', views.register_staff, name='register_staff'),
    path('staff/retrieve/', views.retrieve_staff, name='retrieve_staff'),
    path('staff/retrieve/<str:employee_number>/', views.retrieve_staff, name='retrieve_staff_number'),
    path('staff/update/<str:employee_number>/', views.update_staff, name='update_staff'),
]