from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class RegistrationAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Both username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username is already taken."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a new user
        user = User.objects.create_user(username=username, password=password)

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
