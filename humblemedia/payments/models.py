from django.db import models

class Payment(models.Model):
    user = models.ForeignKey('auth.User', related_name='payments')
    resource = models.ForeignKey('resources.Resource', related_name='payments')
    amount = models.PositiveIntegerField()
    cause = models.ForeignKey('causes.Cause', related_name='payments')

    def __str__(self):
        return '{} bought {} for {} BGN and gave them to {}'.format(
            self.user.full_name(),
            self.resource.title,
            self.amount,
            self.cause.title)
