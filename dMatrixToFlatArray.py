#this program converts the pairwise distance matrix(D) to flat array consisting of upper triangular of D;
#also has scipy.squareform to do same thing

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
	        my_array[i, j] = difference
	        my_array[j, i] = difference
	        
	#get upper triangular in flat array
	m = my_array.shape[0]
	r = np.arange(m)
	mask = r[:,None] < r
	distArr = my_array[mask]
  
  
  distArray = ssd.squareform(my_array)
	print "from masking: "
	print distArr

	print "by squareform :"
	print distArray


	Z = linkage(distArr, 'single')
	fig = plt.figure(figsize=(25,10))
	dn = dendrogram(Z)
	plt.show()
	labelsOptimal = fcluster(Z, thres, criterion='distance')
	print labelsOptimal
