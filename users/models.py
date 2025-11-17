from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='users/%y/%m/%d', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.username


