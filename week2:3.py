#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 17:42:34 2025

@author: armandoiachini
"""

import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

samplerate, data = wavfile.read("piano_chord_mono.wav")

print("sample rate: ", samplerate, "Hz")
print("data type: " , data.dtype)
print("Data Shape" ,data.shape)
"convert data to float"
data = data.astype(np.float32)
print("converted data type: " , data.dtype)
print(data)

"normalisation" 
data = data / np.max(data)
t = np.arange(len(data)) / samplerate
print(len(data))


plt.figure()
plt.plot(t, data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform of piano_chord_mono.wav")

#sd.play(data, samplerate)
#sd.wait()

"Trimp data"

threshold = 0.05

startTrump = np.where(data > threshold)[0][0]
print("Trimp From: ", startTrump)
endTrump= np.where(data > threshold)[0][-1]
print("End Trimp: ", endTrump)

DataTrump = data[startTrump : endTrump]

tTrump= np.arange(len(DataTrump)) / samplerate

plt.figure()
plt.plot(tTrump, DataTrump)
plt.xlabel("Time s")
plt.ylabel('Amplitude')
plt.title("Make america great again!")

"Implememnt a fade"

fade = np.linspace(0, 1, len(data), endpoint=False) 

print("fade" , fade)

dataFade = data * fade
sd.play(dataFade)
sd.wait()

plt.figure()
plt.plot(t,dataFade)




