from rest_framework import serializers
from .models import Theme, UserProfile

class ThemeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
    

class SelectUserProfileThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UpdateUserProfileThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["selected_theme"]


class MyThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

