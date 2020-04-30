#!/usr/bin/python 

import os,sys,glob
from tqdm import tqdm
import numpy as np


# Enter folder with Trajectories
path = os.getcwd()
p1 = path + '/Trajectories'
os.chdir(p1)
# Enumerate Taxa
d_ = glob.glob('*.gro')
e_ = glob.glob('*.xtc')
if len(d_) != len(e_):
	raise ValueError('Mismatch between structures and topologies. This condition should not happen.')
# Create N_trials number of folders
N_trials = 100
dir_trial = np.arange(0,100,1)
# Creating Analysis directory for easy hand-ling
os.system('mkdir Trials')
p2 = path + '/Trajectories/Trials'
os.chdir(p2)
# Make trial folders
for folders in dir_trial:
	os.system('mkdir trial_' + str(folders))
	os.system('cp ../../Scripts/* trial_'+str(folders))
# Generate list of random numbers for each trajectory and save them
# Access each trajectory 
# For each random number in saved file
for traj in d_:
	frame_sel = np.random.randint(0,10000,N_trials) # Generates N_trials numbers to get a frame per trial
	with open(p2 + '/' + traj.split('.')[0]+'.vals','a') as f:
		for val_ in frame_sel:
			f.write(str(val_) + '\n')
# save frame to trial folder
# TCL
os.chdir(path)
os.system('vmd -dispdev text -eofexit < BS_slave.tcl ')
