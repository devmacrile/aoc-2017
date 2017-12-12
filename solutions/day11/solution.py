# -*- coding: utf-8 -*-

import os
import math


def load_directions(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    with open(fpath) as f:
        directions = f.read().strip()
    return directions.split(',')


def main(directions=load_directions()):

    def hexdist(x, y):
        return max(map(abs, pos + [pos[0] - pos[1]]))

    pos = [0, 0]
    hexmap = {'n': [0, 1],
              'ne': [1, 1],
              'se': [1, 0],
              's': [0, -1],
              'sw': [-1, -1],
              'nw': [-1, 0]}

    max_distance = 0
    for direction in directions:
        move = hexmap[direction]
        pos = [pos[0] + move[0], pos[1] + move[1]]
        max_distance = max(max_distance, hexdist(pos[0], pos[1]))

    return hexdist(pos[0], pos[1]), max_distance


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
