import subprocess
from .common import get_media_duration

def get_video_capture(filename, at_second, output_file):
    command = 'ffmpeg -ss %s -i %s -vframes 1 %s' % (at_second, filename, output_file)
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

def get_preview_tile(input_path, output_path):
    cmd = 'ffmpeg -i {input} -frames 10 -vf "select=not(mod(n\,105)),scale=320:240,tile=3x6" {output}'.format(
        input_path, output_path
    )
    res = subprocess.check_output(cmd, shell=True)
    return res.decode()

def get_random_video_captures(filename, count, output_files):
    INITIAL_CAPTURE_SECOND = 5
    duration = get_media_duration(filename)
    capture_window = (duration - INITIAL_CAPTURE_SECOND) / count
    capture_tuples = zip(range(INITIAL_CAPTURE_SECOND, duration, int(capture_window)), output_files)
    for (at_second, output_file) in capture_tuples:
        get_video_capture(filename, at_second, output_file)
