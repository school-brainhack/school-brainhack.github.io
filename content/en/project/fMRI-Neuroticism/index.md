---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-06-10" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Predicting Neuroticism and Personality Traits from fMRI Data"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Annabelle Harvey, Liz Izakson]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fmri, machine learning, personality]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Are neuropsychiatric disorders extreme cases of connectivity patterns that are found in the overall population? Using personality traits as a measure of individual variation and knowing that neuroticism is especially linked with mental disorders we wanted to see if neuroticism in a healthy population was linked with specific patterns of connectivity that could be compared to those common to neuropsychiatric disorders."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "Connectome_quanta_mag.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->
# Predicting Neuroticism and Personality Traits from fMRI Data

![JR Bee illustration](Connectome_quanta_mag.png)
JR Bee Illustration
# Project Definition - Week 1
### Background
#### Annabelle
I am a currently doing my master's in computer science at UdeM in the bioinformatics stream. I haven't locked down my thesis project yet but it will involve the impact of rare genetic variants on functional connectivity. I did my undergrad in math and have a pretty good basis in coding in python and machine learning, but I am totally new to neuroscience and very excited about brainhack school.

#### Project
I worked on this project with Liz Izakson. We're interested in variation in human brains and am curious about neuropsychiatric disorders as extremes of characterestics that are found in the overall population. To explore this idea, we want to look at the human connectome project dataset of 1200 healthy young adults that includes resting state fMRI and personality/behaviour data. Specifically, we want to try and predict neuroticism, one of the big five personality traits that is associated with [psychosis](https://www.frontiersin.org/articles/10.3389/fpsyt.2018.00648/full) and [mental disorders](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4382368/), from fMRI to see if:
1. If there are significant/consistent connnectivity patterns for neuroticism in fMRI data.
2. If so, how do they compare to findings about schizophrenia/anxiety/depression/ADHD in the literature.

### Tools
We plan on using the following tools:
 * compute canada servers with globus and aws s3 for file access and transfer
 * nilearn
 * similarity network fusion
 * sklearn
 * Data visualization
 
## Learning Goals
I especially want to use brainhack school to learn to work with fMRI data, explore different parcellation methods and ways to produce features from connectivity matrices. I also want to learn to use compute canada servers, and to improve and explore my coding skills and to learn tools for open science and reproducibility.

### Data
We will use the HCP 1200 healthy young adult dataset.

### Deliverables
I would like to produce jupyter notebooks with examples of the analysis code, an interactive data visualization, and a script for running jobs on compute canada servers.

# Results - Week 4

### Progress overview

