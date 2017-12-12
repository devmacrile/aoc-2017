# -*- coding: utf-8 -*-

import os


def load_input(fname):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        data = f.read().strip()
    return data


def main(digseq, skip=1):

    total = 0
    for i, s in enumerate(digseq):
        if s == digseq[(i + skip) % len(digseq)]:
            total += int(s)

    return total


if __name__ == '__main__':
    digseq = load_input('input.txt')
    print('CAPTCHA solutions are: %d, %d' % (main(digseq), main(digseq, len(digseq) // 2)))
