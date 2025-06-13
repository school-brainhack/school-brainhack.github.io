For brainhack school TW-SG 2025

__bhfunc2025.py__ includes some functions are used in other code

__projectVisualizeTest.ipynb__ is the main processing steps I work on extracting the activities and images from preprocessed fMRI images

The exported csv files are plotted to bar graphs in __resultplotting.ipynb__

---
type: "project" 

date: "2025-06-12"

title: "Univariate analysis on melody evaluation test"

names: [Hsin-Yu Cheng]

github_repo: https://github.com/SkyStream5240/Hsin-YuCheng_project

tags: [auditory, fmri]

summary: "The project focused on extracting activities from functional images in a previous study about neural representation of melody-transposition. Using parcellated brain atlas as a mask, the BOLD signals underwent univariate analysis to look for effects in error detection or music-like stimulus-related brain regions/"

---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Inspired by the previous paper: Y.-­ A. Han and P.J. Hsieh Imaging Neuroscience, Volume 2, 2024 https://doi.org/10.1162/imag_a_00352. I want to understand how simple melody stimuli can induce neuronal activities in the brain.


### Tools

The __Univariate analysis on melody evaluation test__ project will rely on the following technologies:
 * jupyter notebook
 * python packages - nilearn and nibabel
 * nilearn.dataset - Spatially constrained parcellation: msdl_rois

### Data

Using the functional fMRI data in the previous paper: Y.-­ A. Han and P.J. Hsieh Imaging Neuroscience, Volume 2, 2024 https://doi.org/10.1162/imag_a_00352.
Will not be provided when the project is uploaded.

### Deliverables

At the end of this project, we will have:
 - comparison of activity in a set of parcellated brain regions

## Results

### Progress overview

The preprocessed image series went through masking and activities are extracted.

### Tools I learned during this project

 * **Github workflow** 
 * **dealing with Nifti data** 
 * **basic data visualization in seaborn** 

### Results

#### Deliverable 1: Comparison of activity difference 

Two subjects, one run each, are analyzed to look for the activation difference in dorsal ACC, dlPFC, and a generalized auditory region. <img width="317" alt="image" src="https://github.com/user-attachments/assets/247a787c-f099-485a-ad7d-fbc159b00b79" />
Expected effect are seen in one run of one subject but the other doesn't seem obvious.

<img width="301" alt="image" src="https://github.com/user-attachments/assets/88091782-5c86-4533-b52e-9b90b65d3185" />
<img width="311" alt="image" src="https://github.com/user-attachments/assets/9be9241c-9e34-490a-b75d-aabe95c8ff7d" />
<img width="297" alt="image" src="https://github.com/user-attachments/assets/c4a09939-0352-42fa-a922-22e0e70bc367" />

<img width="310" alt="image" src="https://github.com/user-attachments/assets/b8f49aa2-2051-4142-ba4a-da26bfe8c6ca" />
<img width="311" alt="image" src="https://github.com/user-attachments/assets/c6a9d909-0279-48ee-a6a5-216ee57426d5" />
<img width="305" alt="image" src="https://github.com/user-attachments/assets/5f650b49-855b-483c-b6cc-0ac8a21ff745" />


## Conclusion and acknowledgement

We can see the brain activity in different regions vary a lot in different individuals, even in identical test runs. More data needs analysis for a further, more general conclusion. 

(You can also make submit your project to neurolibre https://neurolibre.org/. It is a preprint server for interactive data analyses. It is tailored for publishing interactive neuroscience notebooks that can seamlessly integrate data, text, code and figures.The submission instructions can be found here https://docs.neurolibre.org/en/latest/index.html and the jupyter book docs there https://jupyterbook.org/intro.html.)
