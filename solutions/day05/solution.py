# -*- coding: utf-8 -*-

import os


def load_instructions(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        contents = f.read().strip()
        instructions = contents.split('\n')
    return list(map(int, instructions))


def main():
    instructions = load_instructions()
    
    i = 0
    steps = 0
    while 0 <= i < len(instructions):
        index = i
        i += instructions[i]
        instructions[index] += 1
        steps += 1

    return steps


if __name__ == '__main__':
    print('Maze escaped in %d steps!' % main())