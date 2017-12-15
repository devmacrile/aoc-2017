# -*- coding: utf-8 -*-

from collections import deque

from knothash import knot_hash


def hextobinary(hexval):
    assert len(hexval) == 32
    return bin(int(hexval, 16))[2:].zfill(128)

def used_count(keystring):
    occupied = compute_occupied_cells(keystring)
    return len(occupied)

def compute_occupied_cells(keystring):
    occupied = set()
    for i in range(128):
        hashval = knot_hash('-'.join([keystring, str(i)]))
        binary = map(int, hextobinary(hashval))
        occupied.update([(i, j) for j, bit in enumerate(binary) if bit])
    return occupied

def connected_components(keystring):
    """
    Simple bfs to find connected components.
    """
    num_components = 0
    unexplored = compute_occupied_cells(keystring)

    while len(unexplored) > 0:
        q = deque()
        q.append(next(iter(unexplored)))
        while len(q) > 0:
            (x, y) = q.popleft()
            if (x, y) in unexplored:
                unexplored.remove((x, y))
                q.extend([(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)])
        num_components += 1
        
    return num_components


if __name__ == '__main__':
    keystring = 'hwlqcszp'
    print('Number of occupied squares is %d!' % used_count(keystring))
    print('Number of connected components is %d!' % connected_components(keystring))
