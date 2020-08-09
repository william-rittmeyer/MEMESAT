#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pylab as plt
import numpy as np
from math import pi


#sampling frequency
Fs = 2000; 

#time
t = np.arange(0,.1,1/Fs)

#carrier wave
fc = 100;

#signal frequency
fm = 20;

#modulation index
b = 3;

#data signal
ys = np.cos(2*pi*fm*t);


#modulated signal
ym = np.cos(2*pi*fc*t + b * np.sin(2*pi*fm*t));


plt.plot(t,ym);
plt.plot(t,ys);
plt.title('Frequency Modulated (FM) signal');
plt.xlabel('Time');
plt.ylabel('Signal Amplitude');
plt.legend('FM Signal' 'Data');


# In[ ]:





# In[ ]:




