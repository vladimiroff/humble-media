# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20140426_1443'),
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='content_type',
            field=models.ForeignKey(default=0, to_field='id', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='resource',
        ),
    ]
