import argparse
from collections import defaultdict, namedtuple


Node = namedtuple('Node', ['city', 'distance'])


class Graph(object):
    def __init__(self):
        self.cities = defaultdict(list)
        self.routes = []

    def add_city(self, city1, city2, distance):
        self.cities[city1].append(Node(city2, distance))
        self.cities[city2].append(Node(city1, distance))

    def find_shortest_route(self):
        # DFS in nodes
        lengths = []
        for k in self.cities:
            route = [k]
            self.find_routes(route)
        for route in self.routes:
            lengths.append(self.find_length(route))
        return min(lengths)

    def find_longest_route(self):
        lengths = []
        for k in self.cities:
            route = [k]
            self.find_routes(route)
        for route in self.routes:
            lengths.append(self.find_length(route))
        return max(lengths)

    def find_routes(self, route):
        curr = route[-1]
        if len(route) == len(self.cities.keys()):
            self.routes.append(route)
            return
        for node in self.cities[curr]:
            if node.city not in route:
                new_route = route + [node.city]
                self.find_routes(new_route)

    def find_length(self, route):
        length = 0
        for i in range(len(route) - 1):
            curr = self.cities[route[i]]
            nex = route[i + 1]
            for j in curr:
                if nex == j.city:
                    length += j.distance
        return length


def main():
    parser = argparse.ArgumentParser(description='Solve the day 9 challenges for Advent of Code')
    parser.add_argument('string', help='The secret to use', nargs='?')
    parser.add_argument('-f', '--file', help='Read the pattern from a file instead of from the command line')
    args = parser.parse_args()
    string = args.string
    graph = Graph()

    if args.file:
        try:
            instructions = []
            with open(args.file, 'r') as f:
                for line in f:
                    instructions.append(line[:-1])

            for instruction in instructions:
                i = instruction.split(' ')
                graph.add_city(i[0], i[2], int(i[-1]))

            print graph.find_longest_route()
            exit()
        except IOError as err:
            print 'There was an error reading from disk: %s' % err.strerror
            exit()
    if not string:
        print 'Please enter a string'
        exit()
    try:
        res = parse(string)
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
