#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:36:17 2025

@author: armandoiachini
"""

from scipy.io import wavfile
from scipy.signal import stft
import numpy as np
import matplotlib.pyplot as plt


samplerate , data = wavfile.read("oboe.wav")


Ts = 1 / samplerate;
t= np.arange(len(data)) / samplerate


nperseg  = 1024          # window size (samples)
noverlap = 512           # overlap (samples) -> hop = 512
window   = 'hann'
nfft     = nperseg

f, t_frames, Zxx = stft(
    data, fs=samplerate,
    window=window,
    nperseg=nperseg,
    noverlap=noverlap,
    nfft=nfft,
    boundary=None, padded=False
)


"Obtein the magnitude"

magnitudeSTFT = np.abs(Zxx)
log_magnitudeSTFT = np.log(magnitudeSTFT)


plt.figure()
plt.imshow(
    log_magnitudeSTFT,
    origin='lower',                      # put 0 Hz at the bottom
    aspect='auto',                       # stretch automatically in time
    extent=[t[0], t[-1], f[0], f[-1]]    # label axes correctly
)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar() 

print(Zxx.shape)

oneFrame = Zxx[0:100,0]
print("One Frame.shape: " ,oneFrame.shape)


