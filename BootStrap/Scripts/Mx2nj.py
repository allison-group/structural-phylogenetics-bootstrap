#!/usr/bin/python
import os
import numpy as np
import Bio
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, _DistanceMatrix

path_ = os.path.dirname(os.path.realpath(__file__))
path_break = path_.split('/')
dir_ = path_break[len(path_break)-1]
####################################################################################################################
# Creat NEX file
l_in = open('taxas.txt')
taxa_ = []
for line in l_in:
   line = line[0:len(line)-1]
   taxa_ = np.append(taxa_,line)

l_in.close()

f_ = open(dir_ + '.p1.nex','a')
nn_ = open('temp.ann.taxa','a')
f_.write('#nexus\nBEGIN taxa;\nDIMENSIONS ntax=' + str(len(taxa_)) + ';\nTAXLABELS\n')
count = 0 
for taxas_ in taxa_:
   count = count + 1
   f_.write('[' + str(count) + ']' + taxas_ + '\n')
   nn_.write('[' + str(count) + ']' + taxas_ + '\n')

f_.write(';\nEND [taxa];\nBEGIN distances;\nDIMENSIONS ntax=' + str(len(taxa_)) + ';\nFORMAT labels diagonal triangle=both;\nMATRIX\n')

g_ = open('distance_.log','r')
count2 = 0
for lines in g_:
   count2 = count2 + 1
   lines = lines.rstrip()
   f_.write('[' + str(count2) + ']' + taxa_[count2-1] + '\t' + lines +'\n')

f_.write(';\nEND [distances];')

g_.close()
f_.close()
nn_.close()
############################################################################################################################
t_ = open('taxas.txt')
taxas_ = []

for line in t_:
   taxas_.append((line.rsplit()[0]))

t_.close()

dist_ = np.genfromtxt('distance_.log')
dist1_ = np.tril(dist_)
# Make list of lists

dist2_ = []
for x in range(0,np.shape(dist1_)[0]):
   dist2_.append(list(dist1_[x][0:x+1]))
mm_ = _DistanceMatrix(taxas_,dist2_)
root_ = DistanceTreeConstructor()
tree = root_.nj(mm_) 

path_ = os.path.dirname(os.path.realpath(__file__))
path_break = path_.split('/')
dir_ = path_break[len(path_break)-1]
Phylo.write(tree,str(dir_)+'.nex','newick')
############################################################################################################################
g_ = open('final.nex.tree','a')
with open(dir_ + '.p1.nex','r') as f_:
	for line in f_:
		g_.write(line)
g_.write('\nBEGIN TREES;\nTREE tree1 =')
with open(dir_ + '.nex','r') as f_:
	for line in f_:
		g_.write(line)
g_.write('END;')
g_.close()

os.system('rm *.nex')
