import argparse
import re


def has_straight(string, length):
    for i in range(len(string) - length):
        for j in range(length):
            if ord(string[i]) + j != ord(string[i+j]):
                break
        else:
            return True
    else:
        return False


def foo(string, banned):
    for i in banned:
        if i in string:
            return False
    else:
        return True


def has_pairs(string, count):
    pair = ''
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and string[i] not in pair:
            pair += string[i]

    if len(pair) >= count:
        return True
    else:
        return False


def is_secure_1(string):
    return has_straight(string, 3) and foo(string, ['i', 'o', 'l']) and has_pairs(string, 2)


def next_string(string):
    res = ''
    if not string:
        res = 'a'
    elif string[-1] == 'z':
        res = next_string(string[:-1]) + 'a'
    else:
        res = string[:-1] + chr(ord(string[-1]) + 1)
    return res


def main():
    parser = argparse.ArgumentParser(description='Solve the day 5 challenges for Advent of Code')
    parser.add_argument('string', help='The string to check for niceness', default='', nargs='?')
    parser.add_argument('-p', '--part', help='Do part two?', action='store_true')
    args = parser.parse_args()

    string = args.string
    if args.part:
        is_secure = is_secure_2
    else:
        is_secure = is_secure_1

    if not string:
        print 'Please enter a string'
        exit()
    try:
        string = next_string(string)
        while not is_secure(string):
            string = next_string(string)

        print string + ' is secure'
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
