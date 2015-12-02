import argparse


def increment_floor(char):
    result = 0
    if char == '(':
        result = 1
    elif char == ')':
        result = -1
    elif char != '\n':
        raise ValueError('Invalid Character in Pattern: %s' % char)
    return result


def first_entry(string, target):
    # load input from file
    current_floor = 0
    count = 0
    for char in string:
        current_floor += increment_floor(char)
        count += 1
        if current_floor == target:
            break
    else:
        raise ValueError('Target not Entered in Pattern')
    return count


def count_parens(string):
    count = 0
    for char in string:
        count += increment_floor(char)
    return count


def main():
    parser = argparse.ArgumentParser(description='Solve the day 1 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern of parentheses to solve', default='', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    parser.add_argument('-t', '--target', help='Find the first character instance when this floor is entered in the pattern', default='')
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
        if(args.target):
            entry = first_entry(pattern, int(args.target))
            print 'Target entered at %d' % entry
        else:
            floor_count = count_parens(pattern)
            print 'Floor: %d' % floor_count
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
