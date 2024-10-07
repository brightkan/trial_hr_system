from staff.models import StaffCode


def is_valid_code(code):
    try:
        StaffCode.objects.get(code=code, is_used=False)
        return True
    except StaffCode.DoesNotExist:
        return False
