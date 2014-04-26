from django import forms
from django.contrib.contenttypes.models import ContentType

from .models import Attachment


class AttachmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model')
        self.id = kwargs.pop('id')
        super(AttachmentForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(AttachmentForm, self).save(commit=False)
        instance.content_type = ContentType.objects.get(model=self.model[:-1])
        instance.object_id = self.id
        instance.save(*args, **kwargs)
        return instance

    class Meta:
        model = Attachment
        fields = (
            'file_name',
        )


class ResourceForm(forms.ModelForm):
    class Meta:
        fields = (
            'title',
            'description',
            'min_price',
            'is_published',
        )
