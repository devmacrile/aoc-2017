# -*- coding: utf-8 -*-

import os


def load_dance(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    dance = []
    with open(fpath) as f:
        movestring = f.read().strip()
        moves = movestring.split(',')
        for move in moves:
            if move[0] == 's':
                dance.append((move[0], int(move[1:])))
            elif move[0] == 'x':
                dance.append((move[0], map(int, move[1:].split('/'))))
            else:
                dance.append((move[0], move[1:].split('/')))
    return dance


def dance(programs, dance):
    for move in dance:
        if move[0] == 's':
            i = move[1]
            programs = programs[-i:] + programs[:-i]
        else:
            if move[0] == 'p':
                getindex = lambda j: [i for i in range(len(programs)) if programs[i] == move[1][j]][0]
                i = int(getindex(0))
                j = int(getindex(1))
            else:
                i, j = move[1]
            programs[i], programs[j] = programs[j], programs[i]
    return list(programs)


def danceathon(n=1000000000):
    programs = map(chr, range(97, 113))
    moves = load_dance()

    # run one iteration
    program_key = ''.join(programs)
    programs = dance(programs, moves)
    cycle = 1

    # find cycle size
    while ''.join(programs) != program_key:
        cycle += 1
        programs = dance(programs, moves)

    for i in range(n % cycle):
        programs = dance(programs, moves)

    return programs

if __name__ == '__main__':
    print('Program order after dance is %s' % ''.join(danceathon(n=1)))
    print('Program order after dance-athon is %s' % ''.join(danceathon()))

