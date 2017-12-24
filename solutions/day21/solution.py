# -*- coding: utf-8 -*-

import os
from collections import Counter


def load_rules(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    rules = {}
    with open(fpath) as f:
        for line in f:
            i, o = line.strip().split(' => ')
            rotations = [identity, rotate90, rotate180, rotate270]
            for rotation in rotations:
                rules[rotation(i)] = o
                rules[flip(rotation(i))] = o
    return rules


rows = lambda art: art.split('/')
cols = lambda art: [''.join(map(lambda x: x[i], rows(art))) for i in range(len(rows(art)))]
rotate = lambda art: '/'.join(map(lambda x: x[::-1], cols(art)))
flip = lambda art: '/'.join(map(lambda x: x[::-1], rows(art)))
identity = lambda x: x
rotate90 = rotate
rotate180 = lambda x: rotate(rotate(x))
rotate270 = lambda x: rotate(rotate(rotate(x)))


def grow_art(art, rules):
    r, c = rows(art), cols(art)
    size = len(r[0])  # assert all equal if paranoid
    factor = 2 if size % 2 == 0 else 3
    cellsize = size // factor

    # initialize grid of unit art
    supergrid = [[None for x in range(cellsize)] for y in range(cellsize)]
    for i in range(cellsize):
        for j in range(cellsize):
            rstart, rend = i * factor, (i + 1) * factor
            cstart, cend = j * factor, (j + 1) * factor
            artcell = '/'.join([r[k][cstart:cend] for k in range(rstart, rend)])
            supergrid[i][j] = rules[artcell]

    # stitch together super rows into valid art form
    newart = []
    for i, superrow in enumerate(supergrid):
        newrows = [''.join(map(lambda x: x.split('/')[i], superrow)) for i in range(factor + 1)]
        newart.append('/'.join(newrows))

    return '/'.join(newart)


def main(iterations=5):
    rules = load_rules()
    art = '.#./..#/###'

    for i in range(iterations):
        art = grow_art(art, rules)

    return Counter(art)['#']


if __name__ == '__main__':
    print('The number of on pixels after 5 iterations is %d!' % main(iterations=18))
