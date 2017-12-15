# -*- coding: utf-8 -*-

from functools import reduce


def main():
    lengths = [129, 154, 49, 198, 200, 133, 97, 254, 41, 6, 2, 1, 255, 0, 191, 108]
    circular = range(256)
    circular, pos, skip = knot_iteration(circular, lengths, 0, 0)
    return circular[0] * circular[1]


def knot_iteration(sparse_hash, lengths, pos, skip):
    for length in lengths:
        if length >= len(sparse_hash):
            continue

        if pos + length > len(sparse_hash):
            remainder = (pos + length) - len(sparse_hash)
            values = list(reversed(sparse_hash[pos:] + sparse_hash[:remainder]))
            sparse_hash[pos:] = values[:len(sparse_hash) - pos]
            sparse_hash[:remainder] = values[len(sparse_hash) - pos:]
        else:
            sparse_hash[pos:(pos + length)] = list(reversed(sparse_hash[pos:(pos + length)]))

        pos = (pos + length + skip) % 256
        skip += 1

    return sparse_hash, pos, skip


def knot_hash(chars):
    ascii_values = [ord(c) for c in chars]
    lengths = ascii_values + [17, 31, 73, 47, 23]
    sparse_hash = range(256)

    pos, skip = 0, 0
    for i in range(64):
        sparse_hash, pos, skip = knot_iteration(sparse_hash, lengths, pos, skip)

    densehash = []
    for i in range(16):
        start, end = 16 * i, 16 * (i + 1)
        densehash.append(reduce(lambda x, y: x ^ y, sparse_hash[start:end]))

    return ''.join(map(lambda x: format(x, 'x').zfill(2), densehash))

if __name__ == '__main__':
    chars = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
    print('The product is %d!' % main())
    print('The full hash is %s!' % knot_hash(chars))
