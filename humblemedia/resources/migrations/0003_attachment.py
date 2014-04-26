# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20140426_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.FileField(upload_to='attachments')),
                ('resource', models.ForeignKey(to_field='id', to='resources.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
