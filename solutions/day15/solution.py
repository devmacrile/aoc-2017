# -*- coding: utf-8 -*-
"""
Generator A starts with 289
Generator B starts with 629
"""


def makegen(start, scale, multiple, divisor=2147483647):
    product = start * scale
    yield product % divisor
    while True:
        if product % multiple == 0:
            yield product
        product = (product * scale) % divisor


def main(iterations=int(40e6), multiples=(1, 1), verbose=True):
    matches = 0
    divisor = 2 ** 16
    gena = makegen(289, 16807, multiples[0])
    genb = makegen(629, 48271, multiples[1])
    for i in range(iterations):
        if next(gena) % divisor == next(genb) % divisor:
            matches += 1

        if verbose:
            if i == 0:
                print('Starting...')
            elif i % (iterations // 10) == 0 and i > 0:
                print('%d%s complete...' % ((100 * i // iterations), '%'))
            elif i == iterations - 1:
                print('Done.')

    return matches


if __name__ == '__main__':
    #print('Part1: The judges final count is %d!' % main())
    print('Part2: The judges final count is %d!' % main(int(5e6), (4, 8)))
