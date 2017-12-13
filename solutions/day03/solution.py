# -*- coding: utf-8 -*-

import itertools
from collections import defaultdict


def main(target):

    start = 2
    start_pos = (1, 0)
    level_size = 8

    # first determine which 'level' of the spiral
    # our target number resides; compute the 'start',
    # or first member of that 'level'
    while start + level_size < target:
        start += level_size
        start_pos = (start_pos[0] + 1, start_pos[1] - 1)
        level_size += 8

    # compute size of side of level square
    # compute diagonal differentials related to the starting
    # number of this level
    side_size = level_size // 4 + 1
    diags = [j * side_size - j for j in range(1, 5)]
    
    difference = target - start
    for j, diag in enumerate(diags):

        if difference < diag:

            diag = diags[j - 1]
            remainder = difference % diag + 1

            # determine on which side of the spiral 
            # level our number sits
            if j == 0:
                xdiff = 0
                ydiff = target - start
            elif j == 1:
                xdiff = remainder
                ydiff = diags[0] - 1
            elif j == 2:
                xdiff = side_size - 1
                ydiff = (diags[0] - 1) - remainder
            elif j == 3:
                xdiff = side_size - (remainder + 1)
                ydiff = -1

            break

    target_pos = (start_pos[0] - xdiff, start_pos[1] + ydiff)

    return abs(target_pos[0]) + abs(target_pos[1]), target_pos


def stress_test(target):
    turns = {"right": "up", 
                  "up": "left", 
                  "left": "down", 
                  "down": "right"}
    counts = defaultdict(int)

    def neighbors(i, j):
        nothome = lambda x, y: x != 0 or y != 0
        return [(i + a, j + b) for a in [-1, 0, 1] for b in [-1, 0, 1] if nothome(a, b)]

    d = "right"
    i, j = 0, 0
    counts[(i, j)] = 1
    steps_in_direction = itertools.count(1, 0.5)

    while counts[(i, j)] < target:
        steps = int(next(steps_in_direction))
        for _ in range(steps):
            if d == "right":
                i += 1
            elif d == "up":
                j += 1
            elif d == "left":
                i -= 1
            elif d == "down":
                j -= 1

            counts[(i, j)] = sum([counts[tup] for tup in neighbors(i, j)])

        d = turns[d]

    return counts[(i, j)]


if __name__ == '__main__':
    # some simple tests
    # 2 => 1
    # 3 => 2
    # 57 => 8
    target = 368078
    print('The Manhattan distance for %d is %s.' % (target, main(target)))
    print('The first stress test value > our target is %d!' % stress_test(target))
