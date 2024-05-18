---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-05-18" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Functional Connectivity in Schizophrenia patients with and without Auditory Hallucinations"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Jagruti Pershad, Daisy Hu]

# Your project GitHub repository URL
github_repo: https://github.com/24jagruti11/Schiz_Auditory_hallucination.git


# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [Schizophrenia, fMRI, Auditory Hallucination, Functional Connectivity]

# Summary

summary: "This project focuses on examining if there are differences in the functional connectivity in schizophrenia with and without auditory hallucinations as well as healthy controls during speech perception. 
The data (OpenNeuro) (https://openneuro.org/datasets/ds004302/versions/1.0.1). 
71 participants were divided into 3 groups, Schizophrenia patients a) **with** auditory hallucination (AVH+), b) **without** auditory hallucination (AVH-) and Healthy Controls (HC)
They did a speech perception task when they were in a fMRI scanner.
Our aim was to learn preprocessing and analysis of fMRI data and getting familiar with machine learning."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "Ppt 1.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project 

### Background

This project uses machine learning to look at functional connectivity in schizophrenia patients with and without auditory hallucination during speech perception.
The data used is available on OpenNeuro (https://openneuro.org/datasets/ds004302/versions/1.0.1)
Since the underlying cause of auditory hallucinations in schizophrenia patients has not been found yet, we wanted to look at the functional connectivity of these individuals while they perform a speech perception task to examine the activity of different brain regions.

### Tools

The "project template" project will rely on the following technologies:
 * Downloading the data from OpenNeuro
 * SciNet teach cluster for the preprocessing of the data
 * Processing of fMRI data with nilearn


### Data

The data used is available on OpenNeuro (https://openneuro.org/datasets/ds004302/versions/1.0.1)

### Deliverables

At the end of this project, we will have:
 - Git repository
 - Codescript

## Results

### Progress overview

The project involved importing data on a github repository, using SciNet teach cluster for the preprocessing of the data and parcellation. Preprocessing involved running MRIQC to generate quality metric report, fMRIPrep for preprocessing of the data, Ciftify Clean for signal cleaning and Ciftify for the visualisation of the data. Parcellation helped to divide brain regions based on brain activty where groups of similar voxels are averaged to reduce the effect of random noise effects. Then, functional connectivity matrices were computed for all participants with complete data for 392 ROIs. Machine learning was used to classify diagnosis (healthy controls, patients with auditory hallucination, patients without auditory hallucination) based on functional connectivity matrices. Data for 67 participants went through reshaping, scaling, dimension reduction using PCA, and permutation testing a cross validation SVM (sklearn).

### Tools I learned during this project

 * Learning the basic mechanisms of Github
 * fMRI Data Processing with Nilearn
 * fMRI Data Visualization
 * fMRI Data Parcellation 
 * Machine Learning

### Results
The machine learning algorithm was not able to classify diagnosis based on functional connectivity.
