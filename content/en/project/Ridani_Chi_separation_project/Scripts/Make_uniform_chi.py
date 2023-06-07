####################################
# Filename: Make_uniform_chi.py
# Author: Daniel Ridani 
#
# Description: Script to make a uniform map of susceptibility. which means that within a region all voxel has the exact same value.
# Inputs
# ----------
# data_path : str
#     Path to the segmented model nifti file provided in simulation file.
# susceptibility values: float
#     Add your custimzed value for each region.
# save_path : str
#     Path to save the results
####################################
import nibabel as nib
import numpy as np

# Load the NIfTI segmentation file
seg_file = 'Path/to/SegmentedModel.nii.gz'
seg_img = nib.load(seg_file)
seg_data = seg_img.get_fdata()

# Define the region values lookup table
region_values = {
    1: value1,
    2: value2,
    3: value3,
    4: value4,
    5: value5,
    6: value6,
    7: value7,
    8: value8,
    9: value9,
    10: value10,
    11: value11,
    12: value12,
    13: value13,
    14: value14,
    15: value15,
    16: value16
}

# Assign values to each region in the segmentation
for region_num in range(1, 17):
    region_voxels = (seg_data == region_num)
    region_value = region_values.get(region_num, None)
    seg_data[region_voxels] = region_value

# Create a new NIfTI image with the modified segmentation data
modified_seg_img = nib.Nifti1Image(seg_data, seg_img.affine, seg_img.header)

# Save the modified NIfTI segmentation file
modified_seg_file = 'Add/path/to/save/results'
nib.save(modified_seg_img, modified_seg_file)

print("Modified segmentation file saved successfully.")
