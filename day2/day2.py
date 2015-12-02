import argparse


def split_pattern(pattern):
    pattern = pattern.split('x')
    return [int(x) for x in pattern]


def ribbon_length(length, width, height):
    front = 2 * (length + width)
    side = 2 * (width + height)
    top = 2 * (length + height)
    return min(front, side, top) + length * width * height


def slack_surface_area(length, width, height):
    front_a = length * width
    side_a = width * height
    top_a = length * height
    return 2 * front_a + 2 * side_a + 2 * top_a + min(front_a, side_a, top_a)


def main():
    parser = argparse.ArgumentParser(description='Solve the day 2 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern that represents the shape of a box to solve', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read patterns from a file instead of from the command line')
    parser.add_argument('-r', '--ribbon', help='Find the amount of ribbon to order.', action='store_true')
    args = parser.parse_args()

    if args.ribbon:
        length = 0
        if args.file:
            try:
                with open(args.file, 'r') as f:
                    for pattern in f:
                        dimensions = split_pattern(pattern)
                        length += ribbon_length(*dimensions)
                print 'Total Length of Ribbon is %d' % length
            except IOError as err:
                print 'There was an error reading from disk: %s' % err.strerror
                exit()
        elif args.pattern:
            try:
                dimensions = split_pattern(args.pattern)
                length = ribbon_length(*dimensions)
                print 'Total Length of Ribbon is %d' % length
            except ValueError as err:
                print str(err)
        else:
            print 'Please enter a pattern'
    else:
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
