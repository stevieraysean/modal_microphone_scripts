import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, linspace, power, log10

samps = 100000
freqs = linspace(0.000, 1.0, samps)

N = 4
M = 2

R = 64
outs_64 = []
for f in freqs:
    outs_64.append(power( (sin(2*pi*f*R*M/2)/sin(2*pi*f/2)), N))

R = 32
outs_32 = []
for f in freqs:
    outs_32.append(power( (sin(2*pi*f*R*M/2)/sin(2*pi*f/2)), N))

scale = int(samps/64)

freqs = freqs * 3.072e6

plt.plot(freqs[:scale], 20*log10(outs_64[:scale]),freqs[:scale], 20*log10(outs_32[:scale]))
plt.show()