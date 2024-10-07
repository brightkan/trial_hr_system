from django.db import models
import uuid


class StaffMember(models.Model):
    surname = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    id_photo = models.TextField(blank=True, null=True)
    employee_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return f"{self.id} {self.surname} {self.other_names}"


class StaffCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    staff_member = models.OneToOneField('StaffMember', on_delete=models.CASCADE, null=True, blank=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    @classmethod
    def generate_code(cls):
        return str(uuid.uuid4()).replace('-', '')[:10]

    def __str__(self):
        return self.code
