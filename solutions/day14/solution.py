# -*- coding: utf-8 -*-

from knothash import knot_hash


def used_count(keystring, disk_dim=(128, 128)):
    occupied = 0
    for i in range(disk_dim[0]):
        hash_input = '-'.join([keystring, str(i)])
        hash_value = knot_hash(hash_input)
        binary = bin(int(hash_value, 16))[2:]
        occupied += sum(map(int, str(binary)))
    return occupied

if __name__ == '__main__':
    print('Number of occupied squares is %d!' % used_count('hwlqcszp'))