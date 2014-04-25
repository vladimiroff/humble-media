# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '__first__'),
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('target', models.PositiveIntegerField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
