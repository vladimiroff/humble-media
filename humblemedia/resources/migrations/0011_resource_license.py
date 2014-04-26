# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20140426_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='license',
            field=models.ForeignKey(blank=True, to='resources.License', to_field='id', null=True),
            preserve_default=True,
        ),
    ]
