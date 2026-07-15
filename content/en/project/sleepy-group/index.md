---
type: "project" # DON'T TOUCH THIS ! :)
date: "2026-06-19" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Understanding Sleep vs Wake Brain Connectivity Using Simultaneous fMRI and EEG"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Grace Burns, Alena Ionova, Gaithtry Rameswaran, Talia Fiaani]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2026/sleep_group_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [project, github, multimodal, brainhack, fmri, eeg, sleep]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: This project investigates how resting-state functional connectivity differs between sleep and wake states using simultaneous EEG and fMRI data from the OpenNeuro "Simultaneous EEG and fMRI signals during sleep from humans" dataset. By comparing default mode network connectivity and EEG frequency-band connectivity across states, the project found minimal differences at the network level but a reliable increase in theta-band connectivity during sleep, highlighting the value of combining modalities to characterize state-dependent brain connectivity.

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "sleeping_eeg_signal.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Functional connectivity in the brain is how different regions of the brain synchronously activate to perform certain tasks. Resting State Functional Connectivity (RSFC) is a measure often used in neuroscience research to characterize this brain connectivity at rest, which can be useful in understanding which regions are communicating with each other, and if there are any disturbances to these connections. 
Traditionally, RSFC is measured during an awake but relaxed state, however, this may not always be possible in certain populations like young children and is therefore sometimes done during sleep. 
In this project we investigate how RSFC differs between asleep and awake states using both electroencephalography (EEG) and functional Magnetic Resonance Imaging (fMRI), two common neuroimaging modalities. 
Both tools give us an understanding of brain function, but through different modalities. EEG measures the electrical activity of the brain, while fMRI measures brain activity indirectly through the Blood-Oxygen-Level-Dependent (BOLD) signal, which measures oxygenated and deoxygenated blood in different regions of the brain. 

Sleep stages are reflected in distinct EEG frequency patterns, so EEG helps identify whether the brain is in a wake-like, NREM-like, or transitional state, something fMRI alone cannot distinguish. 
Subjects do commonly fall asleep during resting-state fMRI scans, likely due to the lack of stimulation and task demands (Tagliazucchi and Laufs, 2014), which has motivated the use of simultaneous EEG or eye-tracking alongside fMRI. 
As EEG is sensitive to sleep stage in a way that fMRI is not, combining both modalities will allow us to more confidently characterize brain states and ask whether connectivity patterns measured with fMRI are mirrored in the EEG signals. 

### Tools

For this project, fMRI data were analyzed using FSL and Nilearn in Python, while EEG processing and analysis were carried out using MATLAB with EEGLAB/AMRI toolboxes and MNE-Python. Jupyter notebooks were used to organize and run the analysis pipelines, with GitHub used for code sharing and version control. Together, these tools allowed us to preprocess multimodal data, calculate EEG frequency and connectivity measures, and compare brain network patterns across sleep and wake states.

### Data

The OpenNeuro dataset “Simultaneous EEG and fMRI signals during sleep from humans” is an open-access multimodal sleep dataset collected from 33 healthy young adults (mean ages 22.1; 17 male/ 16 female) at Pennsylvania State University. Participants completed two resting-state scans and several sleep sessions, with simultaneous EEG, fMRI, and structural MRI data collected during different brain states. The dataset also includes EEG sleep staging performed by a registered polysomnographic technologist, making it useful for comparing brain connectivity during wake/rest and sleep states (classifying epochs as wake, N1, N2 or N3). The fMRI data was already preprocessed. OpenNeuro link to access data: https://openneuro.org/datasets/ds003768/versions/1.0.13 

### Deliverables

At the end of this project, we created:
 - Preprocessed EEG data from all 33 participants including removal of MRI interference and movement correction. 
 - Github repository containing the full code analysis and scripts including preprocessing and connectivity analysis.
 - A results breakdown including network comparison (group level).
 - Connectivity matrices (group level and individual level).
 - Frequency connectivity matrices (group level).

## Results

### Progress overview

Over the four weeks, we developed and ran an analysis pipeline comparing sleep and wake resting-state connectivity using fMRI and EEG. 

### Tools we learned and used during this project

 * **Terminal:** running code in the terminal
 * **Python:** all scripts are written in python
 * **Jupyter notebook:** all scripts were prototyped/ run in jupyter notebook
 * **Git and GitHub:** for version control and open access
 * **fMRI specific tools used:** FSL, NiLearn (python)
 *  **EEG specific tools used:** MatLab - EEGLab/ AMRI Toolboxes, MNE python

### Results

#### Deliverable 1: GitHub Repository

The GitHub repository contains the full code analysis and scripts used for preprocessing, connectivity analysis, and results generation, including the network comparison, connectivity matrices, and frequency connectivity matrices described above [here](https://github.com/brainhack-school2026/sleep_group_project) .

#### Deliverable 2: Final Presentation

You can check out our consolidated results explained in our [final presentation slide deck](https://docs.google.com/presentation/d/1MpFA_dsS9CCAzxvj50GzfHXu-GUe8yn-H_Zna1hJcV8/edit?usp=sharing)

## Conclusion and acknowledgement

This project achieved a full analysis of both fMRI and EEG data, comparing connectivity between sleep and wake states. While fMRI network-level comparisons showed no significant differences between states, EEG frequency-band analysis revealed that theta-band connectivity was reliably higher during sleep than during wake, as well as higher than sleep delta and beta rhythms. 

Thank you to the BrainHack School organizers and Toronto mentors, Dr. Erin Dickie, and TAs for their guidance throughout the course. 
