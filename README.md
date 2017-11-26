# pySpeechRev
This python code performs an efficient speech reverberation starting from a dataset of close-talking speech signals and a collection of acoustic impulse responses. 

The reverberated signal y[n] is computed in the following way:

y[n]=x[n] * h[n]

where x[n] is the clean signal and * is the convolutional operator.

The script takes in input the following arguments:
-  in_folder: folder where the original close-talk dataset is stored.
-  out_folder: folder where the reverberated dataset will be stored.
-  list.txt : it is a text file where each row should contain: original_wav_file IR_file.

Before run it, make sure you have all the needed python packages. In particular:
- pysoundfile: pip install pysoundfile
- numpy
- scipy

Example:
```
python pySpeechRev.py clean_examples/ rev_examples/ list.txt
```

Tested on:
Python 2.7
