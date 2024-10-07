from django.contrib import admin

# Register your models here.

from .models import StaffMember, StaffCode

admin.site.register(StaffMember)
admin.site.register(StaffCode)

admin.site.site_header = "Staff Management System"  # Custom site header
admin.site.site_title = "Staff Admin Portal"        # Custom site title (shown on the browser tab)
admin.site.index_title = "Welcome to the Staff Admin Portal"