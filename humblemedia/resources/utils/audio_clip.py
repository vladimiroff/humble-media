import subprocess
import logging
from . import common

LOG = logging.getLogger(__name__)

def process_mp3(input_path, output_path):
    try:
        duration = common.get_media_duration(input_path)
        if duration > 20:
            start_time = duration / 2
        else:
            start_time = 0
        command = "ffmpeg " \
                  "-ss {start_time:d} " \
                  "-i {input} " \
                  "-to {end_time:d} " \
                  "-af 'afade=t=in:ss=0:d=1,afade=t=out:ss=11:d=13' " \
                  "{output} -y".format(start_time=int(start_time),
                                       end_time=13,
                                    input=input_path,
                                    output=output_path,
                                    )

        res = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        LOG.exception("Failed to process {}".format(input_path))
        return None
    else:
        return res.decode()