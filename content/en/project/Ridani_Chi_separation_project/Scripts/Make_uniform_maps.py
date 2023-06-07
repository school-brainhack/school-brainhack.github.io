####################################
# Filename: Make_uniform_maps.py
# Author: Daniel Ridani 
#
# Description: Script to make a uniform map that will use such as M0, R1 and R2*. which means that within a region all voxel has the mean value of this region. 
# Note: In this script you will notice that I used the term T1 for most of the variable. But you can use it on any map.
# Inputs
# ----------
# data_path : str
#     Path to the segmented model nifti file provided in simulation file.
# data_path : str
#     Path to the desired map you want to transform
# save_path : str
#     Path to save the results
####################################
import nibabel as nib
import numpy as np

# Load the T1-weighted image
t1_file = 'Path/to/map'
t1_img = nib.load(t1_file)
t1_data = t1_img.get_fdata()

# Load the segmentation file
seg_file = 'Path/to/SegmentedModel.nii.gz'
seg_img = nib.load(seg_file)
seg_data = seg_img.get_fdata()

# Get the unique region labels in the segmentation
region_labels = np.unique(seg_data)

# Create a new array to store the modified T1 image
modified_t1_data = np.zeros_like(t1_data)

# Iterate over each region label
for region_label in region_labels:
    if region_label == 0:
        continue  # Skip background label

    # Find the voxels corresponding to the current region label
    region_voxels = (seg_data == region_label)

    # Calculate the mean value of the T1 image within the region
    mean_value = np.mean(t1_data[region_voxels])

    # Assign the mean value to the corresponding region in the modified T1 image
    modified_t1_data[region_voxels] = mean_value

# Create a new NIfTI image with the modified T1 data
modified_t1_img = nib.Nifti1Image(modified_t1_data, t1_img.affine, t1_img.header)

# Save the modified T1 image as a new NIfTI file
modified_t1_file = 'Add/save/path'
nib.save(modified_t1_img, modified_t1_file)

print("Modified image saved successfully.")
