from django import forms

from .models import Organization


class OrganizationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(OrganizationForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(OrganizationForm, self).save(commit=False)
        instance.save(*args, **kwargs)
        instance.admins.add(self.user)
        self.save_m2m()
        return instance

    class Meta:
        model = Organization
        fields = ('title',
                  'logo',
                  'description',
                  'url',
                  'admins')
