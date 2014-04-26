# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_remove_resource_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='modified_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
