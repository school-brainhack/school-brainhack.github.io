---
type: "project" 
date: "2026-06-12" # D
# Title of your project (we like creative titles)
title: "Classifying Autism Spectrum Disorder Using Functional Brain Connectivity"

# List the names of the collaborators within the [ ].
names: [Issac Liu, Arshdeep]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2026/ASD_Classification


website:

# List +- 4 keywords that best describe your project within []. Please only lowercase letters.
tags: [asd, fmri, functional connectivity, machine learning, abide]

# Summarize your project i
summary: "This project uses resting-state fMRI data from the ABIDE dataset to classify individuals with Autism Spectrum Disorder (ASD) from typically developing (TD) controls using functional brain connectivity features and machine learning classifiers. Three classifiers (Ridge, SVC, MLP) were trained on correlation-based connectivity matrices derived from 116 brain regions, achieving up to 64% accuracy, validated with permutation testing."

# If you want to add a cover image (listpage and image on the right), add it to your directory and indicate the name below with the extension.
image: "fmri-autism.jpg"
---

## Project Definition

### Background

Autism Spectrum Disorder (ASD) is a neurodevelopmental condition associated with differences in how brain regions communicate with each other (Ecker et al., 2014; Hull et al., 2017). Research consistently shows that ASD brains exhibit altered functional connectivity — specifically reduced long-range communication between frontal and temporal regions involved in social cognition, and increased local connectivity in frontal areas associated with repetitive behaviours.

This project uses machine learning applied to resting-state fMRI data to classify ASD vs. typically developing (TD) individuals based on functional connectivity patterns, using the ABIDE preprocessed dataset.

### Tools

This project relied on the following tools:

- **Python** — primary programming language
- **Nilearn** — for fetching the ABIDE dataset and computing connectivity matrices
- **Scikit-learn** — for machine learning classifiers (SVC, Ridge, MLP) and evaluation
- **NumPy / Pandas** — for data manipulation
- **Matplotlib / Seaborn** — for visualisation
- **Jupyter Notebook** — for running and presenting the analysis
- **GitHub** — for version control and collaboration

### Data

Data was obtained from the [Autism Brain Imaging Data Exchange (ABIDE)](http://preprocessed-connectomes-project.org/abide/) preprocessed repository, accessed via Nilearn's `fetch_abide_pcp` function.

- **Subjects:** 752 participants (346 ASD, 406 TD), ages 6–25, from 20 sites
- **Atlas:** AAL (Automated Anatomical Labelling) — 116 brain regions (ROIs)
- **Features:** Resting-state fMRI time series per ROI, vectorised Pearson correlation matrices (6,670 features)

### Deliverables

At the end of this project, we have delivered:

- A Jupyter notebook (`ABIDE_classification.ipynb`) with the full analysis pipeline
- Functional connectivity matrices and visualisations for ASD vs. TD subjects
- Trained machine learning classifiers (SVC, Ridge Classifier, MLP)
- Evaluation metrics including accuracy, F1-score, confusion matrices, and permutation test results

## Results

### Overview

We successfully built an end-to-end pipeline from raw fMRI data to ASD classification. The pipeline fetches preprocessed ABIDE data, extracts functional connectivity features using the AAL atlas, trains three classifiers, and evaluates their performance.

### Tools Learned During This Project

- **Nilearn** — learned to fetch neuroimaging datasets and compute connectivity measures using `ConnectivityMeasure`
- **Functional connectivity analysis** — computing Pearson correlation matrices across 116 ROIs and vectorising them into feature vectors
- **Machine learning pipeline** — applying `StandardScaler`, train/test splits, cross-validation, `GridSearchCV`, and permutation testing
- **Neuroimaging concepts** — BOLD signal, brain atlases, ROIs, and resting-state fMRI

### Classifier Performance

| Classifier       | Accuracy | Notes                                |
|------------------|----------|--------------------------------------|
| Ridge Classifier | 64%      | Best performer; optimal alpha = 1000 |
| SVC              | 60%      | Support Vector Classifier            |
| MLP              | 56%      | Neural network; hidden layers = 300  |

### Permutation Test

All classifiers were validated using permutation testing (n=100 permutations), confirming results were statistically significant (p < 0.01) and not due to chance.

### Key Finding

Functional connectivity patterns derived from resting-state fMRI are partially predictive of ASD diagnosis, supporting the hypothesis that ASD is associated with atypical brain connectivity. The 64% accuracy reflects both the biological signal present in the data and the inherent complexity of ASD as a spectrum condition.

## Conclusion and Acknowledgement

This project demonstrates that resting-state functional connectivity contains detectable differences between ASD and TD individuals, consistent with the broader neuroimaging literature. However, the moderate accuracy (64%) highlights key challenges:

- **High dimensionality** — 6,670 features with only 752 subjects; feature selection may improve performance
- **Multi-site variability** — data from 20 different scanning sites introduces noise
- **ASD heterogeneity** — treating ASD as a single category ignores the spectrum's variability

Future work could explore feature selection methods, ASD subtype classification, and site harmonisation techniques to improve performance.

We thank the ABIDE team for making this dataset publicly available, and the BrainHack School instructors and TAs for their support throughout the project.
