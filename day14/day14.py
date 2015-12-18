import argparse


class Reindeer(object):
    def __init__(self, name, speed, sprint_time, rest_time):
        self.name = name
        self.speed = speed
        self.sprint_time = sprint_time
        self.rest_time = rest_time
        self.distance = 0
        self.resting = False
        self.time = 0
        self.points = 0

    def tick(self):
        if self.resting:
            if self.time == self.rest_time - 1:
                self.time = 0
                self.resting = False
            else:
                self.time += 1
        else:
            self.distance += self.speed
            if self.time == self.sprint_time - 1:
                self.time = 0
                self.resting = True
            else:
                self.time += 1


def parse_reindeer(line):
    line = line.split(' ')
    name = line[0]
    speed = int(line[3])
    sprint = int(line[6])
    rest = int(line[-2])
    return Reindeer(name, speed, sprint, rest)


def tick(race):
    for r in race:
        r.tick()
    race.sort(key=lambda r: r.distance, reverse=True)
    race[0].points += 1


def main():
    parser = argparse.ArgumentParser(description='Solve the day 14 challenges for Advent of Code')
    parser.add_argument('time', help='The seconds to race', nargs='?', type=int)
    parser.add_argument('file', help='The files to read the rules from', nargs='?')
    args = parser.parse_args()
    rules = []
    rules2 = []
    try:
        with open(args.file, 'r') as f:
            for line in f:
                rules.append(parse_reindeer(line))
                rules2.append(parse_reindeer(line))
    except IOError as err:
        print 'There was an error reading from disk: %s' % err.strerror
        exit()
    for i in range(args.time):
        tick(rules)
    a =[r.speed*r.sprint_time*(args.time/(r.sprint_time + r.rest_time)) + r.speed*min(r.sprint_time, args.time % (r.sprint_time + r.rest_time)) for r in rules2]
    a.sort(reverse=True)
    print a
    print [r.distance for r in rules]
    print max([r.points for r in rules]) + 1



if __name__ == '__main__':
    main()
