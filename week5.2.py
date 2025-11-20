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

sd.default.device = (None, 1)  # (input device, output device)
sd.play(x, sr)
sd.wait()

rms =lr.feature.rms(y=x)
zcr = lr.feature.zero_crossing_rate(x)

plt.plot(rms.T, "blue")
plt.plot(zcr.T, "red")

X = lr.stft(x)
Xa = np.angle(X )   # i gueessave the angle
              
Xm = np.abs(X)

N = Xm[:,320:400]  # N represents a short segment in time — about 80 frames wide —
                      #but still includes all frequencies."

average = np.mean(N,1)   #Average noise per frequency 1= frequency access

k=0.08
average = k * average

Em = Xm - average[:,None]

Xest = Em * np.exp(1j*Xa)




inverse = lr.istft(Xest, hop_length=512)  #back to time-domain audio
inverse = inverse.astype(np.float32)       
sd.play(inverse, sr, device = 1)
sd.wait()

n_frames = rms.shape[1]
time_axis = np.arange(n_frames) * 512 / sr

rms_inv =lr.feature.rms(y=inverse)
zcr_inv = lr.feature.zero_crossing_rate(inverse)
plt.figure()
plt.plot(time_axis , rms_inv.T, "blue")
plt.plot(time_axis, zcr_inv.T, "red")
plt.show()