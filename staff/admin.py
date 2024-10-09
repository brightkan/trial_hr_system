from django.contrib import admin
from django.contrib.auth import get_user_model

from .model_admins import StaffMemberAdmin, StaffCodeAdmin, UserAdmin
# Register your models here.

from .models import StaffMember, StaffCode

User = get_user_model()
admin.site.register(StaffMember, StaffMemberAdmin)
admin.site.register(StaffCode, StaffCodeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.site_header = "Staff"
admin.site.site_title = "Staff Portal"
admin.site.index_title = "Welcome to the Staff Admin Portal"
