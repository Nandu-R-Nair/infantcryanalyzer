import audioread
import sounddevice as sd
import struct
import wave
import contextlib
import sys
import glob
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import wave
from scipy.io import wavfile as wav
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
out='D:/mainproject/babycrydata/output/'
inpath=input("PATH  :   ")

ext = (inpath.split('/')[-1]).split('.')[-1]
#------------------------convert start -------------------------------------
filename = inpath
if(ext=='3gp'):        
    with audioread.audio_open(filename) as f:
#         print('Input file: %i channels at %i Hz; %.1f seconds.' %
#               (f.channels, f.samplerate, f.duration),
#               file=sys.stderr)
#         print('Backend:', str(type(f).__module__).split('.')[1],
#               file=sys.stderr)
        filename_new = out + filename.split('/')[-1]
        with contextlib.closing(wave.open(filename_new + '.wav', 'w')) as of:
            of.setnchannels(f.channels)
            of.setframerate(f.samplerate)
            of.setsampwidth(2)
            for buf in f:
                of.writeframes(buf)
            print(of)
elif(ext=='caf'):
    with audioread.audio_open(filename) as f:
#         print('Input file: %i channels at %i Hz; %.1f seconds.' %
#               (f.channels, f.samplerate, f.duration),
#               file=sys.stderr)
#         print('Backend:', str(type(f).__module__).split('.')[1],
#               file=sys.stderr)
        filename_new = out + filename.split('/')[-1]
        with contextlib.closing(wave.open(filename_new + '.wav', 'w')) as of:
            of.setnchannels(f.channels)
            of.setframerate(f.samplerate)
            of.setsampwidth(2)
            for buf in f:
                of.writeframes(buf)
elif(ext=='mp4'):
    with audioread.audio_open(filename) as f:
#         print('Input file: %i channels at %i Hz; %.1f seconds.' %
#               (f.channels, f.samplerate, f.duration),
#               file=sys.stderr)
#         print('Backend:', str(type(f).__module__).split('.')[1],
#               file=sys.stderr)
        filename_new = out + filename.split('/')[-1]
        with contextlib.closing(wave.open(filename_new + '.wav', 'w')) as of:
            of.setnchannels(f.channels)
            of.setframerate(f.samplerate)
            of.setsampwidth(2)
            for buf in f:
                of.writeframes(buf)
else:
    filename_new = filename
#-------------------------------end convert---------------------------------


#-----------------------------Feature Extraction----------------------------------------------------
f=filename_new+'.wav'
