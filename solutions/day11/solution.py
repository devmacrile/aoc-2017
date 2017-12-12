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

    pos = [0, 0]
    dmap = {'n': [0, 1],
            'ne': [1, 1],
            'se': [1, 0],
            's': [0, -1],
            'sw': [-1, -1],
            'nw': [-1, 0]}
    for direction in directions:
        move = dmap[direction]
        pos = [pos[0] + move[0], pos[1] + move[1]]

    dist = max(abs(pos[0]), abs(pos[1]), abs(pos[0] - pos[1]))

    return dist


def tests():
    examples = [('se,sw,se,sw,sw'.split(','), 3),
                ('ne,ne,sw,sw'.split(','), 0), 
                ('ne,ne,s,s'.split(','), 2),
                ('ne,ne,ne'.split(','), 3)]
    for directions, answer in examples:
        guess = main(directions)
        print('-----------------------')
        print(directions, guess, answer)
        assert guess == answer
    print('Ok.')
    return True


if __name__ == '__main__':
    tests()
    print('The shortest distance is %d!' % main())
