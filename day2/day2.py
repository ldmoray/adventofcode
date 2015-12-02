import argparse


def split_pattern(pattern):
    pattern = pattern.split('x')
    return [int(x) for x in pattern]


def slack_surface_area(length, width, height):
    front = length * width
    side = width * height
    top = length * height
    slack = min(front, side, top)
    area = 2 * front + 2 * side + 2 * top
    total = area + slack
    return total


def main():
    parser = argparse.ArgumentParser(description='Solve the day 2 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern that represents the shape of a box to solve', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read patterns from a file instead of from the command line')
    args = parser.parse_args()

    area = 0
    if args.file:
        try:
            with open(args.file, 'r') as f:
                for pattern in f:
                    dimensions = split_pattern(pattern)
                    area += slack_surface_area(*dimensions)
            print 'Total Area with slack is %d' % area
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    elif args.pattern:
        try:
            dimensions = split_pattern(args.pattern)
            area = slack_surface_area(*dimensions)
            print 'Total Area with slack is %d' % area
        except ValueError as err:
            print str(err)
    else:
        print 'Please enter a pattern'


if __name__ == '__main__':
    main()
