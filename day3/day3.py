import argparse


def visit_houses(pattern):
    curr = (0,0)
    houses = [curr]
    for char in pattern:
        if char == '^':
            curr = (curr[0] + 1, curr[1])
            houses.append(curr)
        elif char == 'v':
            curr = (curr[0] - 1, curr[1])
            houses.append(curr)
        elif char == '>':
            curr = (curr[0], curr[1] + 1)
            houses.append(curr)
        elif char == '<':
            curr = (curr[0], curr[1] - 1)
            houses.append(curr)
        elif char != '\n':
            raise ValueError('Invalid instruction for Santa')
    return houses

def main():
    parser = argparse.ArgumentParser(description='Solve the day 3 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern of directiosn to solve', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    args = parser.parse_args()

    pattern = args.pattern
    if args.file:
        try:
            with open(args.file, 'r') as f:
                pattern = f.next()
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not pattern:
        print 'Please enter a pattern'
        exit()
    try:
        houses = visit_houses(pattern)
        print 'Houses Visited: %d' % len(set(houses))
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
