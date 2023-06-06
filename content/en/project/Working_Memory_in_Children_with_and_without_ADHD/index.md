---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-05-21" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Working Memory in Children with and without ADHD"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Wei-Chen Chang, Shan-San Huang]

# Your project GitHub repository URL
github_repo: https://github.com/wcnoname5/BHS2023_Project_ADHD

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/wcnoname5/BHS2023_Project_ADHD), click `manage topics`.
# Please only lowercase letters
tags: [adhd, fmri, connectivity, behavioral]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project aims to using both fMRI data and the behavioral data during a n-back task to compare the difference between ADHD children and the heathly control ones."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Attention deficit hyperactivity disorder (ADHD) is characterized by inattention, impulsivity, and hyperactivity (American Psychiatric Association, 1994). ADHD is a relatively common disorder in children, but with high diagnostic heterogeneity (Hammer et al., 2015).
In past researches, ADHD is found to associated with an impaired function of the frontal lobe (Rubia et al., 1999). Furthermore, researchers have found neuroimaging-based biomarkers of ADHD using MRI (Johnston et al., 2014; Lim et al.). Thus we want to use fMRI data from open source data to analyze the difference between ADHD and the healthy childrens. 

### Tools

 The "ADHD" project would have two parts of analysis, behavioral data and funtional images. 
 * `datalad`, which is used for download the dataset.
 * Some simpe `bash` scripts used to fetch the data in interest.
 
 For behavioral data analysis, the following tools was used:
 * `pandas` is used to cleaning and reconstructing the data.
 * `statsmodels.api` is used to perform statistical analysis (2-way ANOVA).
 * `matplotlib` and `Seaborn` are used to visualize the data.

 And for fMRI data analysis, the following tools was used:
 * `fmriprep`, a python-based package is used to preprocessing the functional images.
 * `nilearn`, which is used to visualize the brain images and analyze the connectivity 

### Data

The dataset is from OpenNeuro 
[Working Memory and Reward in Children with and without Attention Deficit Hyperactivity Disorder (ADHD)](https://openneuro.org/datasets/ds002424/versions/1.2.0), and is fetched using `Datalad`. The files structures is saved in `data/ds002424/` which is connected to Github site of the original study.

### Results

#### Deliverable 1: bash scripts
There're 3 bash scripts helps to deal with the data, which are:
 * `download_anat.sh` is used to get all the interested anatomical images in current project via `datalad`.
 * `download_VLD_VLI.sh`: is used to get all the interested functional images via `datalad`.
 * `fmriprep_singSubj.sh`: is used to perform the fMRI preprocessing for single subject via `fmriprep-docker`. This script is actually downloaded and modified from the [Andy's Brain Book's tutorial](https://github.com/andrewjahn/OpenScience_Scripts).

#### Deliverable 2: behavioral data analysis 
In the `Behavioral_Analysis` folder, there're files including:
 * `Behavioral_Analysis.ipynb`: a jupyter notebook go through the behavioral data analysis we've performed.
 * Lots of `.csv`s: the behavioral data used during analysis.
 * Lots of`.png`s: the results for statistical analysis and the visualization.

#### Deliverable 3: fMRI analysis results 
In the `fMRI_Analysis` folder, there're files including:
 * `Analysis.ipynb`: a jupyter notebook that go through the fMRI data analysis, including visualiztion, connectivity, and connectomes.
 * `result_figs/`: A directory that stores all the result figures.

## Conclusion and acknowledgement

In the beginning, we want to build a model to classify the ADHD and healthly controls using the machine learning technique. But the preprocessing of the fMRI data took longer than we expected. (We've spending loads of time dealing with countless problems, and eventually find out how to preprocess the fMRI data with `fmriPrep`.

At that point, we’re running out of time, so we decided to look into the connectivity to see if there is any difference between the ADHD child and Healthy control. Also we have practiced our skills on drawing plots with Python, like using `matplotlib` and `Seaborn`.
For future, we could try out and apply machine learning technique on the dataset.

Thanks all the TAs and Teachers and students all contributing to Brainhack School!
