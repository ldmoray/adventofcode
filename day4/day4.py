import argparse
import hashlib
from multiprocessing import Pool


class AdventCoin(object):
    def __init__(self, secret, prefix):
        self.secret = secret
        self.prefix = prefix

    def __call__(self, num):
        res = 0
        hashed = hashlib.md5(self.secret + str(num)).hexdigest()[:len(self.prefix)]
        if hashed == self.prefix:
            res = num
        return res



def main():
    parser = argparse.ArgumentParser(description='Solve the day 4 challenges for Advent of Code')
    parser.add_argument('secret', help='The secret to use', nargs='?')
    parser.add_argument('prefix', help='The prefix to find', nargs='?')
    args = parser.parse_args()

    try:
        pool = Pool()
        a = 0
        n = 0
        step = 800000
        coin = AdventCoin(args.secret, args.prefix)
        while not a:
            for i in pool.imap_unordered(coin, range(n, n+step), chunksize=1000):
                a = i
                if a:
                    pool.terminate()
                    break
            n = n + step
        print "The smallest positive integer is %d" % a
    except ValueError as err:
        print str(err)


if __name__ == '__main__':
    main()
