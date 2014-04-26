# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_attachment_mime_type'),
        ('causes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='causes',
            field=models.ManyToManyField(default=None, to='causes.Cause'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='mime_type',
        ),
    ]
