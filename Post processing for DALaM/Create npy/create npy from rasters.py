# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:30:17 2020

@author: Rajitha
"""

#Import modules
import glob
import numpy as np
from PIL import Image

#Make a list of files to read
filelist = glob.glob('*.tif')
variable=input("What is the climate variable?:")
#Create an array
x = np.array([np.array(Image.open(fname)) for fname in filelist])

#Dump the array to NPY file
y = np.moveaxis(x, 0, -1 )
np.save('{}.npy'.format(variable), y)

