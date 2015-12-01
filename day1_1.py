def main():
	# load input from file
	floor = 0
	with open('day1_1.txt', 'r') as f:
		line = f.next()
		for char in line:
			if char == '(':
				floor += 1
			elif char == ')':
				floor -= 1
		print "floor %d" % floor


if __name__ == '__main__':
	main()
