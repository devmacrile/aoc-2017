# -*- coding: utf-8 -*-


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


if __name__ == '__main__':
    print('The product is %d!' % main())