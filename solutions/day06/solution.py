# -*- coding: utf-8 -*-


import operator


def main():
    banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

    def state_key(banks):
        return ','.join(map(str, banks))

    cycles = 0
    cache = set()
    key = state_key(banks)

    while key not in cache:
        cache.add(key)

        index, blocks = max(enumerate(banks), key=operator.itemgetter(1))
        banks[index] = 0
        for i in range(1, blocks + 1):
            banks[(index + i) % len(banks)] += 1

        cycles += 1
        key = state_key(banks)

    return cycles


if __name__ == '__main__':
    print('The number of cycles before repeat is %d!' % main())