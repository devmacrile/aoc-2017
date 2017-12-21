# -*- coding: utf-8 -*-

import os
from collections import namedtuple



def particles(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        for i, line in enumerate(f):
            p, v, a = line.strip().split(', ')
            yield i, tuple(map(parse_vector, [p, v, a]))


def parse_vector(v):
    name, vstring = v.split('=')
    tupstr = vstring.replace('<', '').replace('>', '')
    x, y, z = map(int, tupstr.split(','))
    return (x, y, z)


def main():

    def has_zero_accel(acc):
        return any([a == 0 for a in acc])

    def min_terminal_velocity(vel, acc):
        minvel = None
        for i, a in enumerate(acc):
            if a == 0:
                if not minvel:
                    minvel = abs(vel[i])
                else:
                    minvel = min(minvel, abs(vel[i]))
        return minvel

    def dist(v):
        return sum(map(abs, v))

    particle_stream = particles()
    i, (y0, v0, a) = next(particle_stream)
    index, minaccel, minvel = i, dist(a), None
    for i, (y0, v0, a) in particle_stream:
        total_accel = dist(a)
        if total_accel < minaccel:
            index, minaccel = i, total_accel
            minvel = min_terminal_velocity(v0, a)
        elif total_accel == minaccel and min_terminal_velocity(v0, a) < minvel:
            index, minaccel = i, total_accel
            minvel = min_terminal_velocity(v0, a)

    return index, minaccel, minvel

if __name__ == '__main__':
    print('The closest particle as t->inf is %d!' % main()[0])
    