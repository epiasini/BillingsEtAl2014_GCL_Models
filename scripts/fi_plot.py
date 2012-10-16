#! /usr/bin/env python
# -*- coding: utf-8 -*-
## Network I/O plotting script.
import sys
import glob
import numpy as np
from matplotlib import pyplot as plt

timestamp = sys.argv[1]
stim_rate_range = range(1, 440, 40)

fig, ax = plt.subplots()

rates = []
threshold = 'min20'
for amplitude in stim_rate_range:
    data_files = glob.glob('../simulations/{0}_{1}/GoCs_*'.format(timestamp, amplitude))
    rate_average = sum([len(np.loadtxt(f)) for f in data_files])/float(len(data_files))
    rates.append(rate_average)

ax.plot(stim_rate_range, rates, marker='o')

#ax.legend(loc='best')
ax.set_xlabel('stimulation rate (Hz)')
ax.set_ylabel('firing rate (Hz)')
plt.show()
