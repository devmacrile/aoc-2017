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
            if op in ['snd', 'rcv']:
                op, value = line.split()
                instructions.append((op, value))
            else:
                op, regkey, value = line.split()
                instructions.append((op, regkey, value))
    return instructions


def main():
    instructions = load_instructions()
    register = defaultdict(int)
    last_played = recovered = None

    i = 0
    while not recovered and 0 <= i < len(instructions):
        instruction = instructions[i]
        if instruction[0] in ['snd', 'rcv']:
            op, x = instruction
            if op == 'snd':
                last_played = register[x]
            else:
                recovered = last_played
        else:
            op, x, y = instruction
            val = int(y) if y.lstrip('-').isdigit() else register[y]

            if op == 'set':
                register[x] = val
            elif op == 'add':
                register[x] += val
            elif op == 'mul':
                register[x] *= val
            elif op == 'mod':
                register[x] %= val
            else:
                # jump instruction
                if register[x] > 0:
                    i += (val - 1)  # one added by default below
        i += 1

    return recovered


if __name__ == '__main__':
    print('First recovered frequency is %d!' % main())
