from django.db import models
from django.utils import timezone


class Organization(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    logo = models.ImageField(upload_to='organization_logos', null=True, blank=True)
    url = models.URLField()
    followers = models.ManyToManyField('auth.User', related_name='following')
    admins = models.ManyToManyField('auth.User', related_name='administrate')
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-modified_at']
