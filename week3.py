#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:20:37 2025

@author: armandoiachini
"""

"WEEK 3"

"Plot the all array using matplot"
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from scipy.signal import stft
import sounddevice as sd



samplerate , data = wavfile.read("piano_chord_mono.wav")
data = data.astype(np.float32)
data = data / np.max(np.abs(data))

sd.play(data , samplerate)
sd.wait()

print(samplerate)



"Generate Time  axis using np.arange. The increment has to be each sample step"
Ts= 1/samplerate
t= np.arange(len(data)) / samplerate


plt.figure()
plt.plot(t, data)
plt.xlabel("Time s")
plt.ylabel("Amplitude")

"Zoom in"

plt.figure()

plt.plot(t[1000:1050], data[1000:1050])
plt.xlabel("Time s")
plt.ylabel("Amplitude")

"SCompute FFT"
FFT = np.fft.rfft(data)
print("len data" ,len(data))
print("len FFT " ,len(FFT))

"to get the magnitude we remove the imaginary part likke +0j"
magnitude = np.abs(FFT)

"Plot the log using(np.log)"
log_magnitude = np.log(magnitude)
print("len magnitude" ,len(log_magnitude))

plt.figure()
plt.plot(log_magnitude)
plt.xlabel("N samples")
plt.ylabel("Magnitude")



"Label the frequency axis using the same approach as before. In this case, each step is Fs/ N"
" and the range is [0, FS/2] Nyquest"

#frequens = np.arange(0 , (samplerate /2) + 1 , samplerate / len(data))
N = len(data)
print("len data" ,len(data))
binStep = samplerate / N
frequens = np.arange(0, N//2 + 1) * binStep  #f 0 to n//2 each indext * dt ex 0 bin * dt = 00 , 1 bin * dt....until nn//2
print("len frequens" ,len(frequens))

plt.figure()
plt.plot(frequens , magnitude)
plt.xlabel("Frequencyyyyyy")
plt.ylabel("Magnitude")

"Compute the stft using scipy.signal.stft"
"Revire the parameters:"
"window = 1024"
"hops = 512"



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







