We started out working with preprocessed data from the HCP,and explored different ways of using parcellations and connectivity measured to produce connectivity matrices. A lot of time went into learning how to download and use data in this format, but the data is very large and was very challenging to work with. Through reading papers (particularly [Dadi et al. 2019](https://www.sciencedirect.com/science/article/pii/S1053811919301594), and [Cai et al. 2020](https://academic.oup.com/scan/article/15/3/359/5815970)) we eventually discovered that HCP data is much larger than average per subject (about an hour of scan each) and that they have published an even further processed data set of parcellations, time series, and connectivity matrices (PTN release). We decided to switch to this data set which allowed us to work with 810 subjects, which would have been impossible otherwise.

With the PTN data we focused on predicting Neuroticism from the processed connectivity matrices. Using a feature selection strategy from [connectome-based predictive modeling](https://pubmed.ncbi.nlm.nih.gov/28182017/)  (CPM) that is simply choosing the edges in the connectivity matrices most correlated with the score being predicted, I tried CPM, SVR, and linear regression with leave one out cross validation. I found that prediction was very weak and that we were very far from being able to point to any specific regions or networks that are meaningful for any specific trait. Liz tried to improve on the prediction by using neural nets and tweaking parameters.

To try different models, I rewrote jupyter notebooks that I used to write and test code as python scripts that could be used more efficiently and that I could run on compute canada. I also produced documentation and data visualization to go along with the notebooks and scripts. Liz contributed exploratory data analysis and several models to the ptn_pipeline.ipynb notebook. In the end we found that neuroticism and personality traits are very hard to predict from fMRI data and that one month is not very long to explore and compare the many many different options for processing fMRI data that might have better prediction results. The slides for our final presentation can be found [here](https://docs.google.com/presentation/d/1qsFBFawu3MmrGuhGlogRqCZJWTqOs_ZLAXk5uCATcJQ/edit?usp=sharing).

### Tools I learned during this project

 * Nilearn
 * Compute canada
    * Slurm
    * ssh/scp
    * venv
 * Git/github
 * Jupyter lab
 * Scipy
 * Bash
 * t-SNE
 * Monitoring memory/CPU usage and strategies for working with fMRI data on a very weak laptop
    
 
### Results
Here is a summary of predictions of neuroticism using the three models and their respective mean squared error (MSE) values:
![Neuroticism predictions](Neuroticism_summary.png)

Here is an image of the networks that are correlated with neuroticism (note that the predictions are poor and the parcellation done by using group ICA and 200 nodes has no labels so these are more fun visualizations than anything meaningful):
![Positive network](positive_connections.png)
![Negative network](negative_connections.png)

#### Deliverable 1: Jupyter notebooks

 * [ptn_pipeline.ipynb](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/ptn_pipeline.ipynb) - explores the models and code in ptn_script.py.
 * [data_viz.ipynb](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/data_viz.ipynb) - uses the outputs from the python scripts to create figures with seaborn and nilearn plotting, the interactive nilearn plots are saved as .html files in the figures folder of this repo.

#### Deliverable 2: Python scripts

* [ptn_script.py](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/ptn_script.py) - code to run the models and save the output files.
* [clean_data.py](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/clean_data.py) - code to remove the subjects with no behavioural data from HCP PTN recon2 download (see documentation/how_to.md)

#### Deliverable 3: Bash script

* [run_script_locally.sh](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/run_script_locally.sh) - executable to run script for all model comparisons we did on a local machine.

#### Deliverable 4: Data visualization

* [figures/positive_connections.html](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/figures/positive_connections.html) - interactive version nilearn plot of connections positively correlated with neuroticism.
* [figures/negative_connections.html](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/figures/negative_connections.html) - the same for connections negatively correlated with neuroticism.
* [figures](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/tree/master/figures) - other contents are scatter plots of real vs. predicted values for each trait (N, E, O, A, C) and each model (LR, SVR, CPM) as well as summaries of all three models for each trait.

#### Deliverable 5: Documentation
 
* [how_to.md](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/documentation/how_to.md) that describes:
    * downloading the data from HCP
    * running the code
* List of packages used - [requirements.txt](https://github.com/brainhack-school2020/harveyaa_fMRI_neuroticism/blob/master/requirements.txt) 
 
## Thank you!!
Special thanks to Pierre Bellec, Desiree Lussier, Peer Herholz, Liz Izakson and everyone I got to chat with through clinics and groups! Brainhack school has been an amazing introduction to neuroimaging, I'm very grateful for everyone's time, help, resources and encouragement!


### References
Cai et al. 2020 Robust Prediction of Individual Personality From Brain Functional Connectome 
https://academic.oup.com/scan/article/15/3/359/5815970

Dadi et al. 2019 Benchmarking functional connectome-based predictive models for resting-state fMRI https://www.sciencedirect.com/science/article/pii/S1053811919301594

Moreau et al. 2020 The general impact of haploinsufficiency on brain connectivity underlies the pleiotropic effect of neuropsychiatric CNVs https://www.medrxiv.org/content/10.1101/2020.03.18.20038505v1

Ormel et al. 2015 Neuroticism and Common Mental Disorders: Meaning and Utility of a Complex Relationship https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4382368/

Shi et al. 2018 The Relationship Between Big Five Personality Traits and Psychotic Experience in a Large Non-clinical Youth Sample: The Mediating Role of Emotion Regulation https://www.frontiersin.org/articles/10.3389/fpsyt.2018.00648/full

Shen et al. 2017 Using Connectome-Based Predictive Modeling to Predict Individual Behavior From Brain Connectivity https://pubmed.ncbi.nlm.nih.gov/28182017/
