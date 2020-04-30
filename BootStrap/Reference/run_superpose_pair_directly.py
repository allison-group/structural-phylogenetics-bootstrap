#!/usr/bin/python

# This will generate pairs of PDB for Superpose 
# It will also run them on the fly or submit as threads
# for number of comparisons exceeding 1000 its suitable to thread it

import numpy as np
import os,sys
import glob
from tqdm import tqdm
import multiprocessing

n_cores = multiprocessing.cpu_count()
use_cores = n_cores - 1


a = glob.glob('*.pdb')
n = len(a)**2
per_file = np.ceil(n/use_cores)
to_large = -1

if n <= 3000:
	#print "Running on the go"
	for m0 in a:
		for m1 in a:
			os.system('superpose ' + m0 + ' ' + m1 + ' > ' + m0.split('.')[0] + '-' + m1.split('.')[0] + '.q')
else:
	c = 0
	d = 0
	to_large = 1
	print "Large :: writting out"
	for m0 in tqdm(a):
		for m1 in a:
			if c == per_file:
				d += 1
				c = 0
			with open('list.submit.'+str(d),'a') as f:
				f.write('superpose ' + m0 + ' ' + m1 + ' > ' + m0.split('.')[0] + '-' + m1.split('.')[0] + '.q\n')
			c += 1
if to_large == 1:
	print "Submitting threads"
	a = glob.glob('list.submit.*')
	for mem in tqdm(a):
		os.system('chmod +x '+ mem)
		os.system('./'+mem+' &')
