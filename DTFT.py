import numpy as np
import matplotlib.pyplot as plot
def dtft(x):
	y=[ ]
	w=np.arange(-1.0*np.pi,np.pi,np.pi/500.0)
	for i in w:
		sum=0
		for n in range(len(x)):
			if n>=0 and n<len(x):
				j=complex(0,-1)
				sum=sum+(x[n]*np.exp(j*i*n))
		y=np.append(y,sum)
	return(y)

l=int(input("enter length of array:"))
x=np.zeros(l)
for i in range(l):
	x[i]=int(input("enter samples"))
print(x)
print ("DTFT of x=",dtft(x))

w=np.arange(-1.0*np.pi,np.pi,np.pi/500)
f1=int(input("enter signal frequency"))
fs=int(input("enter sampling frequency"))
x=np.arange(-200,200,1)
y=np.sin(2*np.pi*x*float(f1)/float(fs))
plot.subplot(3,1,1)
plot.plot(y)
plot.subplot(3,1,2)
plot.plot(w,np.abs(dtft(y)))
plot.subplot(3,1,3)
plot.plot(w,np.angle(dtft(y)))
plot.show( )

