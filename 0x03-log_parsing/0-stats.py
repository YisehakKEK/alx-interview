#!/usr/bin/python3
"""
Log parsing script
Reads lines from stdin and computes metrics.
"""

import sys
import signal
import re

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
counter = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(counter.keys()):
        if counter[code]:
            print("{}: {}".format(code, counter[code]))

try:
    for line in sys.stdin:
        match = re.match(
            r'^\d+\.\d+\.\d+\.\d+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
            line.strip()
        )
        if match:
            code, size = match.groups()
            total_size += int(size)
            if code in counter:
                counter[code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
