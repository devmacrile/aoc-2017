# -*- coding: utf-8 -*-

import os
from collections import defaultdict


def loadmap(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        grid = map(lambda x: x.strip(), f.readlines())

    gridmap = defaultdict(lambda: '.')
    nrows, ncols = len(grid), len(grid[0])
    cx, cy = ncols // 2, nrows // 2
    for i in range(nrows):
        for j in range(ncols):
            y, x = cy - i, j - cx
            gridmap[(x, y)] = grid[i][j]
    return gridmap


def main(bursts=10000):
    grid = loadmap()
    # infected = set([k for k, v in grid.iteritems() if v == '#'])

    pos = (0, 0)
    direction = 'up'

    turnright = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    turnleft = {v: k for k, v in turnright.iteritems()}

    def forward(pos, direction):
        if direction == 'up':
            newpos = (pos[0], pos[1] + 1)
        elif direction == 'down':
            newpos = (pos[0], pos[1] - 1)
        elif direction == 'right':
            newpos = (pos[0] + 1, pos[1])
        elif direction == 'left':
            newpos = (pos[0] - 1, pos[1])
        return newpos


    infective_bursts = 0
    for _ in range(bursts):
        if grid[pos] == '.':
            direction = turnleft[direction]
            grid[pos] = 'W'
        elif grid[pos] == 'W':
            grid[pos] = '#'
            infective_bursts += 1
        elif grid[pos] == '#':
            direction = turnright[direction]
            grid[pos] = 'F'
        else:
            direction = turnright[turnright[direction]]
            grid[pos] = '.'
        pos = forward(pos, direction)

    return infective_bursts


if __name__ == '__main__':
    print('The number of infective bursts is %d!' % main(bursts=10000000))
    