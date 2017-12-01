import os


def load_input(fname):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fpath = os.path.join(dir_path, fname)
    with open(fpath) as f:
        data = f.read().strip()
    return data


def main():
    digseq = load_input('input.txt')

    total = 0
    for i, s in enumerate(digseq[1:]):
        if s == digseq[i]:
            total += int(s)

    # wrap-around case
    if digseq[0] == digseq[-1]:
        total += int(digseq[0])

    return total


if __name__ == '__main__':
    print('CAPTCHA solution is: %d' % main())
