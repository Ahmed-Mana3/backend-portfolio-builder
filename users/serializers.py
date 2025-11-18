from rest_framework import serializers
from django.contrib.auth import get_user_model

user_model = get_user_model()

class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model

        fields = ["id", "username", "email", "first_name", "last_name", "phone", "image", "password"]

        extra_kwargs = {
            "password" : {"write_only":True}
        }
    
    def create(self, validated_data):
        new_user = user_model.objects.create_user(**validated_data)
        return new_user


