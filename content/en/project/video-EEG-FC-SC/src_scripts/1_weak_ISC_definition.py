
"""Study 1. This script defines the weak ISC time points and slices the Hilbert-transformed envelope signal from 200ms before to 500ms after the time point"""
import numpy as np

HOMEDIR = "/users/local/Venkatesh/Brainhack" # Change this to your local directory

weak_ISC = [ 10,  32,  35,  46,  47,  58,  59,  60,  61,  70,  71,  94,  95,
       107, 108, 123, 124, 132, 137, 142, 146, 148, 155, 156] # Manually selected weak ISC time points

fs = 125 #Hz
_200ms_in_samples = 25 # 200ms
_500ms_in_samples = 63 # 500ms
n_sub = 25 # number of subjects

def slicing(stc): # stc is a 3D array of shape (n_ROI, n_ROI, n_seconds * fs)
    signal_sliced = list() 

    for time in weak_ISC: # time is the time point in seconds
        # Slice the signal from 200ms before to 500ms after the time point
        sliced = stc[:, :,time * fs - _200ms_in_samples : time * fs + _500ms_in_samples]
        signal_sliced.append(sliced)


    return signal_sliced

# Load the Hilbert-transformed envelope signal 
envelope_signal = np.load(f"{HOMEDIR}/src_data/envelope_signal_bandpassed.npz")

# Slice the signal
envelope_signal_sliced = dict()
for labels, signal in envelope_signal.items():# signal is a 3D array of shape (n_ROI, n_ROI, n_seconds * fs)
    envelope_signal_sliced[f'{labels}'] = slicing(signal)
    # Swap axes to make the shape (n_seconds * fs, n_ROI, n_ROI)
    envelope_signal_sliced[f'{labels}'] = np.swapaxes(envelope_signal_sliced[f'{labels}'], 0,1)
    

np.savez_compressed(f'{HOMEDIR}/Generated_data/Cortical_surface_related/wideband_and_other_bands',**envelope_signal_sliced)
