# -*- coding: utf-8 -*-

import os
from collections import defaultdict, deque


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
    groups = defaultdict(set)

    def discovered(vertex):
        for source, group in groups.iteritems():
            if vertex in group:
                return True
        return False

    def bfs(graph, source):
        q = deque()
        q.append(source)
        groups[source].add(source)
        while len(q) > 0:
            v = q.popleft()
            neighbors = graph[v]
            for w in neighbors:
                if not discovered(w):
                    groups[source].add(w)
                    q.append(w)

    # sorted ensures 0 is first => guaranteed to 
    # be the leader key for a group
    for v in sorted(graph.keys()):
        if not discovered(v):
            bfs(graph, v)
            
    return len(groups['0']), len(groups)


if __name__ == '__main__':
    print('The size of the "0-group" is %d (%d groups overall)!' % main())