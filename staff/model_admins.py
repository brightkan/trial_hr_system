from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


class UserAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'last_login')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_active', 'last_login')
    search_fields = ('username', 'email')
    list_per_page = 25

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

class StaffMemberAdmin(ModelAdmin):
    list_display = ('id', 'surname', 'other_names', 'date_of_birth', 'employee_number', 'created_at', 'updated_at')
    list_display_links = ('id', 'surname')
    list_filter = ('date_of_birth', 'created_at', 'updated_at')
    search_fields = ('surname', 'other_names', 'employee_number')
    list_per_page = 25
class StaffCodeAdmin(ModelAdmin):
    list_display = ('id', 'code', 'is_used', 'staff_member')
    list_display_links = ('id', 'code')
    list_filter = ('is_used',)
    search_fields = ('code',)
    list_per_page = 25
