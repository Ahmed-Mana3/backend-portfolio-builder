from django.db import models

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


