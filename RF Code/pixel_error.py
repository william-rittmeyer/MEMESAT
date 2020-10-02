import matplotlib.pylab as plt
import skimage.io as io
import random

from copy import deepcopy

original = io.imread('/Users/willrittmeyer/Desktop/download.jpg')

red_channel = deepcopy(original)
green_channel = deepcopy(original)
blue_channel = deepcopy(original)

red_channel[:,:,1] = 0;
red_channel[:,:,2] = 0;

green_channel[:,:,0] = 0;
green_channel[:,:,2] = 0;

blue_channel[:,:,0] = 0;
blue_channel[:,:,1] = 0;

fig, ax = plt.subplots(ncols=2, nrows =2)



ax[0,0].imshow(original)
#ax[0,0].imshow('Original')

ax[0,1].imshow(red_channel)
#ax[0,1].imshow('red_channel')

ax[1,0].imshow(green_channel)
#ax[1,0].imshow('green_channel')

ax[1,1].imshow(blue_channel)
#ax[0,1].imshow('red_channel')


def random_error(a):
    
    x = random.random()
    
    # a is percent occurence of error
    
    if (x < a):
        
    # if there is an error add a random integer to pixel value
    
        y = random.randint(0,len(original))
        
    else:
        y = 0
        
    return y
    
    
    def error_pic(pic,rate):
    new_picture = deepcopy(pic)
    for i in range(0,225):
        for j in range(0,225):
                new_picture[i,j,0] = (random_error(rate)+ pic[i,j,0])%len(pic);
                new_picture[i,j,1] = (random_error(rate)+ pic[i,j,1])%len(pic);
                new_picture[i,j,2] = (random_error(rate)+ pic[i,j,2])%len(pic);
                
                #random error occurs with "rate"%
                
                
    
    
    red_channel = deepcopy(new_picture)
    green_channel = deepcopy(new_picture)
    blue_channel = deepcopy(new_picture)

    red_channel[:,:,1] = 0;
    red_channel[:,:,2] = 0;

    green_channel[:,:,0] = 0;
    green_channel[:,:,2] = 0;

    blue_channel[:,:,0] = 0;
    blue_channel[:,:,1] = 0;
    
    
    fig, ax = plt.subplots(ncols=2, nrows =2)
    ax[0,0].imshow(new_picture)

    ax[0,1].imshow(red_channel)
    #ax[0,1].imshow('red_channel')

    ax[1,0].imshow(green_channel)
    #ax[1,0].imshow('green_channel')

    ax[1,1].imshow(blue_channel)
    #ax[0,1].imshow('red_channel')
    
    error_pic(original,0.2)
