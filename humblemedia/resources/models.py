from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from payments.models import Payment


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.file

    def document_(self):
        return format(str(self.file).split('/')[-1])


class License(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey('auth.User', related_name='resources')
    min_price = models.PositiveIntegerField(default=1, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    is_verified = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    causes = models.ManyToManyField('causes.Cause', related_name='resources')
    license = models.ForeignKey('License', related_name='resources', null=True, blank=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resources:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super().save(*args, **kwargs)

    def is_bought_by(user):
        return Payment.objects.filter(resource=resource, user=user).exists()


class Preview(models.Model):
    attachment = models.ForeignKey(Attachment, related_name="preview")
    preview_file = models.FileField(upload_to="previews")
    preview_type = models.CharField(max_length=32)
