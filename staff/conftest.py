import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from staff.models import StaffMember, StaffCode


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def valid_unique_code():
    return StaffCode.generate_code()


@pytest.fixture
def invalid_unique_code():
    return 'invalid_code'


@pytest.fixture
def staff_code(valid_unique_code):
    return StaffCode.objects.create(code=valid_unique_code)


@pytest.fixture
def staff_member():
    return StaffMember.objects.create(
        surname='Smith',
        other_names='Jane',
        date_of_birth='1985-05-05',
        id_photo='path/to/photo.jpg',
        employee_number='test-employee-number'
    )


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def authenticated_client(api_client, user):
    login_url = reverse('login')
    response = api_client.post(login_url, {
        'username': 'testuser',
        'password': 'testpass'
    }, format='json')
    
    token = response.data['access_token']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client