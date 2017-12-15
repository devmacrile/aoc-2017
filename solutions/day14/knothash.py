"""
Knot-hash algorithm from Day 10.
"""

from functools import reduce


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
