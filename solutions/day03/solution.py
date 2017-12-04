# -*- coding: utf-8 -*-


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


if __name__ == '__main__':
    # some simple tests
    # 2 => 1
    # 3 => 2
    # 57 => 8
    target = 368078
    print('The Manhattan distance for %d is %s.' % (target, main(target)))