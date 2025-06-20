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
The first step of the pipeline was to register both MRI modalities to compute segmentation overlap. An initial misalignment was observed between the segmentations from the different modalities. To address this, a secondary region-of-interest (ROI) based registration was applied, improving alignment accuracy. The figure below illustrates this correction: red represents the MP2RAGE segmentation, green shows the initial DWI segmentation alignment, and blue depicts the DWI segmentation after ROI-based correction.

![Segmentation Alignment](results/segmentation_alignment.png)

Additionally, outlying values were identified near the edges of both manual segmentations. To ensure plausible values along the optic nerve, Regions of Interest (ROIs) were defined, as illustrated in the example figure below. 

![Segmentation Alignment](results/optic_nerve_roi.png)

### Segmentation Overlap Metrics Summary (whole optic nerve)
Segmentation overlap metrics showed moderate agreement between manual segmentations with Dice coefficients of 0.4961 ± 0.1703 and 0.3958 ± 0.1234 for subjects 1 and 2, respectively.
| Metric                          | Subject 1           | Subject 2           |
|--------------------------------|---------------------|---------------------|
| Number of slices analyzed       | 32                  | 22                  |
| Dice coefficient (mean ± std)   | 0.4961 ± 0.1703     | 0.3958 ± 0.1234     |
| Average overlapping voxels/slice| 20.8                | 19.0                |
| T1 values inside overlap (mean ± std, s) | 0.99 ± 0.13        | 0.99 ± 0.17        |
| FA values inside overlap (mean ± std) | 0.5886 ± 0.1408     | 0.4370 ± 0.1013     |
| Mean MTVF (mean ± std)          | 0.2736 ± 0.0278     | 0.2751 ± 0.0338     |
| Mean MVF (mean ± std)           | 0.1368 ± 0.0139     | 0.1375 ± 0.0169     |
| Mean FVF (mean ± std)           | 0.3486 ± 0.1594     | 0.2154 ± 0.0680     |
| Mean g-ratio (mean ± std)       | 0.7329 ± 0.1019     | 0.5781 ± 0.1614     |

### Results – MVF, FVF & g-Ratio
Plausibles results were obtained for regions of interest (ROIs) in the optic nerve, with calculated g-ratio values ranging between 0.6 and 0.8 for each subject. The calculated mean for each coronal slice includes both the right and the left optic nerves. 
#### Subject 1

![Subject 1 metrics](results/subject1_metrics.png)

#### Subject 2

![Subject 1 metrics](results/subject2_metrics.png)

## Conclusion and Acknowledgement
### Can we visualize the g-ratio value along the optic nerve?
Yes. Using the developed pipeline, we successfully mapped and visualized the g-ratio values along the optic nerve in a reproducible and non-invasive manner. This provides meaningful insight into myelin integrity and fiber composition in differents subjects.

### Tools that I learned during this project
* Python for data processing, scripting, and analysing
* Jupyter Notebooks to organize and run interactive data workflows
* ANTS (Advanced Normalization Tools) for medical image registration and transformation
* Git and GitHub for version control and project collaboration
* BIDS for standardization of the data structure

### Encountered issues
#### Atlas max probability optic nerve label
The [max probability optic nerve label](data/derivatives/templates) was initialy used to assess whether manual segmentation was truly necessary, or if this atlas-based label could serve as an automated segmentation alternative. Howerver, the Dice coefficient between the overlapping regions of both manual segmentations and the maximum probability atlas label ranged only from 15% to 20%. Given this low similarity, the maximum probability label was excluded from further analysis.

#### Registration issue
As previously stated, two registrations issues were encountered. The first was related to the small size (~4-5 voxels wide) and the natural curvature of the optic nerve. Non-affine or elastic registrations tended to deform the optic nerve and create hole in the transformed manual segmentation masks. The second issue involved the alignment of the two manual segmentations: a single rigid registration resulted in an approximate one-slice offset. However, applying a second rigid registration using ROIs was able to correct this initial misalignment.

