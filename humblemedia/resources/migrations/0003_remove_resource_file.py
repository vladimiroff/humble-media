# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20140426_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='file',
        ),
    ]
