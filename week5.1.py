#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 16:08:14 2025

@author: armandoiachini
"""

import sounddevice as sd
from scipy.io import wavfile
import matplotlib.pyplot as plt

samplerate , hiss = wavfile.read("hiss.wav")
hiss = hiss[:,0] / 32767.0


samplerate , mix = wavfile.read("mix.wav")
mix = mix / 32767.0

hiss = hiss[:len(mix)]



antinoise = hiss * -1
k= 0.6
estimate = mix +  k * antinoise

plt.figure()
plt.plot(hiss[1000:1020]), "white"
plt.plot(mix[1000:1020]), "r"




sd.play(estimate, samplerate)
sd.wait()

