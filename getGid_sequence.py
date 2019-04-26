
import sys

# program to generate groupid based on common v-gene,j-gene and junction length
# Generate (gid, sequence)
# sequence = index, seqId, Junction
infile = sys.argv[1] # input dataset file

outfile = sys.argv[2] # name for output file

def getGroupIdSequence():
	data = pd.read_csv(infile,sep='\t')

	# #keep only the first value from v and j column
	data["V_CALL"] = data["V_CALL"].str.split(",").str[0]
	data["J_CALL"] = data["J_CALL"].str.split(",").str[0]
	data['Index'] = data.index
	data["Sequence"] = data["Index"].astype(str)+","+data["SEQUENCE_ID"].astype(str)+","+data["JUNCTION"].astype(str)
	data["groupId"] = data.groupby(["V_CALL","J_CALL","JUNCTION_LENGTH"]).grouper.group_info[0]

	data1 = data[["groupId","Sequence"]]
	data1.to_csv(outfile+".tsv", sep='\t',index=False)



def getGroupIdSequence2():
	data = pd.read_csv(infile,sep='\t')
	print data["Index"]
	data["Sequence"] = data["Index"].astype(str)+","+data["ID"].astype(str)+","+data["JUNCTION"].astype(str)
	data["groupId"] = data.groupby(["V_CALL","J_CALL","JUNCTION_LENGTH"]).grouper.group_info[0]

	data1 = data[["groupId","Sequence"]]
	data1.to_csv(outfile+".tsv", sep='\t',index=False)


getGroupIdSequence2()
