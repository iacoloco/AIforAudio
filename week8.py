#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:41:16 2025

@author: armandoiachini
"""

import librosa as lr
import matplotlib.pyplot as plt
import numpy as mp


dataset_path = "/Users/armandoiachini/Documents/Uni/AIforAudio/dataset"

x, sr = lr.load(dataset_path + "/0/0.wav" )

plt.plot(x)

"Mrcc"

mfccs = lr.feature.mfcc(y=x, sr=sr, hop_length= 128)

M = mfccs

print(M.shape)

"print(np.mean(M,1)"
    


import glob
files = glob.glob(dataset_path + "/*/*.wav")


"--> file[0]    would give the path"

dataMatrix = no.ones(600,20))



make a for loo to:
    
    to make mfcc fora each files
    
    
from os import path

cheack
base name 
and 
dirpath

convert to integer ----> 

LABEL =     int(path.base(path.dirname))


Next week:
    
    
    
    make init in the data set ---> stablish you base c0de variable 
    
    do the globe to capture all the path of the file
    create a matrix of 1 600 by 20
    
    and th foor loop for each file
    mrcc
    matrix
    goal 600 raw and 20 colom of mrcc
    
    
    




