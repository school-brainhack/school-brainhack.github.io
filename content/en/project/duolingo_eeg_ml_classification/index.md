# Brainhack-school-project

---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-10" # Date your first upload your project.
# Title of your project
title: "Predicting feedback perception in an online language learning task using EEG and machine learning"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Stephanie Fu, <a href="https://dylanscottlow.github.io/" target="blank">Dylan Scott Low</a>]

# Your project GitHub repository URL
github_repo: https://github.com/stephanie0404/Brainhack-school-project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [machine learning, duolingo, eeg, neurolinguistics, brainhack]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "In this project, we attempt to apply machine learning methods to the analysis of EEG data recorded while a participant completes language learning tasks on the popular online platform Duolingo. Specifically, we seek to determine if features in the EEG signal can serve to predict whether the participant has gotten a task right or wrong, at the moment when the participant receives feedback on their performance in the task. A k-nearest neighbours classifier achieves a 98% accuracy rate when predicting whether the participant got the answer right or wrong based on the EEG voltages from 8 electrodes."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "./Cz_sample_filtered.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

In recent years, new apps and products have been introduced based on the idea that machine learning techniques could be applied to EEG brainwaves in order to decipher a person's thoughts and generate statistics about the different kinds of thoughts a person has in a day (e.g, <a href="https://neurosity.co/" target="blank">Neurosity</a>; see also <a href="https://futurism.com/the-byte/ai-draws-decodes-brainwaves" target="">Houser, 2019</a>; <a href="https://www.youtube.com/watch?v=-HYbFm67Gs8" target="blank">Fireship, 2023</a>). Our motivation is to attempt to implement our own simple machine learning analysis on raw EEG data to discern cognitive activity, especially that related to language. We selected a dataset containing EEG data recorded while participants completed language learning tasks in the online platform, Duolingo (see "Data" below). Our main objectives in this project were to develop a pipeline for analysing EEG data (OpenBCI format) using open source tools like MNE Python and apply machine learning methods to the analysis. Our personal learning objectives were to make ourselves more familiar with EEG data analysis, the Python programming language and corresponding workflows, and other open source tools used in neurosciencce research.

The main question we asked in this project was: How can we use machine learning techniques to identify, based on EEG data, if the participant was receiving positive feedback (they got the learning task correct) or negative feedback (they got the learning task wrong) from Duolingo?

### Tools

The project relied on the following tools:
 * R programming language (packages: tidyverse, ggplot2, readr)
 * Python programming language (libraries: pandas, scikit-learn, MNE Python)
 * Git/GitHub
 * Bash terminal

### Data

The data we used comes from a project titled <a href="" target="blank"><b>Data in Brief: Multimodal Duolingo Bio-Signal Dataset</b></a> by Notaro & Diamond (2018; click <a href="https://doi.org/10.1016/j.dib.2018.11.044" target="blank">here</a> for the corresponding article). As suggested by the title, this is a multimodal dataset. Four kinds of data were recorded: (1) EEG via a low-cost OpenBCI electrode cap, (2) Gazepoint-GP3 eye-tracking, (3) Autohotkey cursor movements and clicks, and (4) Autohotkey screen content data (screenshots taken when a click occurs). Data was recorded while participants (n = 22) were completing beginner German language lessons on the desktop version of Duolingo. Participants were either English native speakers or fluent in English.

Our project focused on (1) and (4), that is, the EEG and screenshot data. In particular, we analyse only the data of participant 1.

### Deliverables

At the end of this project, these files will be available:
 * A .txt file (data_labels_raw.txt) containing manually selected filenames (timestamps) of the screenshots corresponding to when the participant receives feedback on their Duolingo performance.
 * An R script (data_labels.r) for cleaning the raw filenames list (data_labels_raw.txt) into machine-readable format (data_labels_clean.txt).
 * A Jupyter notebook containing Python script for preprocessing the OpenBCI EEG data (high and low pass filtering).
 * An R script (data_labelling.r) for combining the filtered EEG data with the data_labels_clean.txt file.
 * A Juyter notebook containing Python script for running machine learning classifiers (e.g., MLP, kNN, random forest) on the labelled EEG data.

## Results

### Progress overview

At first, we thought preprocessing the data would be a simple matter. However, we quickly realised that the OpenBCI EEG format (formatted as a .txt file) is not a standard raw EEG format that could be easily imported in MNE Python. Solving this problem caused us some delays, but we eventually came up with a custom script to import the data in MNE Python. Another peculiarity we observed was that the OpenBCI set-up only consisted of 8 electrodes, as opposed to the standard 32 channels.

