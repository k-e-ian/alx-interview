#!/usr/bin/python3
"""
Log parsing
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print the statistics
    """
    print("File size: {}".format(total_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] > 0:
            print("{}: {}".format(k, status_codes[k]))


if __name__ == '__main__':
    count = 0
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            try:
                tokens = line.split()
                if len(tokens) >= 2:
                    file_size = int(tokens[-1])
                    status_code = int(tokens[-2])
                    if status_code in status_codes:
                        total_size += file_size
                        status_codes[status_code] += 1
                        count += 1
                else:
                    raise ValueError("Invalid format")
            except ValueError as e:
                print("Error: {}".format(e))
                continue

            if count % 10 == 0:
                print_stats(total_size, status_codes)

        if count > 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
