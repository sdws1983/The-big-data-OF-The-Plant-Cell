#!/usr/bin/env python

import sys, getopt
import re
import time
import pandas as pd
import os

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
			h = 'useages:\nremove the sequence which contain "N"\n-i : inputfile\n-o : outputfile\n'
	return input_file,output_file,h

def main(input_file, output_file):
	all = []
	
	with open (input_file) as f:
		for i in f:
			i = i.split(", ")
			i = i[:-2]

#			i = i[-1:]#  country

			for each in i:
				each = re.sub(r'\n', ' ', str(each))
				each = re.sub(r'\d', ' ', str(each))

#				each = re.sub(r'-', ' ', str(each))#  country

				each = re.sub(r'\s+$', ' ', str(each))
####################
# University, etc. #
####################
				if u'Department' in each or u'College' in each or u'School' in each or u'Institut' in each or u'Laborato'.lower() in each.lower():
					pass
				else:	
					all.append(each)
				

	tag_all = {}
	for each in all:
		if each not in tag_all.keys():
			tag_all[each] = 1
		else:
			tag_all[each] += 1

	#print (tag_all)
	fou = open('tmp.txt', 'w')
	
	t = []
	for (k,v) in tag_all.items():
		t.append(k)
		tab =  str(k) + '\t' + str(v) + '\n'
		fou.write(str(tab))
	fou.close()
	#print (t)

	data = pd.DataFrame(pd.read_table('tmp.txt', names = ['a','b']))
	data = data.sort(['b'],axis = 0, ascending = False)
	data.to_csv(output_file, sep='\t')
	os.popen('rm tmp.txt')

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
