# -*- coding: utf-8 -*-

import os
import math
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


def disassembled():
    a = 1
    b = 67 * 100 + 100000
    c = b + 17000
    g = 1

    while g != 0:
        f = 1
        d = 2
        # for all e, d pairs
        # check if create b
        # i.e. b is composite
        while g != 0:
            e = 2
            # from e up to b
            while g != 0:
                g = e * d - b

                # check e, d are factors of b
                # => b is composite
                if g == 0:
                    f = 0

                e += 1
                g = e - b
            d += 1
            g = d - b

        # if b is composite
        if f == 0:
            h += 1

        g = b - c
        if g != 0:
            b += 17

    return h


def optimized():
    lowerbound = 67 * 100 + 100000
    upperbound = lowerbound + 17000
    composites = 0
    for cand in range(lowerbound, upperbound + 1, 17):
        if any(cand % d == 0 for d in range(2, int(math.sqrt(cand)))):
            composites += 1
    return composites


if __name__ == '__main__':
    #print('The number of muls is %d!' % main())
    print('The (optimized) program returns %d!' % optimized())
