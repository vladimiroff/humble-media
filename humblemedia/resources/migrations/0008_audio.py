# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_attachment_mime_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('attachment', models.ForeignKey(to_field='id', to='resources.Attachment')),
                ('file_name', models.CharField(max_length=256)),
                ('mp3', models.FileField(upload_to='snippets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
