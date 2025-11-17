from django.db import models
from django.conf import settings
from themes.models import Theme

user_model = settings.AUTH_USER_MODEL

class Portfolio(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/%y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    bg_color = models.CharField(max_length=7, default="#FF7700")
    text_color = models.CharField(max_length=7, default="#FFFFFF")
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_year = models.DateField(auto_now=False)
    end_year = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.school


class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.company
    

class SocialLink(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    url = models.URLField()
    bg_color = models.CharField(max_length=7, default="#FF7700")
    text_color = models.CharField(max_length=7, default="#FFFFFF")

    def __str__(self):
        return self.platform


