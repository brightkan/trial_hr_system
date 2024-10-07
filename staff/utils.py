from staff.models import StaffCode


def is_valid_code(code):
    try:
        # Check if the code exists and is not yet used
        staff_code = StaffCode.objects.get(code=code, is_used=False)
        return True
    except StaffCode.DoesNotExist:
        return False
