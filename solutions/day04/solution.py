# -*- coding: utf-8 -*-

import os


def load_phrases(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        phrases = f.read().strip().split('\n')
        phrasewords = [p.split() for p in phrases]
    return phrasewords


def main(anagrams=True):
    phrases = load_phrases()
    if not anagrams:
        valid = filter(lambda x: len(x) == len(set(map(lambda y: ''.join(sorted(y)), x))), phrases)
    else:
        valid = filter(lambda x: len(x) == len(set(x)), phrases)
    return len(valid)


if __name__ == '__main__':
    print('Number of valid phrases is %d' % main())
    print('Number of non-anagram phrases is %d' % main(anagrams=False))