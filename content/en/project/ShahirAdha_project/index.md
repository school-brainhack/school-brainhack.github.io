---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-12" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Decoding Perceived Emotion from BOLD data using Machine Learning"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Muhammad Shahir Adha]

# Your project GitHub repository URL
github_repo: (https://github.com/MShahirAdha/Adha_project/tree/main)

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [emotion, machine learning, fmri, perception]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project applies machine learning to decode perceived emotions from fMRI data using ROI-based features. Data from the ds003548 OpenNeuro dataset are analyzed, with task labels extracted from events files. ROI time series are extracted using the MIST 64-ROI atlas, and mean signals during emotion blocks are classified using linear SVM. The goal is to distinguish between six conditions (happy, sad, angry, neutral, blank, scrambled), demonstrating key concepts and challenges in neuroimaging-based classification."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "confusion_matrix_test.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Understanding how the brain processes emotions is a central challenge in cognitive neuroscience. Functional Magnetic Resonance Imaging (fMRI) allows researchers to non-invasively measure brain activity during emotional tasks, but traditional univariate methods often miss the distributed nature of neural representations.

This project uses multivariate pattern analysis (MVPA) to decode emotional states from fMRI data in the OpenNeuro dataset ds003548. Participants viewed emotional and non-emotional face stimuli across several runs. Smoothed, denoised BOLD images were used to extract region-wise average signals based on the MIST 64-region functional atlas. A linear Support Vector Machine (SVM) was trained to classify six conditions: happy, sad, angry, neutral, scrambled, and dim. This approach demonstrates how machine learning can reveal distributed emotion-related patterns in the brain.

### Tools

The project will rely on the following technologies:
 * Python: nibabel, pandas, numpy, scikit-learn, nilearn, matplotlib
 * Adding the project to the website relies on github, through pull requests.

### Data

This project uses publicly available fMRI data from the OpenNeuro dataset ds003548, titled "Emotion Category and Face Perception Task Optimized for Multivariate Pattern Analysis". The dataset includes BOLD fMRI scans from participants viewing emotional and non-emotional face stimuli across multiple runs.

Preprocessing was performed using fMRIPrep, and the analysis uses smoothed, denoised BOLD images in MNI space. Task condition labels were extracted from events.tsv files, and brain activity was summarized using the MIST 64-region functional atlas.

### Deliverables

At the end of this project, we will have:
 - The current markdown document, completed and revised.
 - Model test accuracy results and confusion matrix
 - Jupyter notebook code

## Results

### Progress overview

This project was developed as part of BrainHack School 2025. I adapted material from the tutorials to perform emotion classification using fMRI data from the OpenNeuro ds003548 dataset. The pipeline includes data loading, ROI-based feature extraction, and machine learning classification using a linear SVM. The process was straightforward, and community feedback may help refine future iterations.

### Tools I learned during this project

 * **fMRI analysis** I learned how to work with BIDS-formatted fMRI data, use nibabel and nilearn to load and process brain images, and apply ROI-based feature extraction using the MIST 64 atlas.
 * **Machine Learning for Neuroimaging** I applied scikit-learn to perform classification using a linear SVM, using cross-validation strategies suited for subject-level generalization.
 * **GitHub & Collaboration** I practiced using GitHub for project version control and learned how to structure a project for reproducibility and collaboration.

### Results

#### Deliverable 1: Jupyter Notebook code

A Jupyter notebook containing my entire project pipeline, with additional exploratory analyses, is included in the repository.

#### Deliverable 2: project results

The model achieved an overall accuracy of 51.5% on the test data. It model performs very well in identifying control conditions like Blank and Scrambled images, with over 90% accuracy. However, the model struggles more with the emotional categories. For example, Angry is correctly classified only 30% of the time, Happy 23%, Neutral 20%, and Sad performs somewhat better at 47%.
These lower accuracies likely reflect the more subtle and overlapping neural signatures of emotions, making them more challenging to distinguish.


## Conclusion and acknowledgement

This project highlights the applications of MVPA on neuroimaging data to predict perceived emotion. Thanks to all Brainhack School collaborators from NTU SG and NTU TW for the wonderful learning opportunity!
