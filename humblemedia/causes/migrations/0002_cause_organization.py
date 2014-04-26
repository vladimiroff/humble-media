# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='organization',
            field=models.ForeignKey(null=True, blank=True, to='organizations.Organization', to_field='id'),
            preserve_default=True,
        ),
    ]
