from django import forms


class ResourceForm(forms.ModelForm):
    class Meta:
        fields = (
            'title',
            'description',
            'min_price',
            'is_published',
        )
