#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:15:31 2025

@author: armandoiachini
"""

"Assestment 1"

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa as lr

x, sr = lr.load("bush_mono.wav")

x = x.astype(np.float32)

"normalisation" 
x = x / np.max(np.abs(x))

print("sample rate: ", sr, "Hz")
print("data type: " , x.dtype)
print("Data Shape" ,x.shape)
"convert data to float"
x = x.astype(np.float32)
print("converted data type: " , x.dtype)
print(x)


t = np.arange(len(x)) / sr


"Plot"

plt.figure()
plt.plot(t, x)
plt.xlabel("Time s")
plt.ylabel("Amplitude")


sd.play(x, sr)

"hop_length = 512 (liborsa default)"
hop_length = 512 
rms =lr.feature.rms(y=x)
zcr = lr.feature.zero_crossing_rate(x)

"X axes  from frames to seocnds "
n_frames = rms.shape[1]

time_axis = np.arange(n_frames) * hop_length / sr


plt.figure()
plt.plot(time_axis , rms.T, "blue")
plt.plot(time_axis, zcr.T, "red")
plt.show()

"Compiute STFT --->  n_fft = 2048 ; hop_length = 512 (liborsa default)"
hop_length = 512
Xstft = lr.stft(x)
print("Xstft.shape [freq_bins : frames] " , Xstft.shape)


Xa = np.angle(Xstft) 

"Magnitude"
Xm = np.abs(Xstft)
print("Xm.shape" , Xm.shape )

log_magnitudeSTFT = np.log(Xm)

"Defeni time and f axess ---> at the moment f is not in hx but in Frequency Bins"
total_Bins = Xm.shape[0]
print("totalBins:" , total_Bins)

freq_Hz_axesY = frequencies_Hz = np.linspace(0, sr/2, total_Bins)





plt.imshow(
    log_magnitudeSTFT,
    aspect='auto',
    origin='lower',
    extent=[ time_axis[0], time_axis[-1], freq_Hz_axesY[0], freq_Hz_axesY[-1] ]
)



