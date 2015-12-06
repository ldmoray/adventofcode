import argparse
import hashlib
from multiprocessing import Pool

grid = [ [0 for i in range(1000)] for i in range(1000) ]


def toggle(start, end):
    startx = int(start[0])
    starty = int(start[1])
    endx = int(end[0])
    endy = int(end[1])
    for i in range((endx - startx) + 1):
        for j in range((endy - starty) + 1):
            grid[startx + i][starty + j] = grid[startx + i][starty + j] + 2
    return


def off(start, end):
    startx = int(start[0])
    starty = int(start[1])
    endx = int(end[0])
    endy = int(end[1])
    for i in range((endx - startx) + 1):
        for j in range((endy - starty) + 1):
            if grid[startx + i][starty + j]:
                grid[startx + i][starty + j] = grid[startx + i][starty + j] - 1
    return


def on(start, end):
    startx = int(start[0])
    starty = int(start[1])
    endx = int(end[0])
    endy = int(end[1])
    for i in range((endx - startx) + 1):
        for j in range((endy - starty) + 1):
            grid[startx + i][starty + j] = grid[startx + i][starty + j] + 1
    return


def foo(string):
    strategy = ''
    x = string.split(' ')
    if x[0] == 'toggle':
        strategy = toggle
    else:
        x = x[1:]
        if x[0] == 'off':
            strategy = off
        else:
            strategy = on
    start = x[1].split(',')
    end = x[-1].split(',')
    strategy(start, end)
    return


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
                foo(instruction)

            lights = [i for s in grid for i in s]
            print sum(lights)
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
