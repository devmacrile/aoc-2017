# -*- coding: utf-8 -*-

import os
from collections import defaultdict, deque


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


def evaluate(op, x, val, register, index):
    if op == 'set':
        register[x] = val
    elif op == 'add':
        register[x] += val
    elif op == 'mul':
        register[x] *= val
    elif op == 'mod':
        register[x] %= val
    elif op == 'jgz':
        if x.isdigit():
            if int(x) > 0:
                index += (val - 1)
        elif register[x] > 0:
            index += (val - 1)

    return index, register


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
            i, register = evaluate(op, x, val, register, i)

        i += 1

    return recovered


def messaging():

    def make_register(pid):
        r = defaultdict(int)
        r['p'] = pid
        return r

    def make_generator(register, readq, writeq):
        i = 0
        while 0 <= i < len(instructions):
            if instructions[i][0] in ['snd', 'rcv']:
                op, x = instructions[i]
                val = int(x) if x.lstrip('-').isdigit() else register[x]
            else:
                op, x, y = instructions[i]
                val = int(y) if y.lstrip('-').isdigit() else register[y]
            
            # dipatch on operation type
            if op in ['set', 'add', 'mul', 'mod', 'jgz']:
                i, register = evaluate(op, x, val, register, i)
            elif op == 'snd':
                writeq.append(val)
                yield 's'
            elif op == 'rcv':
                if not readq:
                    yield 'w'
                else:
                    register[x] = readq.popleft()
                    yield 'r'

            i += 1


    instructions = load_instructions()
    q0 , q1= deque(), deque()
    r0, r1 = make_register(pid=0), make_register(pid=1)
    p0, p1 = make_generator(r0, q0, q1), make_generator(r1, q1, q0)

    count = 0
    while True:
        x, y = next(p0), next(p1)
        if y == 's':
            count += 1
        # check for deadlock
        if x == 'w' and y == 'w':
            break

    return count


if __name__ == '__main__':
    print('First recovered frequency is %d!' % main())
    print('Program 1 sends %d times!' % messaging())
