# -*- coding: utf-8 -*-

import os
from collections import Counter


def gen_particles(fname='input.txt'):
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

    particle_stream = gen_particles()
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


def step(d):
    d[1][0] += d[2][0]
    d[1][1] += d[2][1]
    d[1][2] += d[2][2]
    d[0][0] += d[1][0]
    d[0][1] += d[1][1]
    d[0][2] += d[1][2]


def collisions():
    particles = map(lambda x: x[1], list(gen_particles()))

    def step(particle):
        x, y, z = particle[0]
        vx, vy, vz = particle[1]
        ax, ay, az = particle[2]
        newv = (vx + ax, vy + ay, vz + az)
        vx, vy, vz = newv
        newp = (x + vx, y + vy, z + vz)
        return (newp, newv, (ax, ay, az))

    unchanged_steps = 0
    num_particles = len(particles)
    print(len(particles))
    while unchanged_steps < 1000:
        positions = {}
        delete = []

        particles = map(step, particles)
        positions = map(lambda x: x[0], particles)
        pcounts = Counter(positions)
        collisions = set([pos for pos, pcount in pcounts.iteritems() if pcount > 1])
        if collisions:
            print(collisions, len(collisions))

        toremove = []
        for i, particle in enumerate(particles):
            if particle[0] in collisions:
                toremove.append(particle)

        for particle in toremove:
            particles.remove(particle)

        if len(particles) == num_particles:
            unchanged_steps += 1
        else:
            unchanged_steps = 0

        num_particles = len(particles)
    
    return len(particles)


if __name__ == '__main__':
    print('The closest particle as t->inf is %d!' % main()[0])
    print('The number of uncollided particles is %d!' % collisions())
