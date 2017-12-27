# -*- coding: utf-8 -*-

from collections import defaultdict

def turing():
    tape = defaultdict(int)
    cursor = 0
    state = 'A'

    steps = 0
    while steps < 12523873:
        if state == 'A':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = 'B'
            else:
                cursor -= 1
                state = 'E'
        elif state == 'B':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = 'C'
            else:
                cursor += 1
                state = 'F'
        elif state == 'C':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'D'
            else:
                tape[cursor] = 0
                cursor += 1
                state = 'B'
        elif state == 'D':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = 'E'
            else:
                tape[cursor] = 0
                cursor -= 1
                state = 'C'
        elif state == 'E':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'A'
            else:
                tape[cursor] = 0
                cursor += 1
                state = 'D'
        elif state == 'F':
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = 'A'
            else:
                cursor += 1
                state = 'C'

        steps += 1

    return sum(tape.values())


if __name__ == '__main__':
    print('The diagnostic checksum is %d!' % turing())