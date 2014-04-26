from django import forms

from .models import Cause


class CauseForm(forms.ModelForm):

    class Meta:
        model = Cause
        fields = ('title',
                  'description',
                  'organization',
                  'target',
                  'url',
                  'tags',
        )
