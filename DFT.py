import numpy as np
import matplotlib.pyplot as plot
def dft(x):
	y=[ ]
	l=len(x)
	if l<N:
		s=N-l
		x=np.append(x,np.zeros(s))
	for k in range(0,N):
		sum=0
		for n in range(0,N):
			if n>=0 and n<l:
				j=complex(0,-1)
				sum=sum+(x[n]*np.exp((j*2*np.pi*n*k)/float(N)))
		y=np.append(y,sum)
	return(y)
m=int(input("Enter length"))
x=np.zeros(m)
print("enter samples:")
for i in range(m):
	x[i]=int(input(" "))
print(x)
N=int(input("enter your DFT points:"))
print("DFT of an array=",dft(x))
f1=int(input("enter signal frequency"))
fs=int(input("enter sampling frequency"))
x=np.arange(-200,200,1)
y=np.sin(2*np.pi*float(f1)/float(fs)*x)
k=np.arange(0,N)
plot.subplot(3,1,1)
plot.plot(y)
plot.subplot(3,1,2)
plot.plot(k,np.abs(dft(y)))
plot.subplot(3,1,3)
plot.plot(k,np.angle(dft(y)))
plot.show( )


	