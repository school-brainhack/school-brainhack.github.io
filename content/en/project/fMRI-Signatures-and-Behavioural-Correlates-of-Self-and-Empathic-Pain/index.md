---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-09" # Date you first upload your project.
# Title of your project (we like creative title)
title: "fMRI Signatures and Behavioural Correlates of Self and Empathic Pain"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Lyanne Zhang, Onjoli Krywiak, Leen Ghanayem, Clarize Donato, Kayla Teopiz, Quin Xie]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2025/Empathic_Pain

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [project, github, markdown, brainhack]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Each project repository should have a markdown file explaining the background and objectives of the project, as well as a summary of the results, and links to the different deliverables of the project. Project reports are incorporated in the BHS [website](https://school.brainhackmtl.org/project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bhs2020.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Empathy is conceptualized as an individual’s ability to perceive, understand and respond appropriately to someone else’s experience.<sup>1,2</sup> In addition, empathic pain is commonly defined as an individual’s perception and emotional response to another person’s suffering or painful situation.<sup>1</sup> The cognitive component of empathy and empathic pain includes perspective taking and maintaining distinction between the self and others.<sup>3</sup> Taken together, it is proposed that disparate neural mechanisms subserve the cognitive processes that comprise empathy and empathic pain.<sup>3,4</sup>

Meta-analytic neuroimaging data suggest that multiple brain regions are implicated in empathic pain, including but not limited to the insula cortex (IC), anterior cingulate cortex (ACC), mid-cingulate cortex (MCC), and nucleus accumbens (NAc).<sup>3,5</sup> It is postulated that the IC and ACC are critical regions of interest (ROI) in the processing of emotional states and motivation.<sup>6</sup> In addition, it has been observed that functional connectivity between the MCC and IC is increased during pain perception in others.<sup>7</sup> Furthermore, the NAc has been implicated in the prediction of empathic-pain related behaviours (e.g., actions to help an individual in pain).<sup>8</sup> However, the underlying neural circuitry and networks that subserve empathic pain remain insufficiently characterized. Moreover, it is not known how sociodemographic, clinical and/or behavioural factors (e.g., loneliness or social connectedness) may mediate or moderate neural mechanisms that subserve empathic pain. 

Herein, this project aimed to apply analytical methods using Python to investigate neural activation and functional connectivity in the IC, ACC and related brain regions in adults completing an fMRI and empathic pain task paradigm.

### Main Objectives 

- Produce a neuroimaging workflow from region-specific activation analyses of pre-processed data, functional connectivity analyses, and data visualization
- Produce a GitHub Repository to enable reproducibility of our analyses.


### Tools

- Software 
  - Python packages: Nilearn Library
  - MS Visual Studio Code
  - R and RStudio
- Code and Project Management
  - Git and GitHub
  - Scripts
  - Jupyter Notebook
- Computing Environment
  - Local Laptops

### Data

This project investigated an Open Source dataset obtained from OpenNeuro [https://openneuro.org/datasets/ds006243/versions/1.0.3]. The dataset consists of fMRI data collected from 54 participants trained in one of two meditation modalities: Loving Kindness Meditation (LKM) (n = 25) and Progressive Muscle Relaxation (PMR) (n = 29). The empathic pain task paradigm consisted of two counterbalanced runs, Experience (Self) and Observe (Other) conductions, each containing 30 trials of 24 seconds in duration, with a total of 720 seconds for a single run. Each run (i.e., 30 trials) included 15 trials involving anticipation of fear and 15 trials involving pain experience). An audio cue was used to indicate whether the participant or study partner would receive a pressure pain stimulus. The pressure pain stimulus is transmitted through a tube to a piston secured on the participants’ thumbnail. 

All participants completed an empathic pain task during an fMRI scan in order to examine neural responses to self-pain test condition (i.e., pain stimulus of the participant’s hand) and empathic pain (i.e., observing someone else receive the pain stimulus). MRI data was collected at the Center for Functional and Molecular Imaging at Georgetown University using a 3T Siemens TIM Trio scanner. High-resolution structural images were acquired using a T1-weighted MP-RAGE sequence (1 mm isotropic voxels), and functional images were collected using a T2*-weighted EPI sequence (3 mm isotropic voxels, TR = 2,500 ms, TE = 30 ms).

### Deliverables

- GitHub Repository
- Dataset
- R Markdown Files
- Analysis workflow and pipeline

## Methods

### Task Activation Analysis
To examine brain regions activated during the empathic pain task, fMRI data was fitted to a first-level general linear model using Nilearn’s FirstLevelModel to compute z-maps for each task contrast. A statistical threshold (z > 3.1) was applied, and significant clusters were identified and labeled using Nilearn’s get_cluster_table and the Harvard-Oxford atlas, respectively. Further, a Multivariate Analysis of Variance (MANOVA) was used to examine whether baseline loneliness and social connectedness scores predicted activation of brain regions implicated in empathic and self-experienced pain, specifically the anterior cingulate cortex (ACC), insular cortex and superior temporal gyrus, following the meditation intervention. The UCLA Loneliness Scale (Russel et al., 1978) and Social Connectedness Scale (Lee et al., 2001) were used to measure loneliness and social connectedness at baseline. 

### Functional Connectivity Analysis
We aimed to compare functional connectivity between self-experienced and empathic pain conditions. First, we applied the masker to all files using the Harvard-Oxford brain atlas, which provides good parcellation of subcortical regions. Next, we generated one connectivity matrix (based on Pearson’s correlation) per condition for each subject. We then computed a network-blocked mean connectivity matrix for each condition for visualization purposes.
To compare connectivity between the two conditions at the edge level, we performed paired t-tests with FDR correction.

We were also interested in investigating whether functional connectivity is associated with loneliness or social connectedness. To investigate this possible association, we used our participants’ previously obtained individual functional connectivity matrices, where each participant had two matrices: one for run 1 (self) and run 2 (other/empathic pain). Then, we categorized participants’ functional connectivity matrices by run type (i.e., 1 vs 2). As well, we were interested in only functional connectivity/roi-to-roi pairs that had either the insula/insular cortex or the cingulate cortex/gyrus as one of the rois in a pair. 

Finally, to test potential associations between functional connectivity with loneliness or social connectedness, statistical analyses were performed via linear regression models. Functional connectivity of specific roi pairs (i.e., those containing insula or cingulate cortex), and covariates including age, sex, and condition were included as predictors, while our dependent/predicted variables included loneliness or social connectedness. 

## Results

### Task Activation

#### Finding 1: Many regions are activated during self pain and empathic pain tasks
![image](https://github.com/user-attachments/assets/b90db574-23c6-410e-895d-83740d766efb)
Various cortical and subcortical regions were activated during the self-pain and empathic-pain tasks, including brain regions in the frontal, parietal, temporal and occipital lobes. The empathic-pain condition was characterized by decreased activation of the frontal medial cortex and increased activation of the posterior division of the inferior temporal gyrus, middle temporal gyrus, superior temporal gyrus and temporal fusiform gyrus. On the other hand, the self-pain condition was characterized by decreased activation of the cuneal cortex, middle frontal gyrus, middle temporal gyrus, and increased activation of the supracalcarine cortex. 

#### Finding 2: Interaction between baseline loneliness and condition predicts activation in the ACC during self pain but not empathic pain task

Upon examining whether baseline loneliness and social connectedness predicted brain activation during the empathic and self-pain tasks, a MANOVA revealed a significant interaction between baseline loneliness and activation of the ACC in the self-pain condition (p = .03). Specifically, participants in the LKM meditation group showed a significant decrease in ACC activation at higher baseline loneliness scores.

### Functional Connectivity 

# Finding #1

# Finding #2: Functional connections are associated with social connectedness but not loneliness 

Several functional connectivity pairs containing our rois of interest (cingulate cortex and/or insula) were negatively associated with social connectedness in both self and empathic pain tasks. Notably, these significant associations do not pass FDR correction. In contrast, our functional connectivity pairs of interest were not significantly associated with loneliness. It appears that our rois of interest, these being the cingulate cortex and/or insula, that are typically implicated in empathic pain tasks, are also functionally connected with other regions of interest and are associated with social connectedness. This highlights that functional connectivity with our rois of interest that underlie empathic pain also appears to underlie behaviour such as social connectedness. 



### Results


##### Other projects
Here are other good examples of repositories:
- [Learning to manipulate biosignals with python](https://github.com/mtl-brainhack-school-2019/franclespinas-biosignals) by François Lespinasse
- [Run multivariate anaylysis to relate behavioral and electropyhysiological data](https://github.com/mtl-brainhack-school-2019/PLS_PV_Behaviour)
- [PET pipeline automation and structural MRI exploration](https://github.com/mtl-brainhack-school-2019/rwickens-sMRI-PET) by Rebekah Wickens
- [Working with PSG [EEG] data from Parkinson's patients](https://github.com/mtl-brainhack-school-2019/Soraya-sleep-data-in-PD-patients) by Cryomatrix
- [Exploring Brain Functional Activation in Adolescents Who Attempted Suicide](https://github.com/mtl-brainhack-school-2019/Anthony-Gifuni-repo) by Anthony Gifuni

## Conclusion and acknowledgement


