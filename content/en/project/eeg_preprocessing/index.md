# BrainHack School 2023 Project 
## EEG Preprocessing in Python

# Project Definition
## Background
This project aims to do a pre-processing of an open dataset regarding an auditory oddball effect. We selected the dataset from OpenNeuro which contain 13 participants. Pure tones with respectively 500 Hz (standard) and 1000 Hz (oddball), as well as a 1000 Hz white noise distractors, are presented to the participants to examine their neural responses in the oddball task.

We will mainly focus on the pre-processing of the open dataset using MNE-Python package. The pre-processing will include handling bad channels, filtering, artifact detection, and repairing artifact with ICA. We aim to show the pipeline of data pre-processing with data visualization in a Jupyter notebook.

## Tools
- MNE-Python
- jupyter notebook

## Data
EEG data from an auditory oddball task (an open dataset accessed via OpenNeuro)

Link to the open dataset: https://openneuro.org/datasets/ds003061/versions/1.1.2

Dataset description:
- 13 subjects
- 3 identical sessions (13 min each)
- 750 stimuli
    - 70% standard (500 Hz pure tone, 60 ms)
    - 15% oddball (1000 Hz pure tone, 60 ms)
    - 15% distractors (1000 Hz white noise, 60 ms)
- Respond to oddball by pressing a key

## Deliverables
- A GitHub repository for our project (BHS_EEG_Preprocessing)
- A markdown file for the project description (README.md)
- A jupyter notebook presenting our preprocessing steps and results (EEG_preprocessing_oddball_task.ipynb)

# Results
## Progress overview
Our current progress includes reading the raw data of the open dataset, selecting subset of the channels, visualizing the sensor locations, referencing, filtering, extract events using annotations, creating epochs for the events, creating evoked data, and wrapping the previous steps into a pre-precessing function, and then finally loop over all 13 subjects to visualize the results between the standard and the oddball condition.

## Tools I learned during this project
- EEG Preprocessing steps
- MNE-Python: We mainly use this package to do the preprocessing of our EEG data
- OpenNeuro: We learnt how to find and use open datasets
- GitHub Workflow: We learnt version control and collaboration using Git & GitHub


