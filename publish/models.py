from django.db import models
from builder.models import Portfolio
from django.utils import timezone

class PublishedSite(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, unique=True, blank=True) 
    is_live = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically generate URL as buildfolio.net/<username>
        if not self.url:
            self.url = f"buildfolio.net/{self.portfolio.user.username}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url

