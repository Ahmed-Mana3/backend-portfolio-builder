from django.urls import path
from . import views

urlpatterns = [
    path('projcets/', views.projects_list, name='projects_list'),
    path('projcets/<int:pk>/', views.project_pk, name='project_pk'),

    path('skills/', views.skills_list, name='skills_list'),
    path('skills/<int:pk>/', views.skill_pk, name='skill_pk'),

    path('education/', views.education_list, name='education_list'),
    path('education/<int:pk>/', views.education_pk, name='education_pk'),

    path('experience/', views.experience_list, name='experience_list'),
    path('experience/<int:pk>/', views.experience_pk, name='experience_pk'),

    path('socail_links/', views.socail_links_list, name='socail_links_list'),
    path('socail_links/<int:pk>/', views.socail_links_pk, name='social_pk'),
]


