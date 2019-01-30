import numpy as np

m=int(input("enter rows for 1st MATRIX"))
n=int(input("enter columns for 1st MATRIX"))
print ("enter elements in 1st matrix")
a=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		a[i][j]=int(input(" "))

print("enter elements in mATRIX2")
b=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		b[i][j]=int(input(" "))

print("ADDITION OF TWO MATRICES")
r=np.zeros((m,n))
for i in range(m):
	for j in range(n):
		r[i][j]=a[i][j]+b[i][j]
print(r)

	