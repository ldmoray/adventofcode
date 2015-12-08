import argparse
from collections import defaultdict


circuit = {}


def build_circuit(string):
    x = string.split(' ')
    source, dest = x[:-2], x[-1].rstrip()
    for i in range(len(source)):
        if source[i].isdigit():
            source[i] = int(source[i])
    circuit[dest] = source


def get_signal(wire):
    res = None
    if isinstance(wire, (int, long)):
        return wire
    source = circuit[wire]
    if len(source) == 1:
        if isinstance(source[0], (int, long)):
            res = source[0]
        else:
            res = get_signal(source[0])
    else:
        if source[0] == 'NOT':
            res = ~get_signal(source[1])
        else:
            a = source[0]
            command = source[1]
            b = source[2]
            if command == 'AND':
                res = get_signal(a) & get_signal(b)
            elif command == 'OR':
                res = get_signal(a) | get_signal(b)
            elif command == 'LSHIFT':
                res = get_signal(a) << b
            else:
                res = get_signal(a) >> b
    circuit[wire] = [res]
    return res



def main():
    parser = argparse.ArgumentParser(description='Solve the day 6 challenges for Advent of Code')
    parser.add_argument('string', help='The secret to use', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    args = parser.parse_args()
    string = args.string
    if args.file:
        try:
            instructions = []
            with open(args.file, 'r') as f:
                for line in f:
                    instructions.append(line)
            for instruction in instructions:
                build_circuit(instruction)

            print get_signal('a')
            exit()
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not string:
        print 'Please enter a string'
        exit()
    try:
        res = foo(string)
        print res
    except ValueError as err:
        print str(err)

    try:
        a = find_smallest_int(args.secret, args.prefix)
        print "The smallest positive integer is %d" % a
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
