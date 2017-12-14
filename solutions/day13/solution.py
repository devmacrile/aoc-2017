# -*- coding: utf-8 -*-

import os
from collections import namedtuple

"""
class Scanner(object):

    def __init__(self, depth, range_, position=0):
        self.depth = depth
        self.range = range_
        self.position = position

    @property
    def period(self):
        return 2 * (self.range - 1)

    def __repr__(self):
        return 'Scanner(depth=%d, range=%d, period=%d)' % (self.depth, self.range, self.period)
"""

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


def compute_severity():
    firewall = load_firewall()
    severity = 0
    for depth, scanner in firewall.iteritems():
        if scanner.depth >= period(scanner):
            if scanner.depth % period(scanner) == 0:
                severity += scanner.depth * scanner.range
    return severity


if __name__ == '__main__':
    print('Total severity is %d!' % compute_severity())


