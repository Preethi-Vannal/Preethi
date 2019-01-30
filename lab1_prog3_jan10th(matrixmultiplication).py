import numpy as np

m=int(input("enter rows for 1st MATRIX"))
n=int(input("enter columns for 1st MATRIX"))
print ("enter elements in 1st matrix")
a=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		a[i][j]=int(input(" "))

p=int(input("enter rows for 2nd MATRIX"))
t=int(input("enter columns for 2nd MATRIX"))
print("enter elements in mATRIX2")
b=np.zeros((p,t))
for i in range(p):
	for j in range(t):
		b[i][j]=int(input(" "))

if(n==p):
	print("MULTIPLICATION OF A GIVEN MATRIX")
	sum=0
	for i in range(m):
		for k in range(t):
			sum=0
			for j in range(n):
				sum=sum+a[i][j]*b[j][k]
				y=np.zeros((m,t))
				for i in range(m):
					for j in range(n):
						y[i][j]=sum
	print(y)							
else:
	print ("MATRIX MULTIPLICATION IS NOT POSSIBLE")
				
	



