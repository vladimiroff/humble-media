from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Attachment(models.Model):
    file_name = models.FileField(upload_to='attachments')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.file_name

    def document_(self):
        return format(str(self.file_name).split('/')[-1])



class Resource(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey('auth.User', related_name='resources')
    min_price = models.PositiveIntegerField(default=1, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    is_verified = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resources:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super().save(*args, **kwargs)
