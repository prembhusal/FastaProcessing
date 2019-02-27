import sys
import random
f =open( sys.argv[1])
n = int(sys.argv[2])
l =[]
for line in f:
	line = line.strip()
	if line.find(">")==-1:
		l.append(line)
	else:
		pass

#print l
#random.shuffle(l)
#print l
count = 0
for i in range(n):
	print ">seq"+str(count)
	print l[i]
	count+=1
