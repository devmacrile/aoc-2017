# -*- coding: utf-8 -*-

import os
from collections import defaultdict


def load_instruction_set(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    with open(fpath) as f:
        instructions = f.readlines()

    return instructions


def main():
    instructions = load_instruction_set()
    
    register = defaultdict(int)
    register_ceiling = 0

    def get_mutation_params(instruction):
        variable, action, value = instruction.split()[:3]
        assert action in ['inc', 'dec']
        return variable, action, int(value)

    def parse_clause(instruction):
        clause = instruction.split()[4:]
        variable = clause[0].strip()
        clause[0] = 'register["%s"]' % variable
        return ' '.join(clause)


    for instruction in instructions:
        clause = parse_clause(instruction)
        if eval(clause):
            variable, action, value = get_mutation_params(instruction)
            if action == 'inc':
                register[variable] += value
            elif action == 'dec':
                register[variable] -= value

            register_ceiling = max(register_ceiling, register[variable])

    variable, max_final = max(register.items(), key=lambda k: k[1])
    return variable, max_final, register_ceiling


if __name__ == '__main__':
    print('The max register is ["%s" = %d], with the max value encountered %d!' % main())