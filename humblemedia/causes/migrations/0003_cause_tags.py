# encoding: utf8
from django.db import models, migrations
import taggit.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0002_cause_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', through=taggit.models.TaggedItem, to=taggit.models.Tag),
            preserve_default=True,
        ),
    ]
