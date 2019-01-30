import numpy as np
m=int(input("enter rows"))
n=int(input("enter columns"))
if(m==n):
	print ("enter elements in matrix")
	a=np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			a[i][j]=int(input(" "))
	print ("GIVEN MATRIX")
	print (a)
	y=np.linalg.det(a)
	print ("DETERMINANT OF A GIVEN MATRIX:",y)
	if(y!=0):
		r=np.linalg.inv(a)
		print ("INVERSE OF A GIVEN MATRIX:",r)
	else:
		print("matrix inversion is not possible because det value is zero")
else:
	print("given matrix is not a suitable matrix for performing inversion")
