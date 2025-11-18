from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me', views.get_user_data, name='get_user_data'),

]
