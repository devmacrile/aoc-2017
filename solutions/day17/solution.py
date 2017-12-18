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

if __name__ == '__main__':
    print(main(stepsize=366))