# pySpeechRev
This python code performs an efficient speech reverberation starting from a dataset of close-talking speech signals and a collection of acoustic impulse responses. 

The reverberated signal y[n] is computed in the following way:
```
y[n]=x[n] * h[n]
```

where x[n] is the clean signal and * is the convolutional operator.

The script takes in input the following arguments:
-  in_folder: folder where the original close-talk dataset is stored.
-  out_folder: folder where the reverberated dataset will be stored.
-  list.txt : it is a text file where each row should contain: original_wav_file IR_file.

Before run it, make sure you have all the needed python packages. In particular:
- pysoundfile: ``pip install pysoundfile``
- numpy
- scipy

Example:
```
python pySpeechRev.py clean_examples/ rev_examples/ list.txt
```

# Reverberated TIMIT
To create a reverberated version of TIMIT do the following steps:
1- Make sure you have the TIMIT dataset. If not, it can be downloaded from the LDC website (https://catalog.ldc.upenn.edu/LDC93S1).
2- Change lst_TIMIT.txt according to the paths of your TIMIT Dataset
3- Run:
python pySpeechRev.py $path_TIMIT  $path_TIMIT_rev lst_TIMIT.txt

The current version of TIMIT has been contaminated with some high-quality impulse responses of the DIRHA-English Dataset [3]. 

Tested on:
Python 2.7, Ubuntu

This code has been used in the following papers:



[1] M. Ravanelli, P. Svaizer, M. Omologo, "Realistic Multi-Microphone Data Simulation for Distant Speech Recognition",  in Proceedings of Interspeech 2016. https://arxiv.org/abs/1711.09470

[2] M. Ravanelli, M. Omologo, "Contaminated speech training methods for robust DNN-HMM distant speech recognition", in Proceedings of  INTERSPEECH 2015. https://arxiv.org/abs/1710.03538

[3] M. Ravanelli, M. Omologo, "The DIRHA-English corpus and related tasks for distant-speech recognition in domestic environments", in Proceedings of ASRU 2015. https://arxiv.org/abs/1710.02560
