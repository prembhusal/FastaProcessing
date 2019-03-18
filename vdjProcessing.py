import sys
from collections import Counter
import pandas as pd
import numpy as np
import csv

infile = sys.argv[1]


def getVJid():
	#process the v,j column and assign unique id for each v,j column;
	#consider first value if v,j column has multiple value
	data = pd.read_csv(infile)

	#keep only the first value from v and j column
	data["V_CALL"] = data["V_CALL"].str.split(",").str[0]
	data["J_CALL"] = data["J_CALL"].str.split(",").str[0]

	#assign unique id for unique v,j gene
	data["V_CALL"] = data.groupby("V_CALL").ngroup()
	data["J_CALL"] = data.groupby("J_CALL").ngroup()

	print data["V_CALL"]
	

def sampleGroups():
	#data = getVJid()
	data = pd.read_csv(infile,sep="\t")
	#print data["V_CALL"]
	size = int(sys.argv[2])
	#sample from the data for given size
	n = 10
	biggestG = []
	#sample n times;
	for i in range(n):

		sampledf = data.sample(n=size,replace=False)
		#mytable = data.groupby(["V-GENE and allele","J-GENE and allele","JUNCTION-nt nb"]).size().reset_index()
		mytable = sampledf.groupby(["V_CALL","J_CALL","JUNCTION_LENGTH"]).size().reset_index() # unique combination of col-10,col-11 , col-13
		listTable = list(zip(*[mytable[c].values.tolist() for c in mytable]))
		sortedL =  sorted(listTable, key= lambda x:x[3], reverse=True) # sort the list based on group count
		biggestG.append(int(sortedL[0][3]))

	#print "tota groups :", len(sortedL)
	print "biggest group: ",biggestG
	print "mean:", np.mean(biggestG)
	print "std :", np.std(biggestG)
def main():
	getVJid()
if __name__ == '__main__':
	main()
