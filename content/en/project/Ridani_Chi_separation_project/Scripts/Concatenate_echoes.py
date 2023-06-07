####################################
# Filename: Concatenate_echoes.py
# Author: Daniel Ridani 
#
# Description: Script to concatenate N number of echo. You can as much as you want echoes, each time you add just load the file and add it's name to the concatination line
# 
# Inputs
# ----------
# data_path : str
#     Path to magnitude or phase echo file
# save_path : str
#     Path to save the results
####################################
import nibabel as nib
import numpy as np

# Load the two input NIfTI files
nii1 = nib.load('Path/to/first/echo')
nii2 = nib.load('Path/to/second/echo')
nii3 = nib.load('Path/to/third/echo')
nii4 = nib.load('Path/to/fourth/echo')
nii5 = nib.load('Path/to/fifth/echo')
nii6 = nib.load('Path/to/sixth/echo')

# Extract the image data and dimensions
data1 = nii1.get_fdata()
dims = data1.shape

# Concatenate the data by grouping the echoes
grouped_data = np.stack((data1, nii2.get_fdata(), nii3.get_fdata(), nii4.get_fdata()), nii5.get_fdata(), nii6.get_fdata()), axis=3)

# Create a new NIfTI image using the grouped data
grouped_nii = nib.Nifti1Image(grouped_data, affine=nii1.affine, header=nii1.header)

# Save the new NIfTI image to a file
nib.save(grouped_nii, 'add/Save/path')
