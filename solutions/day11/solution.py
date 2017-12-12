# -*- coding: utf-8 -*-

import os
import math
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def load_directions(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    with open(fpath) as f:
        directions = f.read().strip()
    return directions.split(',')


def main(directions=load_directions()):

    pos = Point(0, 0)
    hexmap = {'n': Point(0, 1),
              'ne': Point(1, 1),
              'se': Point(1, 0),
              's': Point(0, -1),
              'sw': Point(-1, -1),
              'nw': Point(-1, 0)}

    def hexdist(x, y):
        return max(map(abs, [x, y, x - y]))

    max_distance = 0
    for direction in directions:
        move = hexmap[direction]
        pos = Point(pos.x + move.x, pos.y + move.y)
        max_distance = max(max_distance, hexdist(pos.x, pos.y))

    return hexdist(pos.x, pos.y), max_distance


def tests():
    examples = [('se,sw,se,sw,sw'.split(','), 3),
                ('ne,ne,sw,sw'.split(','), 0), 
                ('ne,ne,s,s'.split(','), 2),
                ('ne,ne,ne'.split(','), 3)]
    for directions, answer in examples:
        guess, _ = main(directions)
        print('-----------------------')
        print(directions, guess, answer)
        assert guess == answer
    print('Ok.')
    return True


if __name__ == '__main__':
    tests()
    print('The shortest distance is %d (max distance is %d)!' % main())
