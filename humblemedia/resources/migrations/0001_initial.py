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
            name='Resource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('file', models.FileField(upload_to='resources/')),
                ('min_price', models.PositiveIntegerField(default=1, blank=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
