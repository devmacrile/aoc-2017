# -*- coding: utf-8 -*-

from functools import reduce


def main():
    lengths = [129, 154, 49, 198, 200, 133, 97, 254, 41, 6, 2, 1, 255, 0, 191, 108]
    circular = range(256)

    pos = 0
    skip = 0
    for length in lengths:
        if length >= len(circular):
            continue

        if pos + length > len(circular):
            remainder = (pos + length) - len(circular)
            values = list(reversed(circular[pos:] + circular[:remainder]))
            circular[pos:] = values[:len(circular) - pos]
            circular[:remainder] = values[len(circular) - pos:]
        else:
            circular[pos:(pos + length)] = list(reversed(circular[pos:(pos + length)]))

        pos = (pos + length + skip) % 256
        skip += 1

    return circular[0] * circular[1]


def knot_hash(chars):
    ascii_values = [ord(c) for c in chars]
    lengths = ascii_values + [17, 31, 73, 47, 23]
    circular = range(256)

    pos = 0
    skip = 0
    for iteration in range(64):
        for length in lengths:
            if length >= len(circular):
                continue

            if pos + length > len(circular):
                remainder = (pos + length) - len(circular)
                values = list(reversed(circular[pos:] + circular[:remainder]))
                circular[pos:] = values[:len(circular) - pos]
                circular[:remainder] = values[len(circular) - pos:]
            else:
                circular[pos:(pos + length)] = list(reversed(circular[pos:(pos + length)]))

            pos = (pos + length + skip) % 256
            skip += 1

    densehash = []
    for i in range(16):
        start, end = 16 * i, 16 * (i + 1)
        densehash.append(reduce(lambda x, y: x ^ y, circular[start:end]))

    return map(lambda x: format(x, 'x'), densehash)

if __name__ == '__main__':
    chars = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
    print('The product is %d!' % main())
    print('The full hash is %s!' % ''.join(map(str, knot_hash(chars))))
