import numpy as np
import matplotlib.pyplot as plot
f1=input(" enter frequency for 1st signal") 
fs=input("enter your sampling frequency")
x1=np.arange(0,20,0.1)
y1=np.sin(2*np.pi*x1*(float(f1)/float(fs)))
c=10*y1
plot.subplot(3,1,1)
plot.plot(x1,c)
f2=input("enter frequency for 2nd signal")
x2=np.arange(0,20,0.1)
y2=np.cos(2*np.pi*x2*(float(f2)/float(fs)))
d=6*y2
plot.subplot(3,1,2)
plot.plot(x2,d)
x3=x1+x2
e=c+d
plot.subplot(3,1,3)
plot.plot(x3,e)
plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )
