import argparse
from collections import defaultdict
from itertools import permutations


def parse(rules, line):
    line = line.split(' ')
    origin = line[0]
    dest = line[-1][:-1]
    direction = line[2]
    value = int(line[3])

    if direction == 'lose':
        value = -value
    rules[origin][dest] = value


def find_happiness(rules, ordering):
    happiness = 0
    ordering.append(ordering[0])
    for i in range(len(ordering) - 1):
        happiness += rules[ordering[i]][ordering[i + 1]]
    ordering.reverse()
    for i in range(len(ordering) - 1):
        happiness += rules[ordering[i]][ordering[i + 1]]
    return happiness


def find_max_happiness(rules):
    happinesses = []
    for i in permutations(rules.keys()):
        happinesses.append(find_happiness(rules, list(i)))
    return max(happinesses)


def add_me(rules, me):
    me = 'Lenny'
    for k in rules.keys():
        rules[me][k] = 0
        rules[k][me] = 0


def main():
    parser = argparse.ArgumentParser(description='Solve the day 13 challenges for Advent of Code')
    parser.add_argument('file', help='The secret to use', nargs='?')
    args = parser.parse_args()
    rules = defaultdict(dict)
    try:
        with open(args.file, 'r') as f:
            for line in f:
                parse(rules, line[:-1])
    except IOError as err:
        print 'There was an error reading from disk: %s' % err.strerror
        exit()

    add_me(rules, 'Lenny')
    print find_max_happiness(rules)


if __name__ == '__main__':
    main()
