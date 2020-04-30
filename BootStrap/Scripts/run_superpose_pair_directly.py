#!/usr/bin/python 
# This will generate pairs of PDB for Superpose 

import numpy as np
import os,sys
import glob


a = glob.glob('*.pdb')

for m0 in a:
	for m1 in a:
		os.system('superpose ' + m0 + ' ' + m1 + ' > ' + m0.split('.')[0] + '-' + m1.split('.')[0] + '.q')

