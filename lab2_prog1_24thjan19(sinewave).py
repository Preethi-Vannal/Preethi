import numpy as np
import matplotlib.pyplot as plot
f1=input(" frequency for your signal") 
fs=input("enter your sampling frequency")
x=np.arange(0,10,0.1)
y=np.sin(2*np.pi*x*(float(f1)/float(fs)))
plot.plot(x,y)
plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )