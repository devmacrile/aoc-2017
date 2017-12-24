# -*- coding: utf-8 -*-

import os
from collections import defaultdict


def load_instructions(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    instructions = []
    with open(fpath) as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            op = line[:3]
            op, regkey, value = line.split()
            instructions.append((op, regkey, value))
    return instructions


def main():
    instructions = load_instructions()
    register = defaultdict(int)

    i = 0
    muls = 0
    while 0 <= i < len(instructions):
        instruction = instructions[i]
        op, x, y = instruction
        val = int(y) if y.lstrip('-').isdigit() else register[y]

        if op == 'set':
            register[x] = val
        elif op == 'sub':
            register[x] -= val
        elif op == 'mul':
            register[x] *= val
            muls += 1
        else:
            # jump instruction
            if x.isdigit():
                if int(x) != 0:
                    i += (val - 1)
            elif register[x] != 0:
                i += (val - 1)
        i += 1

    return muls

if __name__ == '__main__':
    print('The number of muls is %d!' % main())