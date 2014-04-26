# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20140426_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='mime_type',
            field=models.CharField(null=True, max_length=64),
            preserve_default=True,
        ),
    ]
