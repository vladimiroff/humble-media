import subprocess
import re


def get_media_duration(filename):
    # returns duration in seconds
    command = 'ffmpeg -i %s 2>&1|grep Duration' % filename
    result = subprocess.check_output(command, shell=True)
    print (result)
    duration_line = result.decode()
    match = re.match(r'\s*Duration:\s*(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)', duration_line)
    if not match:
        raise Exception('Cannot parse duration from file {}'.format(filename))

    groups = match.groupdict()

    hours   = int(groups.get('hours'))
    minutes = int(groups.get('minutes'))
    seconds = int(groups.get('seconds'))

    return hours * 3600 + (minutes * 60) + seconds