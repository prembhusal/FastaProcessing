import sys
from sklearn.metrics.cluster import normalized_mutual_info_score

'''

compute the NMI score

usage: python eval.py true_label_file predicted_label_file
'''

label_true = open(sys.argv[1])
label_pred = open(sys.argv[2])

tlabel = [ int(t) for t in label_true]
plabel = [ int(t) for t in label_pred]


print normalized_mutual_info_score(tlabel, plabel)
