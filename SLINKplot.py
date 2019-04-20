
import matplotlib.pyplot as plt
import numpy as np
import sys
import re
#import Levenshtein
from itertools import chain, combinations
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster,fclusterdata
import time


infile = sys.argv[1] # input fasta file

thres = float(sys.argv[2]) # threshold to cut the dendrogram



def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram ')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata



def hamming(s1,s2):
	dif = 0
	for c1,c2 in zip(s1,s2):
		if c1 != c2:
			dif += 1

	return (dif)/float(len(s1))	

def getSquareForm(InputFile):
	Seqs=[]
	f= open(InputFile,'r')
	for line in f:
		
		if re.search('>', line):
			pass
		else:
			Seqs.append(line.strip())

	n = len(Seqs)
	# convert input sequences to pdist format that scipy takes 
	#(eg list(combinations(range(3),2)) = [(0, 1), (0, 2), (1, 2)])
	pdistL = [] 
	combList = list(combinations(range(n),2))
	for (x,y) in combList:
		distance = hamming(Seqs[x],Seqs[y])
		pdistL.append(float(distance))

	X = np.array(pdistL)
	Z = linkage(X, 'single')
	labelsOptimal = fcluster(Z, thres, criterion='distance')

	# labelsOptimal = fcluster(Z, thres, criterion='distance')
	# for i in labelsOptimal:
	# 	print i
	#labelsOptimal = fcluster(Z, k , criterion='maxclust')
	#fig = plt.figure(figsize=(25,10))

	# fancy_dendrogram(
 #    Z,
 #    truncate_mode='lastp',
 #    p=15,
 #    leaf_rotation=90.,
 #    leaf_font_size=1.,
 #    show_contracted=True,
 #    annotate_above=10,
 #    max_d=thres,  # plot a horizontal cut-off line
	# )
	# plt.show()
	#dn = dendrogram(Z)
	#plt.show()

def withDistMatrix(InputFile):
	Seqs=[]
	f= open(InputFile,'r')
	for line in f:
		
		if re.search('>', line):
			pass
		else:
			Seqs.append(line.strip())

	n = len(Seqs)

	my_array = np.zeros((n,n))
	
	for i, ele_1 in enumerate(Seqs):
	    for j, ele_2 in enumerate(Seqs):
	        if j >= i:
	            break # Since the matrix is symmetrical we don't need to
	                  # calculate everything
	        #difference = EditDistance(ele_1, ele_2) 
	        #difference = editDistDP(ele_1, ele_2,len(ele_1),len(ele_2)) 
	        difference = hamming(ele_1, ele_2) #/float(min(len(ele_1),len(ele_2)))
	        #my_array[i, j] = difference
	        my_array[j, i] = difference
	print my_array
	Z = linkage(my_array, 'single')
	labelsOptimal = fcluster(Z, thres, criterion='distance')
	print labelsOptimal

t1 = time.time()
#getSquareForm(infile)
withDistMatrix(infile)
t2 = time.time()

print "time", (t2-t1)
