#!/usr/bin/python 

import os,sys,glob
import numpy as np

# %5d%-5s%5s%5d%8.3f%8.3f%8.3f%8.4f%8.4f%8.4f

#content_ = np.genfromtxt('protein-water-hollow.gro',dtype=None,encoding='utf-8',delimiter=[5,5,5,5,8,8,8,8,8,8],skip_header=2,skip_footer=1)
#print content_

cnt = 0
t_l = 0
g = open('protein-water-hollow-mod.gro','a')
with open('protein-water-hollow.gro') as f:
	for line in f:
		l_ = line.split('\n')[0]
		cnt += 1
		if cnt == 2:
			t_l = int(l_) + 3 
		if cnt < t_l and cnt > 2:
			if cnt < 100000:
				g.write("{:>5}{:<5}{:>5}{:>5}{:>8.3f}{:>8.3f}{:>8.3f}\n".format(l_[0:5],l_[5:10],l_[10:15].strip(),l_[15:20],float(l_[20:28]),float(l_[28:36]),float(l_[36:44]),l_[44:52],l_[52:60],l_[60:68]))
			else:
				g.write("{:>5}{:<5}{:>5}{:>5}{:>8.3f}{:>8.3f}{:>8.3f}\n".format(l_[0:5],l_[5:10],l_[10:15].strip(),int(l_[15:21])-100000,float(l_[21:29]),float(l_[29:37]),float(l_[37:45]),l_[45:53],l_[53:61],l_[61:69]))

g.close()

os.system('head -2 protein-water-hollow.gro > h.l')
os.system('tail -1 protein-water-hollow.gro > t.l')
os.system('cat h.l protein-water-hollow-mod.gro t.l > protein-water-hollow-mod2.gro')
os.system('mv protein-water-hollow-mod2.gro protein-water-hollow-mod.gro')
os.system('rm h.l t.l')
