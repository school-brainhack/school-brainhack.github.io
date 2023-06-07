####################################
# Filename: R2Prime_calculation.py
# Author: Daniel Ridani 
#
# Description: Script to estimate R2' maps from T2* maps
# Inputs
# ----------
# data_path : str
#     Path to T2* file
# save_path : str
#     Path to save the results
####################################
import numpy as np
import nibabel as nib

# Load the input images
img1 = nib.load('Path/to/T2*/data')

# Calculate the inverse of each image
inv_img1 = 1/img1.get_fdata()

# Calculate the difference between the two images
diff_img = inv_img1/1.91

# Save the result to a NIfTI file
result_img = nib.Nifti1Image(diff_img, img1.affine)
nib.save(result_img, 'add/save/path/R2_prime.nii.gz')
