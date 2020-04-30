#!/usr/bin/python

import os

os.system('./run_superpose_pair_directly.py')
os.system('./qPairs2list.py')
os.system('./Qscore_2_Mx.py')
os.system('./Mx2nj.py')

# If everything works - a file should be created called
# final.nex.tree holding the tree string

