from rest_framework import serializers
from .models import Project, Skill, Education, Experience, SocialLink

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            "portfolio" : {"read_only":True}
        }


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        extra_kwargs = {
            "portfolio" : {"read_only":True}
        }


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        extra_kwargs = {
            "portfolio" : {"read_only":True}
        }


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        extra_kwargs = {
            "portfolio" : {"read_only":True}
        }


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
        extra_kwargs = {
            "portfolio" : {"read_only":True}
        }


