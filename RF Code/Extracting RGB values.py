#!/usr/bin/env python
# coding: utf-8

# In[86]:


import matplotlib.pylab as plt
import skimage.io as io
import numpy as np

from copy import deepcopy


#read image from directory

pic = io.imread('/Users/willrittmeyer/Desktop/bernie.jpg')


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


# In[87]:


#convert matrix of RGB brightness to array

red_rows = red_channel[:,:,0]
green_rows = green_channel[:,:,1]
blue_rows = blue_channel[:,:,2]

red_values = red_rows.flatten()
green_values = green_rows.flatten()
blue_values = blue_rows.flatten()


#bits needed to encode picture in binary

len(red_values)*3*8


# In[ ]:





# In[ ]:





# In[ ]:





# In[88]:


plt.plot(red_values[1:1000]);


# In[89]:


#bits needed to encode picture in binary

len(red_values)*3*8


# In[80]:





# In[ ]:




