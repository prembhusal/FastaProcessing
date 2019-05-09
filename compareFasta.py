
import sys
  
file1 = sys.argv[1] #first input file
file2 = sys.argv[2] #second input file

#read the fasta file and make dictionary of (contig,sequence)
def getContigSequenceMap(inputFile):
        d = {}
        tempContig =''
        for line in open(inputFile):
                line = line.strip()
                if line.startswith(">"):
                        tempContig = line[1:]
                        d[tempContig] =[]
                else:
                        d[tempContig].append(line)

        for contig in d:
                d[contig] =''.join(d[contig])

        return d

d1 =getContigSequenceMap(file1) # dictionary for file1
l1 = [x for x in d1] # list of contigs for file1


d2 = getContigSequenceMap(file2) # dictionary for file2
l2 = [x for x in d2] # list of contigs for file2

#check from file1 whether the similar contig is in file2
for contig in l1:
        if contig in d2.keys():
                if d1[contig].lower()==d2[contig].lower():
                        print contig, " :Same "
                else :
                        print contig, " :Different"
        else:
                print contig, ":missing in " , file2

#check form file2 if similar contig is in file1
for contig in l2:
        if contig in d1.keys():
                if d1[contig].lower()==d2[contig].lower():
                        print contig, " :Same "
                else :
                        print contig, " :Different"
        else:
                print contig, ":missing in " , file1
