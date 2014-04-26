from django import forms

from .models import Cause


class CauseForm(forms.ModelForm):

    class Meta:
        model = Cause
        fields = ('title',
                  'description',
                  'creator',
                  'organization',
                  'target',
                  'url',
                  'is_published')
