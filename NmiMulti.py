import sys
from sklearn.metrics.cluster import normalized_mutual_info_score
import numpy as np
l = []
for j in range(10):

        f1 = open("locMst"+str(j))
        f2 = open("sctCent"+str(j)+"L-1")
        f1lab = [int(i) for i in f1]
        f2lab = [int(i) for i in f2]
        l.append(normalized_mutual_info_score(f1lab, f2lab))

print l
print "mean",np.mean(l)
print "std",np.std(l) 
