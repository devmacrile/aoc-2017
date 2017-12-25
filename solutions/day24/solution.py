# -*- coding: utf-8 -*-

import os
from operator import itemgetter


def load_ports(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        lines = map(lambda line: line.strip(), f.readlines())
        ports = map(lambda line: tuple(map(int, line.split('/'))), lines)
    return ports


def main():
    ports = load_ports()

    def chainsum(chain):
        return sum(map(sum, chain))

    def optbridge(chain, ports, pins=0):
        valid = [p for p in ports if pins in p]
        if not valid:
            return len(chain), chainsum(chain)  # chainsum(chain)
        else:
            arguments = []
            for v in valid:
                newpins = v[1] if v[0] == pins else v[0]
                subports = ports[:]
                subports.remove(v)
                superchain = chain[:]
                superchain.append(v)
                arguments.append((superchain, subports, newpins))
            candidates = [optbridge(*args) for args in arguments]
            return max(candidates, key=lambda x: x[0] * x[1])

    return optbridge([], ports)


if __name__ == '__main__':
    print('The max length chain is %d, with strength %d!' % main())
