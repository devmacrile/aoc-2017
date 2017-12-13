# -*- coding: utf-8 -*-

import os
from collections import defaultdict


def load_adjacency_list(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    
    graph = defaultdict(list)
    with open(fpath) as f:
        for line in f.readlines():
            source, neighbors = line.strip().replace(' ', '').split('<->')
            graph[source] = neighbors.split(',')
    return graph

def main():
    graph = load_adjacency_list()
    group = set()

    def dfs(program):
        group.add(program)
        for neighbor in graph[program]:
            if neighbor not in group:
                dfs(neighbor)

    dfs('0')
    return len(group)


if __name__ == '__main__':
    print('The size of the "0-group" is %d!' % main())