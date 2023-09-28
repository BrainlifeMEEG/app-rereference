# Copyright (c) 2020 brainlife.io
#
# This file is the main script for applying baseline correction to MEG/EEG Epochs files.
#
# Author: Kamilya Salibayeva
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


fname = config['epochs']
ref_ch = config['ref_ch']

epochs = mne.read_epochs(fname)
epochs.set_eeg_reference(ref_channels = ref_ch)

# save mne/raw
epochs.save(os.path.join('out_dir','epo.fif'))

