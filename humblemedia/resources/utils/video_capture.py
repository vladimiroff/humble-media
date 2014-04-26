import subprocess
import re

def _get_video_duration(input_file):
    # returns duration in seconds
    command = 'ffmpeg -i %s 2>&1 | grep "Duration"' % input_file
    result = subprocess.Popen(command,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout_lines = result.stdout.readlines()
    duration_line = stdout_lines[0].decode()
    match = re.match(r'\s*Duration:\s*(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)', duration_line)
    if not match:
        raise Exception('Invalid video file')

    groups = match.groupdict()

    hours   = int(groups.get('hours'))
    minutes = int(groups.get('minutes'))
    seconds = int(groups.get('seconds'))

    return hours * 3600 + (minutes * 60) + seconds

def _get_video_capture(input_file, at_second, output_file):
    command = 'ffmpeg -ss %s -i %s -vframes 1 %s' % (at_second, input_file, output_file)
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

def get_random_video_captures(input_file, count, output_files):
    INITIAL_CAPTURE_SECOND = 5
    duration = _get_video_duration(input_file)
    capture_window = (duration - INITIAL_CAPTURE_SECOND) / count
    capture_tuples = zip(range(INITIAL_CAPTURE_SECOND, duration, round(capture_window)), output_files)
    for (at_second, output_file) in capture_tuples:
        _get_video_capture(input_file, at_second, output_file)
