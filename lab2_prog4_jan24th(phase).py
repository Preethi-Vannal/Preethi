import numpy as np
import matplotlib.pyplot as plot
f1=input(" enter frequency for 1st signal") 
fs=input("enter your sampling frequency")
p=0
x1=np.arange(0,10,0.1)
y1=np.cos(2*np.pi*x1*(float(f1)/float(fs))+p)
plot.subplot(3,1,1)
plot.plot(x1,y1)
f2=input("enter frequency for 2nd signal")
q=180
x2=np.arange(0,10,0.1)
y2=np.cos(2*np.pi*x2*(float(f2)/float(fs))+q)
plot.subplot(3,1,2)
plot.plot(x2,y2)
x3=x1+x2
y3=y1+y2
plot.subplot(3,1,3)
plot.plot(x3,y3)
plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )






