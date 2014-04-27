from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

from resources.models import Attachment


class Cause(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    creator = models.ForeignKey('auth.User', related_name='causes')

    organization = models.ForeignKey('organizations.Organization', related_name='causes', null=True, blank=True)
    target = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    is_verified = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)

    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    modified_at = models.DateTimeField(auto_created=True, auto_now=True, default=timezone.now)

    tags = TaggableManager()

    class Meta:
        ordering = ['-modified_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('causes:details', kwargs={'pk': self.pk})

    def get_attachments(self):
        ct = ContentType.objects.get_for_model(self)
        return Attachment.objects.filter(object_id=self.id, content_type=ct)
