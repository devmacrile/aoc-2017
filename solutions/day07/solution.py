# -*- coding: utf-8 -*-

import os
from collections import defaultdict


def load_tower(fname='input.txt', reverse=True):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    tree = defaultdict(list)
    weights = defaultdict(int)
    with open(fpath) as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            name, weight = line.split()[:2]
            weights[name] = int(weight.replace('(', '').replace(')', ''))
            if '->' in line:
                neighbors = map(lambda x: x.strip(), line.split('->')[1].split(','))
                if reverse:
                    for neighbor in neighbors:
                        tree[neighbor].append(name)
                else:
                    tree[name].extend(neighbors)
    return tree, weights


def bottom_program(tower):
    program = tower.keys()[0]  # arbitrary source

    def has_children(program):
        return len(tower[program]) > 0

    while has_children(program):
        program = tower[program][0]

    return program


def wrong_weight(tower, weights, source):
    summed_weights = {}

    def calculate_weight(program):
        children = tower[program]
        if not children:
            return weights[program]
        else:
            return weights[program] + sum(map(calculate_weight, children))

    children = tower[source]
    child_weights = map(calculate_weight, children)
    while len(set(child_weights)) > 1:
        sibling_weight = max(set(child_weights), key=child_weights.count)
        problem_index = (i for i, w in enumerate(child_weights) if w != sibling_weight).next()
        problem_child = children[problem_index]

        children = tower[problem_child]
        child_weights = map(calculate_weight, children)

    correct_weight = sibling_weight - sum(child_weights)
    return problem_child, correct_weight



if __name__ == '__main__':
    tower, _ = load_tower()
    bottom = bottom_program(tower)
    print('The supporting program is %s!' % bottom)

    tower, weights = load_tower(reverse=False)
    print('The broken program is %s, which needs to weigh %d!' % wrong_weight(tower, weights, bottom))

