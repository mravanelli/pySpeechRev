import numpy as np
from scipy import signal
from scipy.io import loadmat
import sys
import os
import soundfile as sf
import shutil


def shift(xs, n):
    e = np.empty_like(xs)
    if n >= 0:
        e[:n] = 0.0
        e[n:] = xs[:-n]
    else:
        e[n:] = 0.0
        e[:n] = xs[-n:]
    return e


def copy_folder(in_folder, out_folder):
    if not (os.path.isdir(out_folder)):
        shutil.copytree(in_folder, out_folder, ignore=ig_f)


def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


def load_IR(IR_file):

    if ".mat" in IR_file:
        IR = loadmat(IR_file, squeeze_me=True, struct_as_record=False)
        IR = IR[IR.keys()[0]]
    else:
        [IR, fs] = sf.read(IR_file)

    return IR


def ReadList(list_file):
    with open(list_file, "r") as f:
        lines = f.readlines()
    list_sig = []
    list_ir = []
    for x in lines:
        list_sig.append(x.split(" ")[0])
        list_ir.append(x.split(" ")[1].rstrip())
    return [list_sig, list_ir]
