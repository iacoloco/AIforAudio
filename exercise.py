#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 16:20:10 2025

@author: armandoiachini
"""
from scipy.io import wavfile
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

"Exrecise 1"


samplerate, data =wavfile.read("piano_chord_mono.wav")
print("Sample rate:", samplerate, "Hz")
print("Data type: ", data.dtype)



duration = len(data) / samplerate
print("Duration: ", duration, "seconds")
print(f"Duration: {duration:.2f} seconds")

print("Shape:", data.shape)
t= np.arange(len(data))/ samplerate
#OR np.arange(0 , len(data) , 1/samplerate)

"Convert int16 bit to Float points"
#y=data.astype(np.float32) / np.max(np.abs(data))
y=data.astype(np.float32)
yAbs = np.abs(y)
yMaxValue= np.max(yAbs)
y = y / yMaxValue
plt.figure()
plt.plot(t,y)
#plt.title("Waveform of piano_chord_mono.wav")
#plt.xlabel("Time in seconds")
#plt.ylabel("Amplitude normalized 1 to -1")

"Trimmed"
"mMke all y acxes absolutes"
yabs= np.abs(y)

threshold= 0.01

sampleMagiorThreshold = np.where(yabs > threshold)[0]
start = sampleMagiorThreshold[0]

end= np.where(yabs > threshold)[0][-1]
trimmed = y[start:end + 1]

start_time = start / samplerate
print("start trimmed: " , start_time)
end_time = end / samplerate
print("end trimmed: " , end_time)

# Play directly
#sd.play(data, samplerate)
#sd.wait()

t_trim = np.arange(len(trimmed)) / samplerate
#plt.plot(t_trim, trimmed)

#plt.plot(duration_chunk,chunk)

#sd.play(chunk, samplerate)
#sd.wait()
#plt.plot(data)
print(data.shape)

"/Users/armandoiachini/Documents/Uni/AIforAudio/audio_project"

#samplerate, data2 =wavfile.read("piano_chord_stereo.wav")

chunk = data[200000:400000]
duration_chunk = np.arange(len(chunk)) / samplerate + 40000/ samplerate
"tranform chunk in -1 to 1 : data / data max value "
chunk = chunk / np.max(np.abs(chunk))
plt.plot(chunk)




data2abs = np.abs(data)

trimStart2 = np.where(data2abs > threshold)[0][0]
trimEnds2 = np.where(data2abs > threshold)[0][-1]
print("trim starts: ", trimStart2)
print("trim ends: " ,trimEnds2)
print(y)


plt.figure()
fade = np.linspace(0, 1, len(chunk), endpoint=True) 
"make fade 2D"
fade = fade[:,None]
print(fade)
plt.plot(fade)



fadeChunk = chunk * fade

plt.plot(fadeChunk)
print(chunk.shape)
print(fade.shape)

sd.play(fadeChunk, samplerate)
sd.wait()

fade2 = np.linspace(1, 0, len(chunk), endpoint=True) 
fade2 = fade2[:,None]
chunk2 = fadeChunk * fade2

plt.plot(fade2)
plt.plot(chunk2)

sd.play(chunk2, samplerate)
sd.wait()
print(start)


"#Week3 FFT"
chunk2 = chunk2[:,0]
FFT = np.fft.rfft(chunk2)
magnitude = np.abs(FFT)
frequency= np.fft.rfftfreq( len(chunk2), 1/ samplerate)
print("frequency shape: ", frequency.shape)
print("magnitude shape: " , magnitude.shape)

plt.figure()
plt.plot(frequency, magnitude)
plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.show()

lgMagnitude = np.log(magnitude)
plt.plot(frequency, lgMagnitude)
plt.title("Magnitude Spectrum (dB scale)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")


              

