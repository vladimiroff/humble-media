from django.db.models import Manager
from django.contrib.contenttypes.models import ContentType

from .models import Attachment

class ResourceManager(Manager):
    def __init__(self, resource_type):
        super().__init__(self)
        self.resource_type = resource_type

    def get_queryset(self):
        ct = ContentType.objects.get_for_model(self.model)
        resource_ids = Attachment.objects.filter(
            content_type=ct, previews__preview_type='resource_type'
        ).values_list('objects_id', flat=True).distinct()
        return super().get_queryset().filter(id__in=resource_ids)
