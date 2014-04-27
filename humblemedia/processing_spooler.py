import uwsgi
import django

django.setup()

from resources.processing import BaseProcessor
from resources.models import Attachment


def content_processing(env):
    print (env)
    resource_id = int(env.get(b"id"))
    processor_name = env.get(b"processor").decode()
    try:
        att = Attachment.objects.get(id=resource_id)
    except Attachment.DoesNotExist:
        return uwsgi.SPOOL_OK

    for cls in BaseProcessor.__subclasses__():
        if cls.__name__ == processor_name:
            instance = cls(att)
            instance.process()
            break

    return uwsgi.SPOOL_OK


uwsgi.spooler = content_processing