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


def checksum():
    rows = load_input('input.txt')
    checksum = sum(map(lambda x: max(x) - min(x), rows))
    return checksum


def rowsum():
    rows = load_input('input.txt')
    mults = []
    for row in rows:
        for i, v in enumerate(row):
            for w in row[i+1:]:
                if max(v, w) % min(v, w) == 0:
                    mults.append(max(v, w) // min(v, w))
                    break
    return sum(mults)


if __name__ == '__main__':
    print('The checksum is: %d (the row result sum is %d)!' % (checksum(), rowsum()))