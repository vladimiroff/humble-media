from django.db import models
from django.utils import timezone


class Payment(models.Model):
    user = models.ForeignKey('auth.User', related_name='payments')
    resource = models.ForeignKey('resources.Resource', related_name='payments')
    amount = models.PositiveIntegerField()
    cause = models.ForeignKey('causes.Cause', related_name='payments')
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} bought {} for {:.2f} BGN and gave them to {}'.format(
            self.user.get_full_name(),
            self.resource.title,
            self.amount / 100,
            self.cause.title)
