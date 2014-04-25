from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    logo = models.ImageField()
    url = models.URLField()
    followers = models.ManyToManyField('auth.User', related_name='following')
    admins = models.ManyToManyField('auth.User', related_name='administrate')

    def __str__(self):
        return self.title
