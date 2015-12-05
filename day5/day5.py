import argparse
import re


def is_naughty(string):
    naughty = ['ab', 'cd', 'pq', 'xy']
    for n in naughty:
        if n in string:
            return True
    return False


def has_doubles(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for v in vowels:
        count += string.count(v)
    return count


def has_double_pair(string):
    return re.search(r'(..).*\1', string)


def has_sandwich(string):
    return re.search(r'(.).\1', string)


def is_nice_1(string):
    return not is_naughty(string) and has_doubles(string) and count_vowels(string) >= 3


def is_nice_2(string):
    return has_double_pair(string) and has_sandwich(string)


def main():
    parser = argparse.ArgumentParser(description='Solve the day 5 challenges for Advent of Code')
    parser.add_argument('string', help='The string to check for niceness', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    parser.add_argument('-p', '--part', help='Do part two?', action='store_true')
    args = parser.parse_args()

    string = args.string
    if args.part:
        is_nice = is_nice_2
    else:
        is_nice = is_nice_1
    if args.file:
        try:
            nice = []
            with open(args.file, 'r') as f:
                for line in f:
                    nice.append(line[:-1])
            nice = [n for n in nice if is_nice(n)]
            print len(nice)
            exit()
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not string:
        print 'Please enter a string'
        exit()
    try:
        if is_nice(string):
            print string + ' is nice'
        else:
            print string + ' is not nice'
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
