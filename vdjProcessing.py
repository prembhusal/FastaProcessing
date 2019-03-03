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
	
def main():
	getVJid()
if __name__ == '__main__':
	main()
