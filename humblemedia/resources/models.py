from django.db import models
from taggit.managers import TaggableManager

class Resource(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey('auth.User', related_name='resources')
    file = models.FileField(upload_to='resource_files/')
    min_price = models.PositiveIntegerField(default=1, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    is_verified = models.BooleanField(default=True, blank=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title
