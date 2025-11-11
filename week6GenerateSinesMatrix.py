#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 17:00:07 2025

@author: armandoiachini
"""

"data sete #omited part is on create data"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:34:26 2025

@author: armandoiachini
"""
import numpy as np

import matplotlib.pyplot as plt


fs =8000

ts = 1/fs

tt= np.arange(0, 100 * ts ,ts)


#generates sines
freq = 100 + 900 * np.random.random()


sine = np.sin(2*np.pi * freq * tt)

plt.figure()
plt.plot(tt , sine)


noise = 2 * np.random.random(100) -1 # think what the max what the min max ---> 1 time 2 menus 1 = 1
plt.figure()
plt.plot(tt,noise)




sines = np.zeros([500,100])

for i in range(500):
    freq = 100 + 900 * np.random.random()
    sine_wave = np.sin(2*np.pi * freq * tt)
    sines[i , : ] = sine_wave
    
    
    
    # generate noises 
noises = np.zeros((500,100))
noise_wave = 2 * np.random.random(100) -1 

for i in range(500):
    freq = 100 + 900 * np.random.random()
    noise_wave = 2 * np.random.random(100) -1 
    noises[i,:] = noise
    









