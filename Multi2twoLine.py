#this program converts multi line fasta to single line
import sys
from Bio import SeqIO

infile = open(sys.argv[1])
outfile = open(sys.argv[2],"w+")

for record in SeqIO.parse(infile,"fasta"):
	sequence = str(record.seq)
	outfile.write('>'+record.id+"\n"+sequence+"\n")
