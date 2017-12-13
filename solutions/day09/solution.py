# -*- coding: utf-8 -*-

import os
import re


def get_stream(fname='input.txt'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)

    with open(fpath) as f:
        stream = f.read().strip()

    return stream


def main(stream=get_stream()):

    stream = re.sub('!.{1}', '', stream)

    # remove garbage strings from stream
    # using '-' as a replacement character
    in_garbage = False
    total_garbage = 0
    for i, s in enumerate(stream):

        if s == '<' and in_garbage == False:
            in_garbage = True
            start = i
        elif s == '>' and in_garbage == True:
            in_garbage = False
            end = i + 1
            stream = stream[0:start] + '-' * (end - start) + stream[end:]
            total_garbage += end - start - 2

    stream = stream.replace('-', '')

    # compute the score of the valid groups
    nest = 1
    score = 0
    for i, s in enumerate(stream):
        if s == '{':
            nest += 1
        elif s == '}':
            nest -= 1
            score += nest

    return score, total_garbage


def test():
    tests = [("{}", 1),
             ("{{{}}}", 6), 
             ("{{},{}}", 5), 
             ("{{{},{},{{}}}}", 16), 
             ("{<a>,<a>,<a>,<a>}", 1), 
             ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9), 
             ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9), 
             ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)]
    for s, answer in tests:
        score = main(s)
        print(s, score, answer)
        assert score == answer
        print('\n')   


if __name__ == '__main__':
    #test()
    score, garbage = main()
    print('The total score for all groups is %d!' % score)
    print('The total number of (non-cancelled) gargage characters was %d!' % garbage)
