from django.db import models
from taggit.managers import TaggableManager


class Cause(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    creator = models.ForeignKey('auth.User', related_name='causes')
    target = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.title
