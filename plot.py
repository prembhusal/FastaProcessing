
from matplotlib import pyplot as plt
import numpy as np
#plot the output for localMst vs SparkMst to find cross point

def mul(x):
	l = [item * 1000 for item in x]
	return l

x = [2,4,8,16,32,64]
local = [1,2,6,21,79,302]
par = [18,19,22,30,43,77]


plt.scatter(x,local)
plt.plot(x,local,linewidth = 1.5, label = 'localMST', color = 'red')

plt.scatter(x,par)
plt.plot(x,par,linewidth = 1.5, label = 'SparkMST', color = 'green')

plt.xlabel("Junction sequence size in thousands")
plt.ylabel("Time in seconds")
plt.legend(loc="upper left")
plt.show()
