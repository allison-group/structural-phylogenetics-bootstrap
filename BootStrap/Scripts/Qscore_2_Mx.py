#!/usr/bin/python

from __future__ import division
import math,os,sys
import numpy as np

taxa_ = []
id_ = []
vals_ = []
vals_c = []
num_ = []
cnt_ = 0

with open('Superpose.score','r') as f_in:
	for line in f_in:
		a = line.rsplit()
		id_ = np.append(id_,str(a[1])+'-'+str(a[2]))
		vals_ = np.append(vals_,a[3])
		vals_c = np.append(vals_c,float(a[3]))

# remove file if it exits
if os.path.isfile('tax.txt'):
   os.system('rm tax.txt')
if os.path.isfile('taxas.txt'):
   os.system('rm taxas.txt')

# populate list of PDBs
os.system('ls *.pdb >tax.txt')

x_ = open('tax.txt','r')
xx_ = open('taxas.txt','a')
for l_ in x_:
   l_ = l_.split('.')[0]
   xx_.write(str(l_) + '\n')
   
x_.close()
xx_.close()

l_in = open('taxas.txt')
for line in l_in:
   line = line[0:len(line)-1]
   taxa_ = np.append(taxa_,line)
l_in.close()
###########################################################
# Creating 2D matrix
m_ = [[0 for x in range(len(taxa_))] for x in range(len(taxa_))]
count = 0
for t_ in id_:
   m1_ = t_.split('-')[0]
   m2_ = t_.split('-')[1]
   row_ = np.where(taxa_ == m1_)[0][0]
   col_ = np.where(taxa_ == m2_)[0][0]
   m_[row_][col_] = 1 - vals_c[count] #**2/(num_[row_]*num_[col_])) 
   count = count + 1

############################################################
f = open('distance_.log','a')
for r_ in range(0,len(taxa_)):
   for c_ in range(0,len(taxa_)):
      f.write('{:8.4f}'.format(m_[r_][c_]))
   f.write('\n')
f.close()


