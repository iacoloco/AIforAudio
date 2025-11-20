#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 11:36:26 2025

@author: armandoiachini
"""

"Assestment 1.2"

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa as lr
from scipy.ndimage import median_filter

x, sr = lr.load("bush_mono.wav")

x = x.astype(np.float32)

"normalisation" 
x = x / np.max(np.abs(x))

rms =lr.feature.rms(y=x)
zcr = lr.feature.zero_crossing_rate(x)

"make rms and zrc on vector"
rms_values = rms[0,:]
zcr_values = zcr[0,:]


rms_Threshold = np.max(rms_values) * 0.2
zcr_Threshold = np.max(zcr_values) * 0.2

"Create a boolean array where zcr> Theshol and rms < Threshold"

noise_condition = (rms_values < rms_Threshold) & (zcr_values > zcr_Threshold)

noise_condition_int = noise_condition.astype(int)

"Speech recconition"
speech_condition_int = 1 - noise_condition_int

        
hop_length = 512
n_frames = rms_values.shape[0]
time_axis = np.arange(n_frames) * hop_length / sr
plt.figure()
plt.plot(time_axis, noise_condition_int)
plt.xlabel("Time (s)")
plt.ylabel("Noise condition (0 = not noise, 1 = noise)")
plt.title("Noise frames detected: 1= Noise / 0= Speech")
plt.show()


Noise_Median_Filter = median_filter(noise_condition_int, size=5)

"Plot smoother noise condition"

plt.figure()
plt.plot(time_axis , Noise_Median_Filter)
plt.xlabel("Time (s) ")
plt.ylabel("1= Noise - 0= Speech")
plt.title("Boolean Noise Detection")
plt.show()


Speech_Median_Filter= median_filter(speech_condition_int, size= 5)
speech_frames1 = Speech_Median_Filter

plt.figure()
plt.plot(time_axis , rms_values, "blue")
plt.plot(time_axis, Speech_Median_Filter)
plt.xlabel("Time (s)")
plt.ylabel("1 = speech - 0=speech")
plt.title("Boolean Speech Detection")
plt.show()

"Transform Index_Frame in T "

"by knowingb Ts = 1 (sample) / fs "
"Knowing that now i have frames with jumps of 512 (Hop_lenght)"
" Convert frame indices to samples and seconds"
"---------># Each frame advances by hop_length (512 samples)."
"#---------------> Sample index  = frame_index * hop_length"
"# ------------------->Time (seconds) = frame_index * hop_length / sr"


"INDICATE THE BEGININ  AND THE END OF REGIONS CONTAINING SPEACH"
chunks_Speech = []
inside = False
count=0
for i, value in enumerate(speech_frames1):
    
    if value == 1 and not inside:
        start   = i
        inside = True
    elif value == 0 and inside:
        end = i -1
        inside =  False
        chunks_Speech.append((start , end ))
        count +=1



print("The Audio has" , count ,  "chunks")
    
        
plt.figure()
plt.plot(time_axis, Speech_Median_Filter)
for start, end in chunks_Speech:
    plt.hlines(
        y=1.1,
        xmin=time_axis[start],
        xmax=time_axis[end],
    )
plt.show()
    
    
        
            
    
        
        
        
    
        




