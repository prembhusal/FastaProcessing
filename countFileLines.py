#this program will list all the files inside the folder and count the total lines in each file
import os

arr = os.listdir('.') # list of files inside current directory

#clunt Total line for each file
for fileName in arr:
	#print fileName 
	os.system("wc -l " +fileName)
