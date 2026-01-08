import numpy as np
from math import sqrt
#basically, write 3 functions which take a numpy array and calculate intensity

#for our puporses luminence and intensity will just be the average of the RGB values.
#I'm too dumb to understand the difference 

def calculate_luminence(pxl):
    return (pxl[0]+pxl[1]+pxl[2])/3

def calculate_higher_lower_luminence(pxls):
    high = 0
    low = 10000
    for pxl in pxls:
        luminence = int(calculate_luminence(pxl)) 
        #print(type(luminence), luminence)
        if luminence > high:
            high = luminence
        if luminence < low:
            low = luminence
    
    return high, low        
    
def intensity_contrast(pxls):
    if pxls == []:
        return 0
    higher_luminence, lower_luminence = calculate_higher_lower_luminence(pxls)    
    return higher_luminence
        
def luminence_contrast(pxls):
    if pxls == []:
        return 0
    higher_luminence, lower_luminence = calculate_higher_lower_luminence(pxls)    
    return higher_luminence/lower_luminence
    
def michelsons_contrast(pxls):
    if pxls == []:
        return 0
    higher_luminence, lower_luminence = calculate_higher_lower_luminence(pxls)
    return (higher_luminence - lower_luminence)/(higher_luminence + lower_luminence)
    
def RMS(pxls):
    if pxls == []:
        return 0
    
    luminize = np.vectorize(calculate_luminence, signature = "(3) -> ()")
    
    pxls = luminize(pxls)
    
    mean = np.mean(pxls)
    pxls = pxls-mean
    pxls = np.power(pxls, 2)
    
    sum = np.sum(pxls)
    div = sum/len(pxls)    
        
    return sqrt(div)