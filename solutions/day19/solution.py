# -*- coding: utf-8 -*-

import os


def load_grid(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    grid = []
    with open(fpath) as f:
        for line in f.readlines():
            if line.strip():
                grid.append(list(line.rstrip('\n')))
    return grid

def main():
    grid = load_grid()
    alphabet = set(map(chr, range(ord('A'), ord('Z') + 1)))
    routechars = set(['|', '-', '+'])

    direction_deltas = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }

    direction_chars = {
        'up': '|',
        'down': '|',
        'left': '-',
        'right': '-'
    }

    def axis_directions(direction):
        if direction in ['up', 'down']:
            return ['up', 'down']
        else:
            return ['left', 'right']

    opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

    add_delta = lambda x, y: [x[0] + y[0], x[1] + y[1]]
    ingrid = lambda loc: (0 <= loc[0] < len(grid)) and (0 <= loc[1] < len(grid[0]))

    def gridval(location):
        return grid[location[0]][location[1]]

    def getnext(grid, location, direction):
        frontier = [(k, add_delta(location, delta)) for k, delta in direction_deltas.iteritems() if k != opposite[direction]]
        routes = filter(lambda x: ingrid(x[1]) and gridval(x[1]) in alphabet.union(routechars), frontier)
        if not routes:
            new_direction = None
            new_location = None
        else:
            if gridval(location) == '+':
                turns = filter(lambda x: x[0] != direction, routes)
                assert len(turns) == 1
                new_direction, new_location = turns[0]
            else:
                new_location = add_delta(location, direction_deltas[direction])
                new_direction = direction
        return new_direction, new_location
        
    path = []
    direction = 'down'
    location = [0, grid[0].index('|')]
    direction, next_location = getnext(grid, location, direction)
    while next_location:
        nextchar = gridval(location)
        if nextchar in alphabet:
            path.append(nextchar)

        location = next_location
        direction, next_location = getnext(grid, location, direction)

    return ''.join(path)


if __name__ == '__main__':
    print('Letters encountered in the path are "%s"' % main())

