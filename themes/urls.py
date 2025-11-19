from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ThemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/select/', views.select_user_profile_theme, name='select_user_profile_theme'),
    path('<int:pk>/update_selected_theme/', views.update_my_theme, name='update_my_theme'),
    path('my/', views.see_my_theme, name='see_my_theme'),
]
