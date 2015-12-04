import argparse
import hashlib
from multiprocessing import Pool


class AdventCoin(object):
    def __init__(self, secret, prefix):
        self.secret = secret
        self.prefix = prefix

    def __call__(self, num):
        res = 0
        hashed = hashlib.md5(self.secret + str(num)).hexdigest()
        if hashed.startswith(self.prefix):
            res = num
        return res


def find_smallest_int(secret, prefix, step=800000):
    pool = Pool()
    answer = 0
    n = 0
    coin = AdventCoin(secret, prefix)
    while not answer:
        for i in pool.imap_unordered(coin, range(n, n+step), chunksize=1000):
            answer = i
            if answer:
                pool.terminate()
                break
        n = n + step
    return answer


def main():
    parser = argparse.ArgumentParser(description='Solve the day 4 challenges for Advent of Code')
    parser.add_argument('secret', help='The secret to use', nargs='?')
    parser.add_argument('prefix', help='The prefix to find', nargs='?')
    args = parser.parse_args()

    try:
        a = find_smallest_int(args.secret, args.prefix)
        print "The smallest positive integer is %d" % a
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
