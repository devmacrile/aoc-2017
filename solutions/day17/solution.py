# -*- coding: utf-8 -*-
"""
Input is 366.
"""

def main(stepsize=366):
    circbuff = [0]
    position = 0

    for value in range(1, 2017 + 1):
        position = (position + stepsize) % len(circbuff) + 1
        circbuff = circbuff[:position] + [value] + circbuff[position:]
        value += 1

    return circbuff[(position + 1) % len(circbuff)]


def zeroneighbor(iterations=5e7, stepsize=366):
    zeropos = 0
    follower = None
    position = zeropos
    for i in range(1, int(iterations) + 1):
        position = (position + stepsize) % i + 1
        if position - zeropos == 1 or \
          (position == 0 and zeropos == i):
            follower = i
        if position < zeropos:
            zeropos += 1
    return follower


if __name__ == '__main__':
    #print(main(stepsize=366))
    print(zeroneighbor())