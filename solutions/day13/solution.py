# -*- coding: utf-8 -*-

import os
from collections import namedtuple


def load_firewall(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    scanners = {}
    with open(fpath) as f:
        for line in f:
            depth, scanner_range = map(int, line.replace(' ', '').split(':'))
            scanners[depth] = Scanner(depth, scanner_range)
    return scanners


Scanner = namedtuple('Scanner', ['depth', 'range'])


def period(scanner):
    return 2 * (scanner.range - 1)


def compute_severity(firewall, offset=0):
    severity, times_caught = 0, 0
    for depth, scanner in firewall.iteritems():
        ostensible_depth = depth + offset
        if ostensible_depth % period(scanner) == 0:
            severity += scanner.depth * scanner.range
            times_caught += 1
    return severity, times_caught


def packet_caught(firewall, offset):
    for depth, scanner in firewall.iteritems():
        if (depth + offset) % period(scanner) == 0:
            return True
    return False


def compute_safe_offset(firewall):
    offset = 0
    while packet_caught(firewall, offset):
        offset += 1
    return offset


if __name__ == '__main__':
    firewall = load_firewall()
    print('Total severity is %d (caught %d times)!' % compute_severity(firewall))
    print('First safe offset is %d!' % compute_safe_offset(firewall))


