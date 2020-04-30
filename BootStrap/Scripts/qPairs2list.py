#!/usr/bin/python

import numpy as np
import os,sys,glob
from tqdm import tqdm

###########################
list_ = glob.glob('*.q')
g_ = open('Superpose.score','a')
for mem in list_:
	###########################
	# Superpose output parser
	###########################
	align_start = 0
	align_end = 0
	align_section = 0
	nl = 0
	q_score = -1
	align_len = -1
	rmsd = -1
	with open(mem,'r') as f_:
		for line in f_:
			line1 = line.rsplit()
			if len(line1) == 6 and line1[0] == 'quality' and line1[1] == 'Q:':
				q_score = float(line1[2])
			if len(line1) == 3 and line1[0] == 'r.m.s.d:':
				rmsd = float(line1[1])
			if len(line1) == 3 and line1[0] == 'Nalign:':
				align_len = line1[1]
			################################################################################
			# Setting up flags to control next iteration
			################################################################################
			if align_section == 1 and align_end == 0:
				if len(line1) > 0 and nl == 1:
					align_start = 1
					align_end = 0
					nl = 0
				if len(line1) > 0 and line1[0] == '|-------------+----------+-------------|':
					nl = 1
			if len(line1) == 4:
				if line1[0] == '$TEXT:Residue' and line1[1] == 'alignment:' and line1[2] ==  '$$' and line1[3] ==  '$$':
					align_section = 1
			if align_section == 1 and len(line1) == 1:
				if line1[0] == "`-------------'----------'-------------'":
					align_end = 1
					align_start = 0
			################################################################################
			#if align_start == 1 and align_end == 0:
			#	print line
			################################################################################

	if q_score == -1:
		q_score = 0
		align_len = 0
	g_.write('{:>4} {:>7} {:>7} {:>5} {:>5} {:>5}\n'.format('#S#',mem.split('-')[0].split('.')[0],mem.split('-')[1].split('.')[0],round(q_score,3),round(rmsd,3),align_len))
	os.system('rm ' + mem)
g_.close()
