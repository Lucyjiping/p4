#!/usr/bin/env python3

import sys


def main():

	small = []
	big = []
	randomPkt = []

	if len(sys.argv)<2:
		print("please input file name\n")
		exit(1)

	f = open(sys.argv[1])
	for x in f:
		if "Small" in x:
			f.readline()
			f.readline()
			y = f.readline()
			z = y.split(":")
			z = z[1]
			z = z[:-2]
			z=float(z)
			small.append(z)

		if "Big" in x:
			f.readline()
			f.readline()
			y = f.readline()
			z = y.split(":")
			z = z[1]
			z = z[:-3]
			z=float(z)
			big.append(z)

		if "Random" in x:
			f.readline()
			f.readline()
			y = f.readline()
			z = y.split(":")
			z = z[1]
			z = z[:-3]
			z=float(z)
			randomPkt.append(z)

	f.close()

	print("Small packet correct classified ratio are:\n")	
	for i in range(len(small)-1):
		print('{}%'.format(small[i]), end=', ')
	print('{}%\n'.format(small[-1]))
	

	print("Big packet correct classified ratio are :\n")
	for i in range(len(big)-1):
		print('{}%'.format(big[i]), end=', ')
	print('{}%\n'.format(big[-1]))


	print("Random packet wrongly classified ratio are: \n")
	for i in range(len(randomPkt)-1):
		print('{}%'.format(randomPkt[i]), end=', ')
	print('{}%\n'.format(randomPkt[-1]))

	print("Small packet average correctly classified ratio: {:.2f}% \n".format(sum(small)/len(small)) )

	print("Big packet average correctly classified ratio: {:.2f}%\n".format(sum(big)/len(big)) )

	print("Random packet average wrongly classified ratio: {:.2f}%\n".format(sum(randomPkt)/len(randomPkt)) )


if __name__ == '__main__':
	main()
	

