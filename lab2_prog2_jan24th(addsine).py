import numpy as np
import matplotlib.pyplot as plot
f1=input(" enter frequency for 1st signal") 
fs=input("enter your sampling frequency")
x1=np.arange(0,10,0.1)
y1=np.sin(2*np.pi*x1*(float(f1)/float(fs)))
plot.subplot(4,1,1)
plot.plot(x1,y1)
f2=input("enter frequency for 2nd signal")
x2=np.arange(0,10,0.1)
y2=np.cos(2*np.pi*x2*(float(f2)/float(fs)))
plot.subplot(4,1,2)
plot.plot(x2,y2)
x3=x1+x2
y3=y1+y2
plot.subplot(4,1,3)
plot.plot(x3,y3)
x4=x1*x2
y4=y1*y2
plot.subplot(4,1,4)
plot.plot(x4,y4)
plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )






