# -*- coding: utf-8 -*-

import os


def load_input(fname):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    rows = []
    with open(fpath) as f:
        for line in f.readlines():
            vals = map(int, line.strip().split('\t'))
            rows.append(vals)
    return rows


def main():
    rows = load_input('input.txt')
    checksum = sum(map(lambda x: max(x) - min(x), rows))
    return checksum


if __name__ == '__main__':
    print('The checksum is: %d' % main())