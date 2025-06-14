---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-09" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Replication Analysis of Brain Correlates of Speech Perception in Schizophrenia Patients with and without Auditory Hallucinations"

# Your project GitHub repository URL
github_repo: https://github.com/FuelToast/timtan_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI, FSL, fMRIPrep, git]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Timothy Tan]

summary: "An attempt to replicate the study by Soler-Vidal et al. (2022), using the study's dataset available on OpenNeuro. Attempted preprocessing of the first participant, sub-01,  using FSL (FEAT files in 'sub-01' folder) and fMRIPrep (material found in 'code' and 'derivatives' folders). Attempted creation of timing files, found in 'Ideal_Time_Series' folder."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "cover.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

I took up the HP4210 Data Aanalytics for Neuroimaging module in NTU Singapore, which led me to learn materials from the Brainhack School. As I studied along the brainhack school tutorials, I decided on doing research on schizophrenia, coming across a dataset avalable on OpenNeuro. This dataset is titled "Brain correlates of speech perception in schizophrenia patients with and without auditory hallucinations", where the dataset was used for a research study of the same name. As I am a beginner in handling fMRI data, I attempted to replicate the study's findings.


### Tools

The tools I used for this project are the following:
 * git and GitHub
 * WSL Docker, Jupyter Notebook and Visual Studio Code (miniconda3 and Python)

### Data

This project was made possible thanks to the available dataset on OpenNeuro, as linked [here](https://openneuro.org/datasets/ds004302/versions/1.0.1). To learn more about the study by Soler-Vidal et al. (2022) that I attempted to replicate, check [here](https://doi.org/10.1371/journal.pone.0276975).

### Deliverables

In my attempt to replicate the study, I aimed to have:
 - Preprocessing of raw fMRI data
 - First-Level Analysis
If I was able to conduct first-level analysis, I would attempt to do second-level analysis.

## Results

### Progress overview

I officially started this project on 25th May, after finalising and clarifying my goals for the project based on my project pitch. Over the course of 2 weeks until presentation date (10th June), I worked on this project step-by-step through online material that guided me on conducting preprocessing of raw fMRI data and subsequent analysis procedures. I modified the preprocessing and analysis steps according to the study that I was replicating.

### Tools I learned during this project

 * **git-annex** Used to fix broken symlinks after cloning the dataset from OpenNeuro.
 * **FSL** Used to pre-process the data and attempt to create first-level analysis.
 * **fMRIPrep** Used to automatically pre-process data and create first-level analysis with default parameters.

### Results

#### Deliverable 1: Preprocessing of raw fMRI Data

I used FSL's modules, BET and FEAT to preprocess the dataset. The preprocessed results can be found in the folder directory 'sub-01/run1.feat'.

I also used fMRIPrep to automatically preprocess the data, but the preprocessed results were incomplete due to unidentified errors. Incomplete preprocessing results are found in the 'derivatives' folder, with the code used to run fMRIPrep found in the 'code' folder.

#### Deliverable 2: First-Level Analysis

I was unable to produce first-level analysis results as I encountered errors while using FSL and fMRIPrep.
In my attempt to produce first-level analysis results with FSL, I created timing files based on the time series provided by the 'task-speech_events.tsv' file. The timing files can be found in the 'Ideal_Time_Series' folder.


## Conclusion and acknowledgement

I enjoyed picking up many new practical skills as part of this project, my first foray into neuroscience. Although I was unable to get the results I wanted during this project's timeframe, I still intend to progress on my own to better understand how data analysis procedures operate when it comes to fMRI data.

Thanks once again to authors of the dataset for making it available [here](https://openneuro.org/datasets/ds004302/versions/1.0.1) at OpenNeuro and for their study that I based my replication on [here](https://doi.org/10.1371/journal.pone.0276975).

Soler-Vidal, J., Fuentes-Claramonte, P., Salgado-Pineda, P., Ramiro, N., García-León, M. Á., Torres, M. L., Arévalo, A., Guerrero-Pedraza, A., Munuera, J., Sarró, S., Salvador, R., Hinzen, W., McKenna, P., & Pomarol-Clotet, E. (2022). Brain correlates of speech perception in schizophrenia patients with and without auditory hallucinations. PloS one, 17(12), e0276975. https://doi.org/10.1371/journal.pone.0276975