Also, we initially intended to analyse the data of more than one participant in the data set, but realised that even data from one participant (recorded over about 58 minutes) was very large, and likely more than sufficient to train an ML model. The large size also delayed our work due to the long wait times when processing the data, sometimes leading to crashes which force us to start the process over again until it reaches fruition (an unfortunate symptom of running such analyses on weak personal machines).

### Tools we learnt during this project

 * **MNE Python**: We learnt how to filter raw EEG data during the preprocessing stage, as well as how to import EEG data even if not in a recognised standard raw format.
 * **Github workflow**: We got well-acquainted with using Git via the Bash terminal, and also some related tools like Datalad and Git LFS (Large File System).
 * **Bash Terminal**: We gained a good understanding of how to use the Bast erminal in lieu of File Explorer (Windows)/Finder (Mac).

### Results

#### Figures and Plots

##### Preprocessing
<img src="./Cz_sample_pre_filtered.png" alt="Unfiltered Cz Channel during 1 second epoch" width="300"> Unfiltered Cz Channel during 1 second epoch.

<img src="./Cz_sample_filtered.jpg" alt="Filtered Cz Channel during 1 second epoch" width="300"> Filtered Cz Channel during 1 second epoch.

<img src="./F3_sample_pre_filtered.png" alt="Unfiltered F3 Channel during 1 second epoch" width="300"> Unfiltered F3 Channel during 1 second epoch.

<img src="./F3_sample_filtered.jpg" alt="Filtered F3 Channel during 1 second epoch" width="300"> Filtered F3 Channel during 1 second epoch.

<img src="./pre_filtered_EEG_psd.png" alt="Power Spectral Density (PSD) plot for the unfiltered EEG" height="250"> Power Spectral Density (PSD) plot for the unfiltered EEG.

<img src="./filtered_EEG_psd.png" alt="Power Spectral Density (PSD) plot for the filtered EEG" height="250"> Power Spectral Density (PSD) plot for the filtered EEG.

<img src="./sensors_montage.png" alt="EEG cap sensor positions" width="300"> EEG cap sensor positions.

##### Machine Learning

<img src="./feature_importance_randomforest.png" alt="Feature Importance (Random Forest)" width="300"> Feature Importance (Random Foreest)

<img src="./cm_randomforest.png" alt="Confusion Matrix (Random Forest)" width="300"> Confusion Matrix (Random Forest)

<img src="./feature_importance_knn.png" alt="Feature Importance (kNN)" width="300"> Feature Importance (kNN)

<img src="./cm_knn.png" alt="Confusion Matrix (kNN)" width="300"> Confusion Matrix (kNN)

<img src="./feature_importance_logit.png" alt="Feature Importance (Logit)" width="300"> Feature Importance (Logit)

<img src="./cm_logit.png" alt="Confusion Matrix (Logit)" width="300"> Confusion Matrix (Logit)

<img src="./feature_importance_mlp.png" alt="Feature Importance (Multilayer Perceptron)" width="300"> Feature Importance (Multilayer Perceptron)

<img src="./cm_mlp.png" alt="Confusion Matrix (Multilayer Perceptron)" width="300"> Confusion Matrix (Multilayer Perceptron)

#### Discussion

The full results can be viewed in the Jupyter notebook <a href="https://github.com/stephanie0404/Brainhack-school-project/blob/main/scripts/ml_eeg_classifier.ipynb" target="blank">ml_eeg_classifier</a> in our GitHub repository. We briefly summarise the accuracy rates attained by each model below.

Random Forest:			0.8923478119142694

Logistic Regression:		0.5955504848830576

k-Nearest Neighbours:		0.9759595794963736

Multilayer Perceptron:		0.6984760818189226

A <i>prima facie</i> look will show that the k-Nearest Neighbours (kNN) classifier achieved the highest performance in accurately predicting whether the participant was looking at positive or negative feedback based on the EEG data. However, it is possible that the high accuracy rate may be due to overfitting, and more sophisticated evaluation metrics will need to be consulted (unfortunately, time limits prevent us from doing so here).

Future directions for this project could involve exploring more advanced machine learning techniques, such as deep learning models, to capture complex patterns in the EEG data. Additionally, incorporating other modalities available in the multimodal dataset, such as eye-tracking or cursor movements, could potentially enhance the prediction accuracy and provide a more comprehensive understanding of the cognitive processes during language learning.

## Conclusion and acknowledgement

In summary, this project provides a starting point for applying machine learning methods to EEG data analysis in the context of language learning. The results highlight the potential of using EEG features to predict certain cognitive tasks, but further research is required to refine this (admittedly) very coarse implementation and address the aforementioned limitations.

We humbly thank the Brainhack School Team for organising this fantastic learning journey, as well as all the instructors who developed the learning modules and corresponding video lectures/lessons. We would especially like to thank the Taiwan Hub team (National Taiwan University and National Central University) for all their support and encouragement.
