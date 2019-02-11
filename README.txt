dywapitchtrack
Dynamic Wavelet Algorithm Pitch Tracking C library

The dywapitchtrack library computes the pitch of an audio stream in real time.
The pitch is the main frequency of the waveform (the ‘note’ being played or sung).
It is expressed as a float in Hz.

Unlike the human ear, pitch detection is difficult to achieve for computers. Many
algorithms have been designed and experimented, but there is no ‘best’ algorithm.
They all depend on the context and the tradeoffs acceptable in terms of speed and
latency. The context includes the quality and ‘cleanness’ of the audio : obviously
polyphonic sounds (multiple instruments playing different notes at the same time)
are extremely difficult to track, percussive or noisy audio has no pitch, most
real-life audio have some noisy moments, some instruments have a lot of harmonics, etc…

The dywapitchtrack is based on a custom-tailored algorithm which is of very high
quality: both very accurate (precision < 0.05 semitones), very low latency (< 23 ms)
and very low error rate. It has been thoroughly tested on human voice.

It can best be described as a dynamic wavelet algorithm (dywa):

The heart of the algorithm is a very powerful wavelet algorithm, described in a paper
by Eric Larson and Ross Maddox : “Real-Time Time-Domain Pitch Tracking Using Wavelets”
of UIUC Physics.
https://pdfs.semanticscholar.org/1ecf/ae4b3618f92b4267912afbc59e3a3ea1d846.pdf

This central algorithm has been improved by adding dynamic tracking, to reduce the common
problems of frequency-halving and voiced/unvoiced errors. This dynamic tracking explains
the need for a tracking structure (dywapitchtracker). The dynamic tracking assumes that
the main function dywapitch_computepitch is called repeatedly, as it follows the pitch
over time and makes assumptions about human voice capabilities and reallife conditions
(as documented inside the code).

Note : The algorithm currently assumes a 44100Hz audio sampling rate. If you use a
different samplerate, you can just multiply the resulting pitch by the ratio between
your samplerate and 44100.

See the dywapitchtrack.h file for the library API documentation.

History :
This algorithm has been designed during a mission for a customer. As I had kept the
author’s rights on the source code, I eventually decided to make this code public and
open source, because it is of really high quality. This algorithm has been extensively
tested, especially it has been included in an Adobe Director Xtra (plugin),
asPitchDetect Xtra, that has been distributed widely for a few years.

I hope that it can be used with pleasure and efficiency in your project.

Thank you
Antoine Schmitt April 2010

-- Documentation

See the dywapitchtrack.h file for the library API documentation.


-- Version history

Inital release : Antoine Schmitt April 2010
v2 : Antoine Schmitt Nov2016, following fine-tuning remarks by Robin Carduner

-- Building, Installing

- the iPhone/dywapitchtrack.xcodeproj builds an iPhone static library, against which
one can statically link an iPhone application.


-- MIT open source licence
 
 Copyright (c) 2010 Antoine Schmitt
  
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
