import argparse
import hashlib
from multiprocessing import Pool

def foo(i):
    a = hashlib.md5('yzbqklnj' + str(i)).hexdigest()
    if a[0:6] == '000000':
        return i
    return 0


def main():
    parser = argparse.ArgumentParser(description='Solve the day 4 challenges for Advent of Code')
    parser.add_argument('pattern', help='The pattern of parentheses to solve', default='', nargs='?')
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
        pool = Pool()
        a = 0
        n = 0
        step = 1000000
        while not a:
            for i in pool.imap_unordered(foo, range(n, n+step), chunksize=10000):
                a = i
                if a:
                    print a
                    pool.terminate()
                    break
            n = n + step
            print "next step %d" % n
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
