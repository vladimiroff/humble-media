import base64
import magic
import os
import logging
from abc import ABCMeta

from .utils import audio_clip, video_capture
from . import models
import uuid


LOG = logging.getLogger(__name__)

class BaseProcessor(metaclass=ABCMeta):
    mime_types = tuple()
    extensions = tuple()

    def __init__(self, attachment):
        self.attachment = attachment

    def process(self):
        rec = models.Preview()
        rec.attachment = self.attachment
        rec.preview_file = "{}.{}".format(str(uuid.uuid4()).replace("-",""), self.get_target_extension())


        input_path = self.attachment.file.path
        output_path = rec.preview_file.path

        self.process_file(input_path, output_path)
        rec.save()
        return rec

    def get_target_extension(self):
        raise NotImplementedError("Please specify target extension")

    def process_file(self, input_path, output_path):
        raise NotImplementedError("Please specify input and output paths")


    @classmethod
    def start_processing(cls, att):
        try:
            import uwsgi
            uwsgi.spool({b"processor":cls.__name__.encode(), b"id":str(att.id).encode()})
        except Exception as exc:
            print ("Please run via uWSGI to execute the background tasks: {}".format(exc))


class AudioProcessor(BaseProcessor):
    mime_types = ('audio/mpeg', 'audio/x-mpeg', 'audio/mp3',
                  'audio/x-mp3', 'audio/mpeg3', 'audio/x-mpeg3',
                  'audio/mpg', 'audio/x-mpg', 'audio/x-mpegaudio',
                  'audio/x-wav',
    )
    extensions = ('.mp3', )

    def get_target_extension(self):
        return "mp3"

    def process_file(self, input_path, output_path):
        return audio_clip.process_mp3(input_path, output_path)



class VideoProcessor(BaseProcessor):
    """
    """
    mime_types = ['video/avi',
                  'video/example',
                  'video/mpeg',
                  'video/mp4',
                  'video/ogg',
                  'video/quicktime',
                  'video/webm',
                  'video/x-matroska',
                  'video/x-ms-wmv',
                  'video/x-flv']

    def get_target_extension(self):
        return "png"

    def process_file(self, input_path, output_path):
        return video_capture.get_preview_tile(input_path, output_path)




class DocumentProcessor(BaseProcessor):
    """
    """
    mime_types = ['application/pdf', 'text/plain']


class MediaManager():
    PROCESSING_MODULES = (AudioProcessor, VideoProcessor, DocumentProcessor)

    def __init__(self, attachment):
        self.attachment = attachment

    def get_mime_type(self, file):
        return magic.from_file(file, mime=True)

    def process(self):
        att = self.attachment
        mime = self.get_mime_type(att.file.path).decode()
        for mod in self.PROCESSING_MODULES:
            if mime in mod.mime_types or any(map(att.file.name.endswith, mod.extensions)):
                mod.start_processing(att)
                return True
        return False


