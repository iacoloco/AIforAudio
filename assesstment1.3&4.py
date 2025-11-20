#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 11:23:07 2025

@author: armandoiachini
"""

"Assesstment step 3: Subtraction"

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa as lr
from scipy.ndimage import median_filter


x, sr = lr.load("bush_mono.wav")
sd.play(x, sr)
sd.wait()

rms =lr.feature.rms(y=x)
zcr = lr.feature.zero_crossing_rate(x)

"make rms and zrc on vector"
rms_values = rms[0,:]
zcr_values = zcr[0,:]

rms_Threshold = np.max(rms_values) * 0.2
zcr_Threshold = np.max(zcr_values) * 0.2

noise_condition = (rms_values < rms_Threshold) & (zcr_values > zcr_Threshold)

noise_condition_int = noise_condition.astype(int)


Noise_Median_Filter = median_filter(noise_condition_int, size=5)
Noises_Frames = Noise_Median_Filter

"Get the Chunks of noises"

Chunk_Noises=[]
inside=False
count=0
index_noises= []


for i, values in enumerate(Noises_Frames):
    if values ==1:
        index_noises.append((i))
        
    if values == 1 and not inside:
        start = i
        inside = True
     
        
    
    if values == 0 and inside:
        end = i -1 
        inside = False
        count += 1
        Chunk_Noises.append((start , end))


start, end = Chunk_Noises[0]         


X = lr.stft(x)
"The STFT is computed using librosa’s default parameters:"
"n_fft = 2048, hop_length = 512 (75% overlap), Hann window."


"-----> Save the angle<--------"
Xangle = np.angle(X )   

"Compute Magnitude"
Xmag = np.abs(X)

"Time axes"

"Xmag.shape ----->Out[(1025, 437) ----_ freq_bins = 1025 ---> frames = 437"
hop_length = 512 
frames = Xmag.shape[1]
freq_bins = Xmag.shape[0]


time_x_Stft = np.arange(frames) * hop_length / sr 



N = Xmag[:,index_noises]  # N represents a short segment in time — about 80 frames wide —
                      #but still includes all frequencies."

average = np.mean(N,1)   #Average noise per frequency 1= frequency access

k=0.6
average = k * average

Em = Xmag - average[:,None]

Xest = Em * np.exp(1j*Xangle)




inverse = lr.istft(Xest, hop_length=512)  #back to time-domain audio
inverse = inverse.astype(np.float32) 
    
sd.play(inverse, sr)
sd.wait()

n_frames = rms.shape[1]
time_axis = np.arange(n_frames) * hop_length / sr

rms_inv =lr.feature.rms(y=inverse)
zcr_inv = lr.feature.zero_crossing_rate(inverse)
plt.figure()
plt.plot(time_axis , rms_inv.T, "blue")
plt.plot(time_axis, zcr_inv.T, "red")
plt.show()
        
        
        

        