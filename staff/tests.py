from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User  # Ensure User model is imported
from .models import StaffMember, StaffCode  # Import your models


class StaffMemberAPITests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register_staff')
        self.login_url = reverse('login')
        self.valid_unique_code = StaffCode.generate_code()
        self.invalid_unique_code = 'invalid_code'

        # Create a valid staff code
        self.staff_code = StaffCode.objects.create(code=self.valid_unique_code)

        # Create a staff member to test retrieval and update
        self.staff_member = StaffMember.objects.create(
            surname='Smith',
            other_names='Jane',
            date_of_birth='1985-05-05',
            id_photo='path/to/photo.jpg',
            employee_number='test-employee-number'
        )

        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Get JWT access token by making a request to the login API
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass'
        }, format='json')

        # Ensure the login was successful and we received a token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access_token']  # Assume 'access' is the key in the response

        # Set up authorization headers for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_register_staff_success(self):
        staff_data = {
            'surname': 'Doe',
            'other_names': 'John',
            'date_of_birth': '1990-01-01',
            'id_photo': 'path/to/photo.jpg',  # Ensure this field is correctly formatted
            'unique_code': self.valid_unique_code
        }
        response = self.client.post(self.register_url, staff_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('employee_number', response.data)

        # Verify that the staff code has been marked as used
        self.staff_code.refresh_from_db()
        self.assertTrue(self.staff_code.is_used)
        self.assertEqual(self.staff_code.staff_member,
                         StaffMember.objects.get(employee_number=response.data['employee_number']))

    def test_register_staff_invalid_code(self):
        invalid_data = {
            'surname': 'Doe',
            'other_names': 'John',
            'date_of_birth': '1990-01-01',
            'id_photo': 'path/to/photo.jpg',  # Adjust as necessary
            'unique_code': self.invalid_unique_code  # Use an invalid code for testing
        }
        response = self.client.post(self.register_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Invalid unique code."})

    def test_register_staff_code_already_used(self):
        # Mark the staff code as used
        self.staff_code.is_used = True
        self.staff_code.save()

        staff_data = {
            'surname': 'Doe',
            'other_names': 'John',
            'date_of_birth': '1990-01-01',
            'id_photo': 'path/to/photo.jpg',  # Adjust as necessary
            'unique_code': self.valid_unique_code
        }
        response = self.client.post(self.register_url, staff_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "The unique code has already been used."})

    def test_retrieve_staff_success(self):
        retrieve_url = reverse('retrieve_staff_number', args=[self.staff_member.employee_number])
        response = self.client.get(retrieve_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['surname'], self.staff_member.surname)

    def test_retrieve_staff_not_found(self):
        response = self.client.get(reverse('retrieve_staff_number', args=['non-existent-number']), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Staff member not found."})

    def test_update_staff_success(self):
        update_url = reverse('update_staff', args=[self.staff_member.employee_number])
        update_data = {
            'surname': 'Johnson'
        }
        response = self.client.put(update_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.staff_member.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.staff_member.surname, 'Johnson')

    def test_update_staff_not_found(self):
        response = self.client.put(reverse('update_staff', args=['non-existent-number']), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Staff member not found."})
