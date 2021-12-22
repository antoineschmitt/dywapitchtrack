from ctypes import *
import librosa


class DyWaPitchTracker(Structure):
    _fields = [
        ("_prevPitch", c_double),
        ("_pitchConfidence", c_int),
    ]

pitchtracker = DyWaPitchTracker()
ptr_pitchtracker = pointer(pitchtracker)

libpitch = cdll.LoadLibrary('libpitch.so')
libpitch.dywapitch_inittracking(ptr_pitchtracker)
libpitch.dywapitch_computepitch.restype = c_double

print(libpitch)

samples, sr = librosa.load('trailer.wav', sr=44100, mono=True)
print(sr)
samples = list(samples)
head = 0
len_s = len(samples)

c_d_samples = c_double * len_s
samples = c_d_samples(*samples)

ptr_s = pointer(samples)

print(len_s)
step = 2048
cur = 0

i = 1

while cur < len_s - step:
    thepitch = libpitch.dywapitch_computepitch(ptr_pitchtracker, ptr_s, cur, step)
    print(i, thepitch)
    cur += 2048 - 336
    i += 1

