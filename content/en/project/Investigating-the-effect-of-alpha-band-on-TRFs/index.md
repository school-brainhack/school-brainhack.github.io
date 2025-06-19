---
type: "project" # DON'T TOUCH THIS ! :)
date: "2024-06-25" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Investigating the effect of alpha band on TRFs"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Kuan-Yu Chen, Ruo-Chi Yao, Liang-Mei Lin, Ming-Feng Hsin]

# Your project GitHub repository URL
github_repo: https://github.com/Aiame/2024_brain_hack_school_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [eeg, github, eelbrain, python]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "In our study of three participants, removing the alpha band affected TRFs, with some features being suppressed and others enhanced. This simplification highlighted local signals, making brain activity clearer. However, it's unclear if these enhanced signals represent true brain activity or noise, requiring further analysis for validation."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "S38_TRFs.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
The alpha band (α-wave) is a type of brainwave with a frequency range of approximately 8 to 12 Hz, often associated with relaxation and closed-eye states. Temporal Response Functions (TRFs) are models used to analyze the brain's response to time-series stimuli, particularly in the context of speech processing. 

Given our interest in understanding whether α-waves influence TRFs during language processing, our project aims to explore the impact of including or excluding α-waves on TRFs. Using an open dataset, we seek to determine how the presence or absence of α-waves affects the modeling and interpretation of neural responses in speech processing.

## Data
### Stimuli
For the EEG recordings in the Alice Dataset, participants listened to the first chapter of "Alice’s Adventures in Wonderland." This chapter consists of 2,129 words arranged into 84 sentences, with an average sentence length of 25.8 words (SD = 24.2). The total duration of the audio is approximately 12.4 minutes.

###　Participants

The study included 49 adult participants who were native English speakers, aged between 18 and 29, with 14 males in the group. All participants reported having normal hearing and no neurological disorders.

### Procedure
Participants were equipped with 61 actively-amplified electrodes plus one ground electrode (actiCap, Brain Products GmbH), arranged according to the Easycap M10 layout for uniform scalp coverage. During the experiment, the audiobook was played at a volume set 45 dB above the participant’s hearing threshold. After the audio session, participants completed an eight-question multiple-choice quiz about the story. The experimental session took between 1 to 1.5 hours to complete.

In our project, 3 EEG data sets were chosen randomly.
This repository offer the analyzed TRF, you might want to download because running the analysis from scratch could be time consuming


### Tools
The dataset processing by using mne-python

### Workflow
-- download data from the Alice repository and run estimate_trf script to get the processed data

-- use the raw data to do ICA, remove the reaction of alpha band and save as a new fif

-- run estimate_trf again to get the removed alpha data

![procedure](https://github.com/Aiame/2024_brain_hack_school_project/assets/127302047/02da82a1-8a8f-471f-b1e0-2bd33666e010)

## Results
subject 13
![output1](https://github.com/Aiame/2024_brain_hack_school_project/assets/127302047/59d47fd7-c0da-46c0-95d3-c3bede280c8b)
subject 18
![output2](https://github.com/Aiame/2024_brain_hack_school_project/assets/127302047/f506544d-c1b5-43d7-ba86-0e52ab8b5b2d)
subject 38
![output](https://github.com/Aiame/2024_brain_hack_school_project/assets/127302047/1746d269-7fec-4b13-ab4d-1a6ebcfe9f49)

## Conclusion and acknowledgement
In our study of three participants, removing the alpha band affected TRFs, with some features being suppressed and others enhanced. This simplification highlighted local signals, making brain activity clearer. However, it's unclear if these enhanced signals represent true brain activity or noise, requiring further analysis for validation.

### Reference
Alice dataset: https://github.com/Eelbrain/Alice/tree/main

Bhattasali, S., Brennan, J., Luh, W. M., Franzluebbers, B., & Hale, J. (2020). The Alice Datasets: fMRI & EEG observations of natural language comprehension. In Proceedings of the Twelfth Language Resources and Evaluation Conference (pp. 120-125).

