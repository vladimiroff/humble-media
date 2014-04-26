# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='token',
            field=models.CharField(max_length=32, default='viki'),
            preserve_default=False,
        ),
    ]
