import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 100.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
y = np.arange(0,1,Ts) # signal vector; create Fs samples

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs

serdev = 'COM4'
s = serial.Serial(serdev)
line=s.readline()
for x in range(0, int(Fs)):
    line=s.readline() # Read an echo string from B_L4S5I_IOT01A terminated with '\n'
    # print line
    y[x] = float(line)

plt.plot(t,y)
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.show()
s.close()
