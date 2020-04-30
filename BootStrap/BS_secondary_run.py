#!/usr/bin/python 

from __future__ import division
import os,sys,glob
from tqdm import tqdm
import numpy as np
import multiprocessing



# Enter folder with Trajectories
path = os.getcwd()
p1 = path + '/Trajectories/Trials/' 
os.chdir(p1)
dirs_ = glob.glob('trial_*')
jobs = len(dirs_)
# >> get num of cores from python multiprocessing library
cores = multiprocessing.cpu_count()
# >> spare 1 core for youtubing
usable_cores = cores - 1
per_file = np.ceil(jobs/usable_cores)
# Creating command structure
l_cnt = 0
f_index = 0
os.chdir(path)
for trial in dirs_:
	if l_cnt == per_file:
		f_index += 1
		l_cnt = 0
	with open('submit_set' + str(l_cnt) + '.sh','a') as f:
		f.write('cd ' + p1 + trial + '\n')
		f.write('./run_superpose_pair_directly.py\n') # >> generate pairwise Q-score comparison for all Taxa in trial
		f.write('./qPairs2list.py\n') # >> 53 x 53 = number of files generated :: Parse files and save results in list
		f.write('./Qscore_2_Mx.py\n') # >> convert list to Matrix 
		f.write('./Mx2nj.py\n') # >> Generte tree from matrix
	os.system('chmod +x submit_set' + str(l_cnt) + '.sh')
	l_cnt += 1
# Collate trees from each folder
# Sum trees to add statistics to tree from starting structures.
# Visualise and improve
