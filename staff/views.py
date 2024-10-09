from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import StaffMember, StaffCode
from .serializers import StaffMemberSerializer
import uuid
from .utils import is_valid_code


@api_view(['POST'])
def register_staff(request):
    """
     Register a new staff member.
    """
    if request.method == 'POST':
        data = request.data

        # Check if unique_code is present
        if 'unique_code' not in data:
            return Response({"error": "Unique code is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the unique code and its status
        try:
            staff_code = StaffCode.objects.get(code=data['unique_code'])
            if staff_code.is_used:
                return Response({"error": "The unique code has already been used."}, status=status.HTTP_400_BAD_REQUEST)
        except StaffCode.DoesNotExist:
            return Response({"error": "Invalid unique code."}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with serializer validation
        serializer = StaffMemberSerializer(data=data)
        if serializer.is_valid():
            staff_member = serializer.save(employee_number=str(uuid.uuid4())[:10])

            # Mark the staff code as used and associate it with the new staff member
            staff_code.is_used = True
            staff_code.staff_member = staff_member
            staff_code.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import StaffMember
from .serializers import StaffMemberSerializer


@api_view(['GET'])
def retrieve_staff(request, employee_number=None):
    """
    Retrieve staff member(s) with pagination.
    """
    if employee_number:
        # Retrieve a specific staff member by employee number
        try:
            staff_member = StaffMember.objects.get(employee_number=employee_number)
            serializer = StaffMemberSerializer(staff_member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StaffMember.DoesNotExist:
            return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Retrieve a list of staff members with pagination
        staff_members = StaffMember.objects.all()

        # Instantiate the paginator
        paginator = PageNumberPagination()
        paginator.page_size = 10  # You can adjust the page size as needed

        # Paginate the queryset
        paginated_staff_members = paginator.paginate_queryset(staff_members, request)

        # Serialize the paginated data
        serializer = StaffMemberSerializer(paginated_staff_members, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)


@api_view(['PUT'])
def update_staff(request, employee_number):
    """
        Update a staff member.
    """

    try:
        staff_member = StaffMember.objects.get(employee_number=employee_number)
    except StaffMember.DoesNotExist:
        return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = StaffMemberSerializer(staff_member, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])  # Only superusers can access
def generate_staff_code(request):
    """
      Generate a new staff code.

      This endpoint allows superusers to generate a new staff code.
      The code is a unique 10-digit alphanumeric string.
      Only superusers can access this endpoint.
    """
    new_code = StaffCode.generate_code()

    # Save the new code to the database
    staff_code = StaffCode.objects.create(code=new_code)

    return Response({'code': staff_code.code}, status=status.HTTP_201_CREATED)

