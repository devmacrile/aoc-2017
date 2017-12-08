# -*- coding: utf-8 -*-

import os
from collections import defaultdict, deque


def load_tower(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    tree = defaultdict(list)
    with open(fpath) as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            if '->' in line:
                name, weight = line.split('->')[0].split()
                neighbors = map(lambda x: x.strip(), line.split('->')[1].split(','))
                for neighbor in neighbors:
                    tree[neighbor].append(name)

    return tree


def main():
    tower = load_tower()
    program = tower.keys()[0]  # arbitrary source

    def has_children(program):
        return len(tower[program]) > 0

    while has_children(program):
        program = tower[program][0]

    return program


if __name__ == '__main__':
    print('The supporting program is %s!' % main())

