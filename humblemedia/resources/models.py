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
        return self.file.name

    def document_(self):
        return format(str(self.file).split('/')[-1])


class License(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ResourceManager(models.Manager):
    def __init__(self, resource_type):
        super().__init__()
        self.resource_type = resource_type

    def get_queryset(self):
        ct = ContentType.objects.get_for_model(self.model)
        resource_ids = Attachment.objects.filter(
            content_type=ct, previews__preview_type=self.resource_type
        ).values_list('object_id', flat=True).distinct()
        return super().get_queryset().filter(id__in=resource_ids)


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

    objects = models.Manager()
    audios = ResourceManager('audio')
    videos = ResourceManager('video')
    images = ResourceManager('image')
    documents = ResourceManager('document')
    others = ResourceManager('unknown')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resources:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super().save(*args, **kwargs)

    def is_bought_by(self, user):
        return Payment.objects.filter(resource=self, user=user).exists()

    def get_attachments(self):
        ct = ContentType.objects.get_for_model(self)
        return Attachment.objects.filter(object_id=self.id, content_type=ct)

    def get_previews(self):
        previews = []
        attachments = self.get_attachments()
        for attachment in attachments:
            preview = attachment.previews.first()
            if preview is not None:
                previews.append(preview.preview_file.name)
        return previews


class Preview(models.Model):
    TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        ('unknown', 'Unknown'),
    )
    attachment = models.ForeignKey(Attachment, related_name="previews")
    preview_file = models.FileField(upload_to="previews")
    preview_type = models.CharField(max_length=32, choices=TYPES, default='unknown')
