from django.db import models
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Attachment(models.Model):
    file_name = models.FileField(upload_to='attachments')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return unicode(self.file_name)

    def document_(self):
        return format(str(self.file_name).split('/')[-1])


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
