---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-15" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Partial Replication of 'Identification of Major Psychiatric Disorders From Resting-State Electroencephalography Using a Machine Learning Approach' Paper"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Jerome Wee]

# Your project GitHub repository URL
github_repo: https://github.com/ConnoisseurJDW/Wee_Project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.


# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [eeg, addiction, replication]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project aims to investigate correlates of alcohol and behavioural addiction through a partial replication of the analysis of EEG data from the EEG Psychiatric Disorders Dataset. Features analysed include PSD and FC per EEG band. Analysis aimed to find best features correlated with respective addictions, and stable region-wise predictors surviving at least 7 of 10 folds of cross-validation. The same analysis was then performed on the 'LEMON' dataset"

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.

---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Behavioural addiction is defined as “Disorders due to addictive behaviours are recognizable and clinically significant syndromes associated with distress or interference with personal functions that develop as a result of repetitive rewarding behaviours other than the use of dependence-producing substances.” (ICD-11). Due to being a result of the internal reward system rather than a psychoactive substance as in substance addiction, it is hard to perform a quantitative investigation on this condition. I felt that neuroimaging would help in this regard, as it will allow for analysis of brain activity to find similarities (if any) between behavioural addictions and substance addictions which will allow for better understanding of these disorders.

### Tools

The "project template" project will rely on the following technologies:
 * Jupyter Notebook for main analysis
 * MNE and scipy packages to process and convert the LEMON dataset for analysis
 * sklearn for analysis of both datasets

### Data

Psychiatric Disorders Dataset (BRMH): https://www.kaggle.com/datasets/shashwatwork/eeg-psychiatric-disorders-dataset
MPI-Leipzig_Mind-Brain-Body (LEMON) Dataset: https://fcon_1000.projects.nitrc.org/indi/retro/MPI_LEMON.html

10 random samples were selected during analysis for the Psychiatric Disorders Dataset

AWS CLI was used to download the psychiatric disorders dataset
EEG data from the LEMON dataset had to be manually downloaded and editted so that the .vhdr file data pointed to the correct corresponding .eeg and .vmrk data files

8 healthy control subjects and 8 alcohol addicted subjects were selected from the LEMON Dataset. The following column was added into the csv file after conversion, which also shows which subjects are control/addicted

subject_ID	specific.disorder
sub-032439	Alcohol use disorder
sub-032489	Alcohol use disorder
sub-032356	Alcohol use disorder
sub-032460	Alcohol use disorder
sub-032313	Healthy control
sub-032485	Healthy control
sub-032369	Alcohol use disorder
sub-032421	Healthy control
sub-032480	Healthy control
sub-032446	Healthy control
sub-032377	Alcohol use disorder
sub-032392	Healthy control
sub-032334	Healthy control
sub-032410	Alcohol use disorder
sub-032358	Healthy control
sub-032499	Alcohol use disorder


### Deliverables
 * Jupyter Notebook for main analysis (Analysis.ipynb)
 * Python script to process and analyse raw EEG data (Raw_to_CSV.py)
 * results saved in .csv files


## Results

### Progress overview
* Code to analyse best features and stable region-wise predictors from the Psychiatric Disorders Dataset
* Conversion of LEMON dataset to same format as Psychiatric Disorders Dataset, followed by analysis of best features for alcohol addiction from this dataset

### Tools I learned during this project
 * MNE Python to clean raw EEG data
 * sklearn to perform Logistic regression with Elastic Net on EEG features (PSD and FC)


### Results

#### Deliverable 1: "Best Features" from the Psychiatric Disorders Dataset
Best feature predictor of Alcohol use disorder was High Beta band Functional Connectivity (AUC = 74.44, SD = 18.63). This differed slightly from the original study where best feature was Whole band Power Spectral Density
Best feature predictor of Behavioural addiction disorder was Delta band Power Spectral Density (AUC = 74.44, SD = 18.63). This was consistent with the original study where best feature was also Delta band Power Spectral Density

Differences in analysis was attributed to lower sample size in this case

#### Deliverable 2: Stable predictors from Psychiatric Disorders Dataset
Entirely different results from original study, as the analysis showed functional connectivity as stable predictors across all bands whereas these were not stable predictors in the original.

Concluded that analysis was likely flawed, thus this part was omitted from the analysis of the LEMON dataset. Continuing to investigate reasons for this error

#### Deliverable 3: "Best Features" from the 'LEMON' Dataset
Best feature predictor of Alcohol use disorder was Beta band Functional Connectivity (AUC = 68.33, SD = 26.30).

Due to some psychological pre-test results being unavailable, and lack of expertise in evaluating psychiatric conditions, behavioural addiction data was not analysed as subjects with this condition could not be identified


## Conclusion and Future Directions
Analsysis was severely limited by my lack of expertise on the topic, both in terms of quantifying behavioural addiction and in using the python as an analysis tool. Additionally, replicating a pre-processed dataset (Psychiatric Disorders) limited the analysis as it was hard to match the format of the 'LEMON' dataset for comparison. I intend to revisit the analysis of stable region-wise predictors in the future as well as attempt the analysis from scratch using raw data if possible to gain a better understanding of the overall process.