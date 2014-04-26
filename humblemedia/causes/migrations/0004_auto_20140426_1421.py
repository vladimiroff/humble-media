# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0003_cause_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cause',
            name='is_deleted',
            field=models.PositiveIntegerField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cause',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now, auto_created=True, auto_now=True),
            preserve_default=True,
        ),
    ]
