#!/usr/bin/env python3
""" log parser
    Accepts a filename on the command line.  The file is a linux-like log file
    from a system you are debugging.  Mixed in among the various statements are
    messages indicating the state of the device.  They look like:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program only
    cares about three: ON, OFF, and ERR.

    Your program will parse the given log file and print out a report giving
    how long the device was ON, and the time stamp of any ERR conditions.
"""

import sys
from datetime import datetime


if __name__ == '__main__':
    log_file = sys.argv[1]

    error_time_stamps = []

    is_running = False
    run_time = 0

    with open(log_file) as f:
        for line in f:
            # Work only with lines which contain 'Device State'
            if 'Device State' in line:
                # Capture timestamp
                time_format = '%b %d %H:%M:%S:%f'
                time_stamp = datetime.strptime(line[:19], time_format)
                if 'ERR' in line:
                    string_stamp = datetime.strftime(time_stamp, time_format)
                    error_time_stamps.append(string_stamp)
                elif not is_running and 'ON' in line:
                    start = time_stamp
                    is_running = True
                elif is_running and 'OFF' in line:
                    end = time_stamp
                    difference = (end - start).seconds
                    run_time += difference
                    start, end = (0, 0)
                    is_running = False

    print(f'The device was running for {run_time} seconds')

    print('Timestamps of error events:')
    for err in error_time_stamps:
        print(err)

    print('There are no unit tests for logparse.')
