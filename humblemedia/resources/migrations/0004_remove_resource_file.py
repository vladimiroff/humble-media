# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='file',
        ),
    ]
