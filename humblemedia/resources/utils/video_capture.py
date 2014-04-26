import subprocess
import re

def get_video_duration(filename):
    # returns duration in seconds
    command = 'ffmpeg -i %s 2>&1 | grep "Duration"' % filename
    result = subprocess.Popen(command,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout_lines = result.stdout.readlines()
    duration_line = stdout_lines[0].decode()
    match = re.match(r'\s*Duration:\s*(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)', duration_line)
    if not match:
        raise 'Invalid video file'

    groups = match.groupdict()

    hours   = int(groups.get('hours'))
    minutes = int(groups.get('minutes'))
    seconds = int(groups.get('seconds'))

    return hours * 3600 + (minutes * 60) + seconds

def get_video_capture(filename, at_second, output_file):
    command = 'ffmpeg -ss %s -i %s -vframes 1 %s' % (at_second, filename, output_file)
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

def get_random_video_captures(filename, count, output_files):
    INITIAL_CAPTURE_SECOND = 5
    duration = get_video_duration(filename)
    capture_window = (duration - INITIAL_CAPTURE_SECOND) / count
    capture_tuples = zip(range(INITIAL_CAPTURE_SECOND, duration, int(capture_window)), output_files)
    for (at_second, output_file) in capture_tuples:
        get_video_capture(filename, at_second, output_file)
