import argparse
import json

def has_red(obj):
    for k in obj:
        if obj[k] == 'red':
            return True
    return False

def strip_numbers(obj):
    res = []
    if isinstance(obj, dict):
        if not has_red(obj):
            for k in obj:
                res.extend(strip_numbers(obj[k]))
    elif isinstance(obj, list):
        for i in obj:
            res.extend(strip_numbers(i))
    elif isinstance(obj, (int, long)):
        res.append(obj)
    return res



def main():
    parser = argparse.ArgumentParser(description='Solve the day 12 challenges for Advent of Code')
    parser.add_argument('string', help='The secret to use', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    args = parser.parse_args()
    string = ''
    if args.file:
        try:
           with open(args.file, 'r') as f:
                string = json.load(f)
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not args.string and not string:
        print 'Please enter a string'
        exit()
    elif not string:
        string = json.loads(args.string)
    try:
        print sum(strip_numbers(string))
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
