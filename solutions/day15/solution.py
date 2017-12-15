# -*- coding: utf-8 -*-
"""
Generator A starts with 289
Generator B starts with 629
"""


def makegen(start, scale, divisor=2147483647):
    product = start * scale
    yield product % divisor
    while True:
        product = (product * scale) % divisor
        yield product


def main(iterations=int(40e6), verbose=True):
    matches = 0
    divisor = 2 ** 16
    gena = makegen(289, 16807)
    genb = makegen(629, 48271)
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
    print('The judges final count is %d!' % main())