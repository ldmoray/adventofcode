import argparse


def count_parens(string):
	count = 0
	for char in string:
		if char == '(':
			count += 1
		elif char == ')':
			count -= 1
		elif char != '\n':
			raise ValueError('Invalid Character in Pattern: %s' % char)
	return count


def main():
	parser = argparse.ArgumentParser(description='Solve the day 1 challenges for Advent of Code')
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
	try:
		floor_count = count_parens(pattern)
		print 'Floor: %d' % floor_count
	except ValueError as err:
		print str(err)


if __name__ == '__main__':
	main()
