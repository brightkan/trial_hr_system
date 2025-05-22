import pytest
from django.urls import reverse
from rest_framework import status
from staff.models import StaffMember, StaffCode


@pytest.mark.django_db
def test_register_staff_success(authenticated_client, valid_unique_code, staff_code):
    register_url = reverse('register_staff')
    staff_data = {
        'surname': 'Doe',
        'other_names': 'John',
        'date_of_birth': '1990-01-01',
        'id_photo': 'path/to/photo.jpg',
        'unique_code': valid_unique_code
    }
    response = authenticated_client.post(register_url, staff_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'employee_number' in response.data

    # Verify that the staff code has been marked as used
    staff_code.refresh_from_db()
    assert staff_code.is_used
    assert staff_code.staff_member == StaffMember.objects.get(employee_number=response.data['employee_number'])


@pytest.mark.django_db
def test_register_staff_invalid_code(authenticated_client, invalid_unique_code):
    register_url = reverse('register_staff')
    invalid_data = {
        'surname': 'Doe',
        'other_names': 'John',
        'date_of_birth': '1990-01-01',
        'id_photo': 'path/to/photo.jpg',
        'unique_code': invalid_unique_code
    }
    response = authenticated_client.post(register_url, invalid_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Invalid unique code."}


@pytest.mark.django_db
def test_register_staff_code_already_used(authenticated_client, valid_unique_code, staff_code):
    register_url = reverse('register_staff')
    # Mark the staff code as used
    staff_code.is_used = True
    staff_code.save()

    staff_data = {
        'surname': 'Doe',
        'other_names': 'John',
        'date_of_birth': '1990-01-01',
        'id_photo': 'path/to/photo.jpg',
        'unique_code': valid_unique_code
    }
    response = authenticated_client.post(register_url, staff_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "The unique code has already been used."}


@pytest.mark.django_db
def test_retrieve_staff_success(authenticated_client, staff_member):
    retrieve_url = reverse('retrieve_staff_number', args=[staff_member.employee_number])
    response = authenticated_client.get(retrieve_url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['surname'] == staff_member.surname


@pytest.mark.django_db
def test_retrieve_staff_not_found(authenticated_client):
    retrieve_url = reverse('retrieve_staff_number', args=['non-existent-number'])
    response = authenticated_client.get(retrieve_url, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"error": "Staff member not found."}


@pytest.mark.django_db
def test_update_staff_success(authenticated_client, staff_member):
    update_url = reverse('update_staff', args=[staff_member.employee_number])
    update_data = {
        'surname': 'Johnson'
    }
    response = authenticated_client.put(update_url, update_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    staff_member.refresh_from_db()
    assert staff_member.surname == 'Johnson'


@pytest.mark.django_db
def test_update_staff_not_found(authenticated_client):
    update_url = reverse('update_staff', args=['non-existent-number'])
    response = authenticated_client.put(update_url, {}, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"error": "Staff member not found."}