#### MTVF vs MVF
Initialy, it was assumed that myelin constitutes nearly 100% of the macromolecular content in white mater like the optic nerve. This assumption led to an overestimation of the Myelin Volume Fraction (MVF) by Macromolecular Tissue Volume Fraction (MTVF), resulting in non-plausible results such as more myelin than fiber. An litterature search revealed that myelin accounts for only 50% of the macromolecular content in white matter. With this correction, plausible values of g-ratio were acheived. 

### Acknowledgement
I would like to thank Nikola Stikov and Agah Karakuzu for their mentorship and expertise, as well as Bas Roker and Ameen Qadi from the Rokers Vision Laboratory in NYU Abu Dhabi. Special thanks also to Eva Alonso Ortiz and Sebastian Rios, the professor and teaching assistant of the course, for their guidance and support.  

## References
Ausmed. (2025, 01). How Does Multiple Sclerosis Affect the Body? | Ausmed. https://www.ausmed.com/learn/articles/multiple-sclerosis-nursing-care
  
Barranco Hernandez, J., Luyken, A., Kebiri, H., Stachs, P., Macias Gordaliza, P., Esteban, O., Aleman Gomez, Y., Sznitman, R., Stachs, O., Langner, S., Franceschiello, B., & Bach Cuadra, M. (2024). Eye-Opening Advances: Automated 3D Segmentation, Key Biomarkers Extraction, and the First Large-Scale MRI Eye Atlas. https://doi.org/10.1101/2024.08.15.608051
  
Brainhack School. (n.d.). Training modules. Retrieved June 19, 2025, from https://school-brainhack.github.io/modules/
  
Duval, T., Stikov, N., & Cohen-Adad, J. (2017). Modeling white matter microstructure. Functional Neurology, 31(4), 217–228. https://doi.org/10.11138/FNeur/2016.31.4.217

Mezer, A., Yeatman, J. D., Stikov, N., Kay, K. N., Cho, N.-J., Dougherty, R. F., Perry, M. L., Parvizi, J., Hua, L. H., Butts-Pauly, K., & Wandell, B. A. (2013). Quantifying the local tissue volume and composition in individual brains with magnetic resonance imaging. Nature Medicine, 19(12), 1667–1672. https://doi.org/10.1038/nm.3390

MS Canada. (2025, February 7). Prevalence and incidence of MS in Canada and around the world | MS Canada. https://mscanada.ca/ms-research/latest-research/prevalence-and-incidence-of-ms-in-canada-and-around-the-world

MS Trust. (2024, 11). McDonald criteria | MS Trust. https://mstrust.org.uk/a-z/mcdonald-criteria

Naghizadeh, Y. (2025). Naghizadeh_project. https://github.com/brainhack-school2025/Naghizadeh_project

NeuroLibre. (n.d.). Retrieved June 19, 2025, from https://neurolibre.org

qMRLab. (n.d.). Home | qMRLab. Retrieved June 19, 2025, from https://qmrlab.org/

Rokers Vision Laboratory. (n.d.). Retrieved June 19, 2025, from https://sites.nyuad.nyu.edu/rokersvisionlaboratory/

State University of New York College of Optometry. (2019, December 11). Scientists Discover the Origin of Brain Mapping Diversity for Eye Dominance [Video]. SciTechDaily. https://scitechdaily.com/scientists-discover-the-origin-of-brain-mapping-diversity-for-eye-dominance-video/

Stikov, N., Campbell, J. S. W., Stroh, T., Lavelée, M., Frey, S., Novek, J., Nuara, S., Ho, M.-K., Bedell, B. J., Dougherty, R. F., Leppert, I. R., Boudreau, M., Narayanan, S., Duval, T., Cohen-Adad, J., Picard, P.-A., Gasecka, A., Côté, D., & Pike, G. B. (2015). In vivo histology of the myelin g-ratio with magnetic resonance imaging. NeuroImage, 118, 397–405. https://doi.org/10.1016/j.neuroimage.2015.05.023

Stikov, N., Perry, L. M., Mezer, A., Rykhlevskaia, E., Wandell, B. A., Pauly, J. M., & Dougherty, R. F. (2011). Bound pool fractions complement diffusion measures to describe white matter micro and macrostructure. NeuroImage, 54(2), 1112–1121. https://doi.org/10.1016/j.neuroimage.2010.08.068
