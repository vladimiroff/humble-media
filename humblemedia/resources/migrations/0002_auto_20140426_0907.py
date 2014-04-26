# encoding: utf8
from django.db import models, migrations
import taggit.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', through=taggit.models.TaggedItem, to=taggit.models.Tag),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(upload_to='resource_files/'),
        ),
    ]
