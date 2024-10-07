import urllib.parse
from django.contrib.auth import get_user_model, authenticate, login as django_session_login
from django.utils import timezone
from rest_framework import exceptions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import jwt
from custom_auth.utils import generate_access_token
from project import settings

# Create your views here.
User = get_user_model()
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user was created using Bakozi OAuth
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # Authenticate user using email and password
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.is_active:
        return Response({'error': 'User account is disabled'}, status=status.HTTP_401_UNAUTHORIZED)

    user.last_login = timezone.now()
    user.save()

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    User = get_user_model()
    refresh_token = request.data.get("refreshToken")
    if request.user.is_authenticated:
        access_token = generate_access_token(request.user)
        return Response({'access_token': access_token})

    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')
    except jwt.InvalidSignatureError:
        raise exceptions.AuthenticationFailed(
            'Invalid refresh token, please login again.')
    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')

    access_token = generate_access_token(user)
    return Response({'access_token': access_token})
