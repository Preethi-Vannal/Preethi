import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plot
fs1,data1=wav.read('voice.wav')
print(fs1,len(data1),data1)
plot.subplot(3,2,1)
plot.plot(data1)
t=np.arange(0,len(data1)/fs1,1.0/fs1)
plot.subplot(3,2,2)
plot.plot(t,data1)

fs2,data2=wav.read('audio.wav')
print(fs2,len(data2),data2)
plot.subplot(3,2,3)
plot.plot(data2)
t=np.arange(0,len(data2)/fs2,1.0/fs2)
plot.subplot(3,2,4)
plot.plot(t,data2)


wav.write('voce.wav',fs1*2,data1)
fs3,data3=wav.read('voce.wav')
print(fs3,len(data3),data3)
plot.subplot(3,2,5)
plot.plot(data3)
t=np.arange(0,len(data3)/fs3,1.0/fs3)
plot.subplot(3,2,6)
plot.plot(t,data3)


plot.show( )

