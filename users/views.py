from django.shortcuts import render
from .serializers import UserRegisterationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


@api_view(["POST"])
@permission_classes([AllowAny])
def signup_user(request):
    serializer = UserRegisterationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            return Response( {"detail": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"detail": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)

    except Exception:
        return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    try:
        current_user = request.user
        serializer = UserRegisterationSerializer(current_user)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)