def randomGen():
	l = ["A","C","T","G"]
	for i in range(64000):
		string =""
		for j in range(70):
			random.shuffle(l)
			string += l[0]
		print ">seq"+str(i)
		print string
