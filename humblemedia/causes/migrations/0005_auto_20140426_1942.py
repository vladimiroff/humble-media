# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0004_auto_20140426_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='modified_at',
            field=models.DateTimeField(auto_created=True, auto_now=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cause',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
    ]
