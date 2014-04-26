import uwsgi
import django

django.setup()

from resources.processing import BaseProcessor
from resources.models import Attachment


def content_processing(env):
    resource_id = env.get("id")
    processor_name = env.get("processor")
    att = Attachment.objects.get(id=resource_id)

    for cls in BaseProcessor.__subclasses__():
        if cls.__name__ == processor_name:
            cls(att)
            cls.process()
            break

    return uwsgi.SPOOL_OK


uwsgi.spooler = content_processing