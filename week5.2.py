#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 16:46:28 2025

@author: armandoiachini
"""

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa as lr


x, sr = lr.load("bush_mono.wav")

#sd.play(x, sr)

rms =lr.feature.rms(y=x)
zcr = lr.feature.zero_crossing_rate(x)

plt.plot(rms.T, "blue")
plt.plot(zcr.T, "red")

X = lr.stft(x)
Xa = np.angle(X )   # i gueessave the angle
              
Xm = np.abs(X)

N = Xm[:,320:400]  # N represents a short segment in time — about 80 frames wide —
                      #but still includes all frequencies."

average = np.mean(N,1)
average = average[None ,:]
Em = Xm - average







# = lr.stft(x)

#Xm = 

#aveg = np.mean(N,1)


#estimateMagnetude = Xm - avg