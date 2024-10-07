from rest_framework import serializers
from .models import StaffMember


class StaffMemberSerializer(serializers.ModelSerializer):
    employee_number = serializers.CharField(read_only=True)
    class Meta:
        model = StaffMember
        fields = ['id', 'surname', 'other_names', 'date_of_birth', 'id_photo', 'employee_number']
