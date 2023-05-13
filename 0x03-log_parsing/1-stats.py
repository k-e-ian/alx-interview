#!/usr/bin/python3
'''
File: 0-stats.py
'''
import sys


def print_stats(total_size, status_codes):
    '''
    script that reads stdin line by line and computes metrics
    '''
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line_number, line in enumerate(sys.stdin):
            try:
                tokens = line.split()
                file_size = int(tokens[-1])
                status_code = int(tokens[-2])
                if status_code in status_codes:
                    total_size += file_size
                    status_codes[status_code] += 1
                    count += 1
                    if count == 10:
                        print_stats(total_size, status_codes)
                        count = 0
            except (ValueError, IndexError):
                pass
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)
