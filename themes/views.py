from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ThemeSerialzer, SelectUserProfileThemeSerializer, MyThemeSerializer, UpdateUserProfileThemeSerializer
from .models import Theme, UserProfile
from django.contrib.auth import get_user_model

user_model = get_user_model()


class ThemeViewSet(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerialzer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def select_user_profile_theme(request, pk):
    try:
        selected_theme = Theme.objects.get(pk=pk)
        user = request.user.id
        data = {"user": user, "selected_theme":selected_theme.id}
        serializer = SelectUserProfileThemeSerializer(data=data)
        if serializer.is_valid():
            selected_theme.usage_count += 1
            selected_theme.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Theme.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_my_theme(request, pk):
    user = request.user.id
    user_theme = UserProfile.objects.get(user=user)
    new_theme = Theme.objects.get(pk=pk)
    data = {'selected_theme' : new_theme.id}
    serializer = UpdateUserProfileThemeSerializer(user_theme, data=data)
    if serializer.is_valid():
        new_theme.usage_count += 1
        new_theme.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def see_my_theme(request):
    try:
        profile = UserProfile.objects.get(user=request.user)

        if profile.selected_theme is None:
            return Response({"message": "No theme selected"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ThemeSerialzer(profile.selected_theme)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except UserProfile.DoesNotExist:
        return Response({"message": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_my_theme(request):
    user = request.user.id
    try:
        user_profile = UserProfile.objects.get(user=user) 
        user_profile.delete()
        return Response({"message":"Theme deleted successfuly"}, status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response({"message":"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


