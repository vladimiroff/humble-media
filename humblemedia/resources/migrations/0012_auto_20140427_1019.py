# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_resource_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preview',
            name='preview_type',
            field=models.CharField(max_length=32, default='unknown', choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('document', 'Document'), ('unknown', 'Unknown')]),
        ),
    ]
