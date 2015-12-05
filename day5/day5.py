import argparse
import re

def foo(pattern):
    pass


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


def is_nice(string):
    if not is_naughty(string):
        if has_doubles(string) and count_vowels(string) >= 3:
            return True
    return False

def main():
    parser = argparse.ArgumentParser(description='Solve the day 5 challenges for Advent of Code')
    parser.add_argument('string', help='The string to check for niceness', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    args = parser.parse_args()

    string = args.string
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
