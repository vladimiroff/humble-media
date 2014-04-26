# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('attachment', models.ForeignKey(to='resources.Attachment', to_field='id')),
                ('preview_file', models.FileField(upload_to='previews')),
                ('preview_type', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
