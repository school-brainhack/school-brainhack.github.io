---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-09" # Date you first upload your project.
# Title of your project (we like creative title)
title: "The Neural mechanism of Nature-based intervention with Environmental information of Forest"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Chun-Yi, Lee]

# Your project GitHub repository URL
github_repo: https://github.com/JamesLeeCY/ChunYi_Lee_project.git

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [nature-based intervention, environmental preference, fMRI, naturalistic paradigm]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Researchers will use fMRI to study how short-term exposure to nature affects the brain. They hypothesize that nature exposure will improve cognitive function and reduce noisy information processing in the VMPFC."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<a href="https://drive.google.com/file/d/1mf_Asopjr3b24oeCJW2zO_3eHvJha_GH/view?usp=sharing">
<img src="https://drive.google.com/uc?export=view&id=1mf_Asopjr3b24oeCJW2zO_3eHvJha_GH" 
width="1000px;" alt=""/>
<br /><sub><b>Project overview</b></sub>
</a>

## Project definition

### Background

Increasingly, research has shown that Nature-Based Interventions (NBIs) have positive effects on cognitive function and mental health. One study showed that participants who walked through an arboretum performed significantly better on memory and directed attention tasks, and increased positive affect more than did an urban-walking group. However, the different environmental preferences of individuals might moderate or confound the cognitive benefits of NBIs. It also remains unclear what specific mechanisms might link the neural processing of environmental information with cognitive benefits.

### Tools

The "The Neural mechanism of Nature-based intervention with Environmental information of Forest" project will rely on the following technologies:

 * HeuDiConv for BIDS
 * fMRIPrep for preprocessing
 * Pliers package for automated feature extraction

### Data

Self-recruiting project
Location: Taiwan Mind & Brain Imaging Center at National Chengchi University
Participants: N = 60 (30 pro-nature, 30 pro-urban)
Stimulus: 10 min video with 5 scenes for both natural and urban environment


### Deliverables

At the end of this project, we will have:
 - Analyze workflow for BIDS conversion and fMRIPrep
 - Code script for Naturalistic paradigm analysis

## Results

### Progress overview

The project was swiftly initiated by Chun-Yi Lee, about the naturalistic paradigm and nature-based intervention.

### Tools I learned during this project

 * HeuDiConv for BIDS
 * fMRIPrep for preprocessing
 * Pliers package for automated feature extraction

### Results

#### Deliverable: results

 * Convert the raw dicom files into BIDS format by HeuDiConv tools
 * Create a container in server to isolate the process and manage packages
 * Preprocessed the nifti files with fMRIPrep as a Robust Preprocessing Pipeline for fMRI Data
 * Try to automated extract the features from environment stimuli with pliers package
 * Try to analyze the whole brain Intersubject Correlation and Functional Alignment between different participants with certain environmental preference


## Conclusion and acknowledgement

 would like to thank the Brain Hack School 2023 for organizing this course and for their support. The course has been highly beneficial, and I would like to express my appreciation to organizer and TA for all your support!
 
 ## References
 
Kuperman, V., Stadthagen-Gonzalez, H. & Brysbaert, M. Age-of-acquisition ratings for 30,000 English words. Behav Res 44, 978–990 (2012). https://doi.org/10.3758/s13428-012-0210-4
Warriner, A.B., Kuperman, V. & Brysbaert, M. Norms of valence, arousal, and dominance for 13,915 English lemmas. Behav Res 45, 1191–1207 (2013). https://doi.org/10.3758/s13428-012-0314-x
Glerean, E., Salmi, J., Lahnakoski, J. M., Jääskeläinen, I. P., and Sams, M. (2012). Functional Magnetic Resonance Imaging Phase Synchronization as a Measure of Dynamic Functional Connectivity. Brain Connect. 2, 91–101. doi:10.1089/brain.2011.0068.
Nastase, S. A., Gazzola, V., Hasson, U., & Keysers, C. (2019). Measuring shared responses across subjects using intersubject correlation. Social Cognitive and Affective Neuroscience, Volume 14, Issue 6, June 2019, Pages 667–685, https://doi.org/10.1093/scan/nsz037
Nummenmaa, L., Lahnakoski, J. M., and Glerean, E. (2018). Sharing the social world via intersubject neural synchronisation. Curr. Opin. Psychol. 24. doi:10.1016/j.copsyc.2018.02.021.
Simony, E., Honey, C. J., Chen, J., Lositsky, O., Yeshurun, Y., Wiesel, A., et al. (2016). Dynamic reconfiguration of the default mode network during narrative comprehension. Nat. Commun. 7. doi:10.1038/ncomms12141.

 
 