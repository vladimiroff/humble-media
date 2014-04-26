from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime


class Cause(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    creator = models.ForeignKey('auth.User', related_name='causes')

    created_at = models.DateTimeField(auto_created=True, default=datetime.now)
    modified_at = models.DateTimeField(auto_created=True, auto_now=True, default=datetime.now)

    organization = models.ForeignKey('organizations.Organization', related_name='causes', null=True, blank=True)
    target = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_deleted= models.PositiveIntegerField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cause_details', kwargs={'pk': self.pk})