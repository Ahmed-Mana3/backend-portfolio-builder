from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOfPortfolio
from rest_framework import status
from rest_framework.response import Response
from .models import Project, Skill, Education, Experience, SocialLink
from themes.models import UserProfile
from .serializers import ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, SocialLinkSerializer
    
  
# GET, POST --> Projects
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def projects_list(request):

    try:
        portfolio = UserProfile.objects.get(user=request.user)
        
        # GET
        if request.method == "GET":
            projects = Project.objects.filter(portfolio = portfolio)
            seriaizer = ProjectSerializer(projects, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        
        # POST
        elif request.method == "POST":
            seriaizer = ProjectSerializer(data=request.data)
            if seriaizer.is_valid():
                seriaizer.save(portfolio=portfolio)
                return Response(seriaizer.data, status=status.HTTP_201_CREATED)
            return Response(seriaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except UserProfile.DoesNotExist:
        return Response({"error": "select theme first"}, status=status.HTTP_404_NOT_FOUND)
        
    except Project.DoesNotExist:
        return Response({"error": "there are no projects, add one"}, status=status.HTTP_404_NOT_FOUND)


# GET PUT DELETE --> Projects
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOfPortfolio])
def project_pk(request, pk):
    try:
        
        project = Project.objects.get(pk=pk)

        if project.portfolio.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
                )

        # GET
        if request.method == "GET":
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # PUT
        elif request.method == "PUT":
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
        elif request.method == "DELETE":
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



# GET, POST --> Skills
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def skills_list(request):
    try:
        portfolio = UserProfile.objects.get(user=request.user)

        # GET
        if request.method == "GET":
            skills = Skill.objects.filter(portfolio=portfolio)
            seriaizer = SkillSerializer(skills, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        
        # POST
        elif request.method == "POST":
            portfolio = UserProfile.objects.get(user=request.user)
            seriaizer = SkillSerializer(data=request.data)
            if seriaizer.is_valid():
                seriaizer.save(portfolio=portfolio)
                return Response(seriaizer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except Project.DoesNotExist:
        return Response(seriaizer.errors, status=status.HTTP_404_NOT_FOUND)


# GET PUT DELETE --> Skills
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def skill_pk(request, pk):
    try:
        skill = Project.objects.get(pk=pk)

        if skill.portfolio.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
                )


        # GET
        if request.method == "GET":
            serializer = SkillSerializer(skill)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # PUT
        elif request.method == "PUT":
            serializer = SkillSerializer(skill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
        elif request.method == "DELETE":
            skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



# GET, POST --> Education
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def education_list(request):
    try:
        portfolio = UserProfile.objects.get(user=request.user)

        # GET
        if request.method == "GET":
            educations = Education.objects.filter(portfolio=portfolio)
            seriaizer = EducationSerializer(educations, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        
        # POST
        elif request.method == "POST":
            portfolio = UserProfile.objects.get(user=request.user)
            seriaizer = EducationSerializer(data=request.data)
            if seriaizer.is_valid():
                seriaizer.save(portfolio=portfolio)
                return Response(seriaizer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except Project.DoesNotExist:
        return Response(seriaizer.errors, status=status.HTTP_404_NOT_FOUND)


# GET PUT DELETE --> Education
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOfPortfolio])
def education_pk(request, pk):
    try:
        education = Education.objects.get(pk=pk)

        if education.portfolio.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
                )
        # GET
        if request.method == "GET":
            serializer = EducationSerializer(education)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # PUT
        elif request.method == "PUT":
            serializer = EducationSerializer(education, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
        elif request.method == "DELETE":
            education.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




# GET, POST --> Experience
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def experience_list(request):
    try:
        portfolio = UserProfile.objects.get(user=request.user)

        # GET
        if request.method == "GET":
            experiences = Experience.objects.filter(portfolio=portfolio)
            seriaizer = ExperienceSerializer(experiences, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        
        # POST
        elif request.method == "POST":
            portfolio = UserProfile.objects.get(user=request.user)
            seriaizer = ExperienceSerializer(data=request.data)
            if seriaizer.is_valid():
                seriaizer.save(portfolio=portfolio)
                return Response(seriaizer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except Project.DoesNotExist:
        return Response(seriaizer.errors, status=status.HTTP_404_NOT_FOUND)


# GET PUT DELETE --> Experience
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def experience_pk(request, pk):
    try:
        experience = Experience.objects.get(pk=pk)

        if experience.portfolio.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
                )

        # GET
        if request.method == "GET":
            serializer = ExperienceSerializer(experience)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # PUT
        elif request.method == "PUT":
            serializer = ExperienceSerializer(experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
        elif request.method == "DELETE":
            experience.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




# GET, POST --> SocialLink
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def socail_links_list(request):
    try:
        portfolio = UserProfile.objects.get(user=request.user)
        # GET
        if request.method == "GET":
            links = SocialLink.objects.filter(portfolio=portfolio)
            seriaizer = SocialLinkSerializer(links, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        
        # POST
        elif request.method == "POST":
            portfolio = UserProfile.objects.get(user=request.user)
            seriaizer = SocialLinkSerializer(data=request.data)
            if seriaizer.is_valid():
                seriaizer.save(portfolio=portfolio)
                return Response(seriaizer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    except Project.DoesNotExist:
        return Response(seriaizer.errors, status=status.HTTP_404_NOT_FOUND)


# GET PUT DELETE --> SocialLink
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def socail_links_pk(request, pk):
    try:
        link = SocialLink.objects.get(pk=pk)

        if link.portfolio.user != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
                )
        # GET
        if request.method == "GET":
            serializer = SocialLinkSerializer(link)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # PUT
        elif request.method == "PUT":
            serializer = SocialLinkSerializer(link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
        elif request.method == "DELETE":
            link.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




"""
message to my self whenever I'm back here:
remember the path you came from
remember no one believed you will get to anywhere
remember you are still strong and still trying Despite the tone of frustration that you hear
be proud of what you got and remember how you were meant to be.
"""


