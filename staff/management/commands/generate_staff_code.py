# staff/management/commands/generate_staff_codes.py

from django.core.management.base import BaseCommand
from staff.models import StaffCode


class Command(BaseCommand):
    help = 'Generate unique 10-digit codes for staff member'

    def handle(self, *args, **kwargs):
        code = StaffCode.generate_code()
        staff_code = StaffCode(code=code)
        staff_code.save()
        self.stdout.write(self.style.SUCCESS(f'Generated code: {code}'))
