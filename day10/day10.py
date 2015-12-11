import argparse


def look_and_say(string):
    string = list(string)
    res = []
    curr = string[0]
    count = 0
    for c in string:
        if c == curr:
            count += 1
        else:
            res.append(str(count))
            res.append(curr)
            curr = c
            count = 1

    res.append(str(count))
    res.append(curr)
    string = ''.join(res)
    return string



def main():
    parser = argparse.ArgumentParser(description='Solve the day 10 challenges for Advent of Code')
    parser.add_argument('string', help='Initial string', nargs='?')
    args = parser.parse_args()

    string = args.string
    try:
        for i in range(40):
            string = look_and_say(string)

        print len(string)
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
