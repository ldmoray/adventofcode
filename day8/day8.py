import argparse
import ast


def expand(string):
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'") + '"'


def main():
    parser = argparse.ArgumentParser(description='Solve the day 7 challenges for Advent of Code')
    parser.add_argument('string', help='The secret to use', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    parser.add_argument('-p', '--part', action="store_true")
    args = parser.parse_args()
    string = args.string
    if args.part:
        parse = expand
    else:
        parse = ast.literal_eval

    if args.file:
        try:
            instructions = []
            parsed = []
            with open(args.file, 'r') as f:
                for line in f:
                    instructions.append(line[:-1])
            for instruction in instructions:
                parsed.append(parse(instruction))

            diff = []
            for i in range(len(instructions)):
                diff.append(abs(len(instructions[i]) - len(parsed[i])))

            print sum(diff)
            exit()
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not string:
        print 'Please enter a string'
        exit()
    try:
        res = parse(string)
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
