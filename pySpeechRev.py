# pySpeechRev
# Mirco Ravanelli - Fondazione Bruno Kessler
# Nov 2017

# Example:
# python pySpeechRev.py clean_examples/ rev_examples/ list.txt

import numpy as np
from scipy import signal
import sys
import os
import soundfile as sf

# Load support lib
from supplib import ReadList
from supplib import copy_folder
from supplib import load_IR
from supplib import shift

# Reading input arguments
in_folder = sys.argv[1]  # input folder
out_folder = sys.argv[2]  # output folder
list_file = sys.argv[3]  # list file ("wav_file IR_file")


# Read List file
[list_sig, list_ir] = ReadList(list_file)

# Replicate input folder structure to output folder
copy_folder(in_folder, out_folder)

# Speech Data Reverberation Loop
for i in range(len(list_sig)):

    # Open clean wav file
    # [fs, signal_clean] = wavfile.read(list_sig[i])
    [signal_clean, fs] = sf.read(list_sig[i])

    signal_clean = signal_clean.astype(np.float64)

    # Signal normalization
    signal_clean = signal_clean / np.max(np.abs(signal_clean))

    # Open Impulse Response (IR)
    IR = load_IR(list_ir[i])

    # IR normalization
    IR = IR / np.abs(np.max(IR))
    p_max = np.argmax(np.abs(IR))

    signal_rev = signal.fftconvolve(signal_clean, IR, mode="full")

    # Normalization
    signal_rev = signal_rev / np.max(np.abs(signal_rev))

    # IR delay compensation
    signal_rev = shift(signal_rev, -p_max)

    # Cut reverberated signal (same length as clean sig)
    signal_rev = signal_rev[0 : signal_clean.shape[0]]

    # Save Reverberated Speech
    file_out = list_sig[i].replace(in_folder, out_folder)
    # wavfile.write(file_out,fs,signal_rev)
    sf.write(file_out, signal_rev, fs)

    print("Done %s" % (file_out))
