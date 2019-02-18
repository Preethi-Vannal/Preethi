import numpy as np
n=int(input("enter sample length"))
x=np.zeros(n)
for i in range(n):
	x[i]=int(input("enter"))
print (x)

sum=0
for i in range(n):
	sum=sum+x[i]
print (sum)
	