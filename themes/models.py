from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL

class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    demo_url = models.URLField(max_length=200)
    preview_image = models.ImageField(upload_to="themes/%y/%m/%d", height_field=None, width_field=None, max_length=None)
    is_active = models.BooleanField(default=True)
    usage_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-usage_count', 'name']

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    selected_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL,null=True, blank=True, related_name="users_selected")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


