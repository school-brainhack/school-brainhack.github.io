---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-20" # Date you first upload your project.
# Title of your project (we like creative title)
title: "g-Ratio mapping of the optic nerve"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Hugo Albert Plante]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2025/albert-plante_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website: 

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [g-ratio, qmri, dmri, multiple sclerosis]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..
summary: "This project aims to accurately compute the optic nerve g-ratio, a key neuroimaging marker reflecting myelin integrity in nerve fibers. Using advances quantitative MRI techniques, it analyses the human optic nerve’s microstructure non-invasively. By integrating MP2RAGE and diffusion MRI, it seeks to improve assessment of myelin and nerve health, contributing to better understanding, early detection, and diagnosis of neurological diseases like multiple sclerosis (MS).."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "brain_anatomy_eye.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Introduction
This project focuses on quantifying myelin integrity in the optic nerve using multimodal MRI. Multiple Sclerosis (MS) causes degradation of the myelin sheath surrounding nerve fibers, impairing neural communication (Ausmed, 2025). Measuring key parameters such as the **g-ratio**, **Myelin Volume Fraction (MVF)**, and **Fiber Volume Fraction (FVF)** enables better understanding and monitoring of demyelination. 

Using MRI-derived maps like T1 and FA, this project aims to compute these metrics non-invasively, providing valuable insights for research and clinical applications in neurological disorders like MS.

### Background

#### Multiple Sclerosis and Neuronal Structure
Multiple sclerosis (MS) is an autoimmune disease that affect 2.8 millions peoples worldwide, as of 2020 (MS Canada, 2025). This disease occur when the body’s immune system mistakenly attack the myelin sheath, causing demyelination. A common early symptom of multiple sclerosis is optic neuritis, but as of 2024, it has also become a McDonald criteria for diagnosing MS (MS Trust, 2024). 

#### g-Ratio: A key Metric in Myelin Studies
the g-ratio is a crucial parameter for quantifying the relative thickness of the myelin sheath. It is defined as the ratio between the inner axonal radius (r) and the outer myelinated radius (R) of a nerve fiber:

$$g=\frac{r}{R}$$

This ratio provides insight into myelin integrity and neuronal health. 

#### Volume Fractions and their significance
* **Myelin Volume Fraction (MVF)** represents the proportion of myelin in a given tissue volume.
* **Fiber Volume Fraction (FVF)** represents the proportion of nerve fibers (axons plus myelin) in a given tissue volume. 
* **Macromolecular Tissue Volume Fraction (MTVF)** represents the proportion of macromolecules (including myelin) in a given tissue volume.
* The relation between MVF and FVF relates directly to the g-ratio (Stikov et al., 2015):

$$\frac{MVF}{FVF}=1-g^2$$

Using two MRI modalities, MVF and FVF can be calculated non-invasively.
#### Imaging Techniques and Quantitatives Maps
* Macromolecular Tissue Volume Fraction is used as an indirect measure of myelin content. In white matter like the optic nerve, myelin composition approximatively 50% of MTVF (Mezer et al., 2013). It has been shown that MTVF can be derived from the actual value of T1 in an MRI voxel (Mezer et al., 2013):

$$\frac{1}{1-MTVF}=\frac{0.44202}{T1}+0.94766$$

* Fractionnal Anisotropy (FA) obtained from diffusion MRI, has shown have a quadratic relation FVF through simulations (Stikov et al., 2011):

$$FVF=0.883{FA}^2-0.082FA+0.074$$

These imaging-derived metrics allow assessment of neuronal integrity and demyelination in diseases like MS. 

### Objectives
* Develop a pipeline for mapping the g-ratio of the optic nerve
* Co-register MP2RAGE, DWI, and their derivatives to a common space (MNI 152)
* Compute g-ratio, MVF, and FVF from segmentations
* Calculate the mean g-ratio along each coronal slice of the optic nerve

### Tools
* Jupyter notebooks for scripting
* BIDS standards for reproducibility and standardization
* Python for data vizualisation
* dMRI module and Spinal Cord Toolbox for inspiration and understanding
* BASH for automation
* **ANTs for image registration**
* 3D Slicer and FSLeyes for image visualization and ROI definition 
* Git and GitHub for Version Control
* Python Packages: 'matplotlib', 'nibabel', 'pandas', 'numpy'

### Data
The data used in this study comes for NYU Abu Dhabi (private dataset), where the MP2RAGE and Diffusion MRI acquisitions were performed on 9 healty subjects. Manuals segmentations of the optic nerve were also perfromed for both modalities to extract the relevant MRI metrics.

For each subject, the dataset includes:
* A raw MP2RAGE image for T1 map extraction
* A denoised and defaced MP2RAGE UNI image
* A DWI b0 image for registration purposes
* A Fractional Anisotropy (FA) map obtained from a Siemens scanner
* Manual segmentations from both MRI modalities

A supplementary critical part of the project was the analysis of a maximum probability label for the optic eye comming form (Barranco Hernandez et al., 2024). The goal of this integration was to determine wether the maximum probability label could be used as a automated segmentation alternative to manual segmentations. 

### Deliverables
* A non-invasive method for mapping the g-ratio along the optic nerve
* An executable, reproducible pipeline that tales multimodal MRI as an input and outputs the mean g-ratio along the optic nerve
* Jupyter Notebooks for data visualization and statistical metrics extraction

## Results
Segmentation overlap metrics showed moderate agreement between manual segmentations with Dice coefficients of 0.4961 ± 0.1703 and 0.3958 ± 0.1234 for subjects 1 and 2, respectively. Mean g-ratio values ranged between 0.6 and 0.8 across the optic nerve ROIs. Registration involved rigid and affine steps to align DWI and MP2RAGE images, with a secondary rigid ROI-based correction to address initial misalignment. The maximum probability optic nerve atlas label was excluded due to low similarity with manual segmentations (Dice 15–20%).


## Conclusion and Acknowledgement
