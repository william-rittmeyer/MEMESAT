#!/usr/bin/env python
# coding: utf-8

# # SSTV 
# (Author: Will "Witt" Rittmeyer)
# 
# 

# In[ ]:


import matplotlib.pylab as plt
import skimage.io as io
import numpy as np

from math import pi
from copy import deepcopy


# ## Extracting Binary RGB values
# 
# ### Read values from image

# In[378]:


#read image from directory

pic = io.imread('/Users/willrittmeyer/Desktop/test.jpg')


#read RGB values

red_channel = deepcopy(pic)
green_channel = deepcopy(pic)
blue_channel = deepcopy(pic)


#red image

red_channel[:,:,1] = 0;
red_channel[:,:,2] = 0;


#green image

green_channel[:,:,0] = 0;
green_channel[:,:,2] = 0;


#blue image

blue_channel[:,:,0] = 0;
blue_channel[:,:,1] = 0;


fig, ax = plt.subplots(ncols=2, nrows =2)


ax[0,0].imshow(pic)
ax[0,0].set_title('Original')

ax[0,1].imshow(red_channel)
ax[0,1].set_title('red_channel')

ax[1,0].imshow(green_channel)
ax[1,0].set_title('green_channel')

ax[1,1].imshow(blue_channel)
ax[1,1].set_title('blue_channel')


# ### Pixel values are extracted and stored in array

# In[379]:


#convert matrix of RGB brightness to array


red_rows = red_channel[:,:,0]
green_rows = green_channel[:,:,1]
blue_rows = blue_channel[:,:,2]

red_values = red_rows.flatten()
green_values = green_rows.flatten()
blue_values = blue_rows.flatten()


#bits needed to encode picture in binary

len(red_values)*3*8


# ### Pixel values are converted to binary

# In[380]:


binary_red = []
binary_green = []
binary_blue = []


#for loops creates a list of binary values encoding


for x in range(0,len(red_values)):

    leading_zeros = 2 + 8 - len(bin(red_values[x]))
    for y in range(0,leading_zeros):
        binary_red.append(0)

    for z in range(2,10-leading_zeros):
        binary_red.append(int(bin(red_values[x])[z]))



for x in range(0,len(green_values)):

    leading_zeros = 2 + 8 - len(bin(green_values[x]))
    for y in range(0,leading_zeros):
        binary_green.append(0)

    for z in range(2,10-leading_zeros):
        binary_green.append(int(bin(green_values[x])[z]))

        

for x in range(0,len(blue_values)):

    leading_zeros = 2 + 8 - len(bin(blue_values[x]))
    for y in range(0,leading_zeros):
        binary_blue.append(0)

    for z in range(2,10-leading_zeros):
        binary_blue.append(int(bin(blue_values[x])[z]))


# ### Plot of first 50 binary values of red

# In[381]:


plt.plot(binary_red[0:49]);


# ## Frequency Modulation (FM)
# 
# 
# ### Example binary input

# In[383]:


#data to bet sent

A = [1,1,0,1,0,0,1,0,0,1,1,1,1]

#sampling frequency

Fs = 1000

#samples per binary number

m = 100

#time

upper_bound = (len(A)*m)/Fs

t = np.arange(0,upper_bound,1/Fs)


ys = []

for x in range(0,len(A)):
    
    for y in range(0,m):
        ys.append(A[x])
        

#plt.plot(t,ym);
plt.plot(t,ys);


# ### FM of binary example 

# In[384]:


#carrier wave in Hz
fc = 20;


#modulation index
b = 10;



ya = [element * b for element in ys]
              
    
#modulated signal

ym = np.cos(2*pi*fc*t + b *t*ya);


plt.plot(t,ym);
plt.plot(t,ys);
plt.title('Frequency Modulated (FM) signal');
plt.xlabel('Time');
plt.ylabel('Signal Amplitude');
plt.legend('FM Signal' 'Data');


# In[ ]:




