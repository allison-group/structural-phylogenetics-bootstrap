#!/usr/bin/python

import os,sys,glob,subprocess
import numpy as np
from tqdm import tqdm 

# Hold all gromacs trajectory and structure files in folder and provide path below
dPath = 'path_to_data_DIR/'

# hold all PDB IDs in a file called list.dir

d_= np.genfromtxt('list.dir',dtype=str)

for i in tqdm(d_):
	gro =  dPath + i + '.gro'
	xtc =  dPath + i + '.xtc'
	os.system('vmd -dispdev text -eofexit -args < get_RMSD.tcl ' + gro + ' ' + xtc + ' ' + i + ' > /dev/null 2>&1')

