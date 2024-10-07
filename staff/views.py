from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StaffMember
from .serializers import StaffMemberSerializer
import uuid
from .utils import is_valid_code


@api_view(['POST'])
def register_staff(request):
    if request.method == 'POST':
        data = request.data
        if 'unique_code' not in data or not is_valid_code(data['unique_code']):
            return Response({"error": "Invalid unique code."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StaffMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save(employee_number=str(uuid.uuid4())[:10])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_staff(request, employee_number=None):
    if employee_number:
        try:
            staff_member = StaffMember.objects.get(employee_number=employee_number)
            serializer = StaffMemberSerializer(staff_member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StaffMember.DoesNotExist:
            return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
        staff_members = StaffMember.objects.all()
        serializer = StaffMemberSerializer(staff_members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_staff(request, employee_number):
    try:
        staff_member = StaffMember.objects.get(employee_number=employee_number)
    except StaffMember.DoesNotExist:
        return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = StaffMemberSerializer(staff_member, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

