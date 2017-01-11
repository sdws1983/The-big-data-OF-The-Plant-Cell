#!/usr/bin/env python2.7

import sys, getopt
import time

def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
	input_file = ""
	output_file = ""
	h = ""
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			h = 'useages:'
	return input_file,output_file,h

def main(input_file, output_file):
	with open (input_file) as f:
		for i in f:
			if i[0] == ">":
				pass
			else:
				num = i.split("\t")[0]
				ff = open(("sort-address-" + str(num)), 'a')
				ff.write(i.split("\t")[1])
				ff.close()
	
if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
