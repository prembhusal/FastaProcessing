
from matplotlib import pyplot as plt
import numpy as np

#plotting biggest group with 4 points and regression line

x = [ 147,164,169,799]
y = [1452,2690,1123,8791]
#x = mul(x)
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color = "green", linestyle="--")
p1 =np.polyfit(x,y,1)
x_extended = np.linspace(20, 2000, 100)
plt.plot(x_extended,np.polyval(p1,x_extended),'r-', linestyle="--")
plt.scatter(147,1452,color = "red",label ='D4')
plt.scatter(164,2690,color='orange',label='D1')
plt.scatter(169,1123,color = "blue",label='D2')
plt.scatter(799,8791,color='black',label='D3')

plt.xlabel("Data size in thousands")
plt.ylabel("Biggest VJ group size")
plt.legend(loc="upper left")
plt.show()
