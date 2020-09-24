#!/usr/bin/env python3

import sys

small_one = 0;
small_zero = 0;
big_one = 0;
big_zero = 0;
random_one = 0;
random_zero = 0;



def main():

	global small_one;
	global small_zero;
	global big_one;
	global big_zero;
	global random_one;
	global random_zero;



	if len(sys.argv)<2:
		print("please input file name\n")
		exit(1)

	f = open(sys.argv[1])
	for x in f:
		y = f.readline()
		if("hello" in y):
			if("0x1" in x):
				small_one = small_one + 1
			elif("0x0" in x):
				small_zero = small_zero +1

		elif("big" in y):
			if("0x3" in x):
				big_one = big_one + 1
			elif("0x0" in x):
				big_zero = big_zero + 1
		elif("greet" in y):
			if("0x0" in x):
				random_zero = random_zero + 1
			elif("0x1" in x):
				random_one = random_one + 1
	f.close()

def print_f():
	global small_one;
	global small_zero;
	global big_one;
	global big_zero;
	global random_one;
	global random_zero;

	total_small = small_one + small_zero
	total_big = big_one + big_zero
	total_random = random_one + random_zero

	small = "Small packets: \n	Total packet number:  {} \n	Correctly classified packet number: {}\n	Correct classified ratio: {:.2f}%\n"

	print(small.format(total_small, small_one, small_one/total_small * 100));

	big = "Big packets:\n	Total packet number:  {}\n	Correctly classified packet number: {}\n	Correct classified ratio: {:.2f}% \n"

	print(big.format(total_big, big_one, big_one/total_big * 100));

	random_msg = "Random packets:\n	Total packet number:  {}\n	Wrongly classified packet number: {}\n	Wrongly classified ratio: {:.2f}% \n\n"

	if(total_random != 0):
		print(random_msg.format(total_random, random_one, random_one/total_random * 100));



if __name__ == '__main__':
	main()
	print_f()
	

