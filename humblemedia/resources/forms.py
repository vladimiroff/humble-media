from django import forms
from django.contrib.contenttypes.models import ContentType
import stripe

from .models import Attachment
from causes.models import Cause
from payments.models import Payment


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
            'file',
        )


class ResourceForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        instance = super(ResourceForm, self).save()
        self.save_m2m()
        return instance

    class Meta:
        fields = (
            'title',
            'description',
            'min_price',
            'causes',
            'is_published',
            'license',
        )


class StripeForm(forms.Form):
    stripeToken = forms.CharField(required=True)
    amount = forms.IntegerField(required=True) # in cents
    cause_id = forms.IntegerField(required=True)

    def __init__(self, user, resource, *args, **kwargs):
        self.user = user
        self.resource = resource
        super().__init__(*args, **kwargs)

    def charge(self):
        cleaned_data = self.clean()

        cause = Cause.objects.get(pk=cause_id)
        amount = cleaned_data['amount']

        if amount < self.resource.min_price:
            raise forms.ValidationError('You hacker!')

        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://manage.stripe.com/account
        stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

        # Get the credit card details submitted by the form
        token = cleaned_data['stripeToken']

        payment = Payment(
            user=self.user,
            resource=self.resource,
            amount=amount,
            cause=cause
        )

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            stripe.Charge.create(
                amount=amount, # amount in cents, again
                currency='bgn',
                card=token,
                description=str(payment)
            )
        except stripe.CardError as e:
            # The card has been declined
            raise forms.ValidationError(e)

        payment.save()
