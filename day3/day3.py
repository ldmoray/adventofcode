import argparse


def visit_houses(pattern, santas):
    which = 0
    curr = (0,0)
    houses = [[curr] for i in range(santas)]
    for char in pattern:
        which_houses = houses[which]
        curr = which_houses[-1]
        if char == '^':
            curr = (curr[0] + 1, curr[1])
            which_houses.append(curr)
        elif char == 'v':
            curr = (curr[0] - 1, curr[1])
            which_houses.append(curr)
        elif char == '>':
            curr = (curr[0], curr[1] + 1)
            which_houses.append(curr)
        elif char == '<':
            curr = (curr[0], curr[1] - 1)
            which_houses.append(curr)
        elif char != '\n':
            raise ValueError('Invalid instruction for Santa')
        which = (which + 1) % santas
    houses = [house for subhouses in houses for house in subhouses]
    return houses

def main():
    parser = argparse.ArgumentParser(description='Solve the day 3 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern of directiosn to solve', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    parser.add_argument('-s', '--santas', help='The number of santas reading the instructions', default=1)
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
        santas = int(args.santas)
        houses = visit_houses(pattern, santas)
        print 'Houses Visited: %d' % len(set(houses))
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
