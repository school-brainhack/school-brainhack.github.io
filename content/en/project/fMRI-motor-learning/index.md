---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-09" # Date you first upload your project.
# Title of your project (we like creative title) <!-- changed here -->
title: Identifying Stages of Motor Learning using fMRI connectivity

# List the names of the collaborators within the [ ]. If alone, simple put your name within [] <!-- changed here -->
names: [Diego Duran ]

# Your project GitHub repository URL <!-- this is changed too -->
github_repo: https://github.com/brainhack-school2023/duran_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty. <!-- changed here too -->
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`. <!-- changed here as well -->
# Please only lowercase letters
tags: [project, github, markdown, brainhack, jupyter notebook, preprocessing, ADHD, fMRI]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects.. <!-- this is changed as well -->

summary: "The focus of this project was to quanitfy stages motor learning in participants learning a sequence of tasks. Participants under went learning over a 5 week period, and received fMRI images after every week. This project aimed to create fMRI connectivity images for each of the weeks and constrast them to identify changes in brain stimulation. These contrasts would then be compared to particiapnts performance metrics to quantify learning by pairing the changes in the brain with changes in performance . Project reports are incorporated on the BHS [website](https://school.brainhackmtl.org/project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bhs2020.png" 
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

#### About me

Hello my name is Diego, I am a graduate student at Toronto Metropolitan Univeristy studying Biomedical Engineering. I have a background in kinesiology and health information management. I am interested in the connection of mind and body and how we can use technology to improve this connection within the context of performance and rehabilitation.

#### About the project

Motor learning can be understood as a set of processes aimed at learning and refining new skills by practicing (Nieuwboer et al, 2009) This process results in changes within the nervous system that translates to improvements in movement accuracy and smoothness. Neuroscientists have created models to depict motor learning such as Fitts and Posner's 3 stages, however there is no consensus about the speciifc changes that occur in the brain. Although these changes are difficult to quantify, performance with a task can serve an indirect measure that can outline clear stages of learning.

<img src="cover_brain_tingz.png" width="80%">

### Personal Goals <!-- Done -->
 * Understand the processing and application of the full neuroimaging workflow, specifically from raw fMRI data to data visualization
 * Build and develop skills in open science applications, particularly for future neuroimaging projects
 * Gaining insight into fMRI data applications, specifically in creating connectivity matrices and brain parcellations

### Tools <!-- Done -->

This project will rely on the following technologies:
<!-- testing thing here -->
<OL>
<LI>Open Neuro fMRI data - doi: 10.18112/openneuro.ds002776.v1.2.0
<LI>Python Scripts
<UL>
<LI>Nilearn - extractring and visualizing data
<LI>Pandas - manipulation and plotting 
<LI>Nibabel - loading images
</UL>
<LI>SciNet - Jupyter Notebook - to implement code for our data/ take first steps within the Teach (University of Toronto) cluster
<LI>Git and GitHub - practice sharing a workspace, fork repositories, version control 
<LI>Bash - Use Terminal for quick and easy access 
</OL>

### Data

For this project, we were working with a Neuroimaging Dataset on Motor sequence learning from Openneuro (Berlot et al. 2020) 

The experiment consisted of 4 imaging sessions, across 5 weeks of training. Participants (N=26) underwent session 1 (ses-01) prior to training onset, session 2 (ses-02) after a week of training and sessions 3-4 (ses-03, ses-04) after 5 weeks. Performance across sesssions 1-3 was paced using a metronome, and in session 4 the performance was at full speed.

Participants executed inside the scanner 6 trained and 6 untrained sequences. Sequence identity (1-12) and sequence type (trained / untrained) for each trial can be found in the accompanying events.tsv files. Additionally, each sequence was performed twice in a row (repetition 1-2 in events.tsv). Berlot et al. 2020

 
### Deliverables
&check; Preprocessed Data<br>
&#10003; Creating Brain Parcellation<br>
&#10003; Visualizations<br>
&#10003; Graphs for Statistical Analysis<br>
&check; Connecitivty Matrix<br>


## Results
 
### Progress overview

This project was initiated by Diego Duran, based off of the OpenNeuro Dataset from Eva Berlot et al.(2020) on June 9th 2023. The final presentation of this project was delivered on 2nd June 2023. All deliverables were given an attempt to be completed, where the ones that were, can be found on this repository. 

### Tools we learned to use during this project

 * **Pre-processing Data Scripts:** We learned how to pre-process data for the first time, which is running code through SciNet clusteres and being able to access the fMRI data. It felt really weird, but somehow quite fun as well.
 * **Jupyter Notebook/Jupyter Lab:** We used this platform to code our results based on the preprocessed data. That was quite the challenge because we were hit with all these new libraries that we did not know could produce _so_ many different visualizations.
 * **Git:** Through the modules, and accessing functions used for preprocessing/analysis - Git was a integral part of what we had to learn.
 * **Bash/Terminal:** To be able to locate our data once it was/after preprocessing, we had to be able to use the classic "cd" and "ls" commands to find where all our outputs from the preprocesed data was hidden.

### Results

#### Deliverable 1: A Github repository with code scripts and data preparation

The data we obtained from Lytle et al. (2020) via OpenNeuro was already validated based on the Brain Imaging Data Structure (BIDS) standards. Thus, we were able to proceed directly to preprocessing data by forking the schizophrenia Canadian Neuroimaging Database (SCanD) project codebase developed by Erin Dickie and TIGR Lab. An overview of the general folder structure for the repository (after all scripts are run) is shown below.
 
<img src="bids_folder_structure.png" alt="Tree diagram showing SCanD_project folder structure" width="600" height="450">

An example of output from the SCanD project preprocessing pipeline fMRI prep anatomical step is shown below for subject 3, a child without ADHD. Specifically, the image below shows the template T1-weighted image with contours delineating the detected brain mask (red outline) and brain tissue (blue outline) segmentations. These outputs were reviewed for quality assurance purposes.

<img src="fmriprep_anat_sub-03.png" alt="Brain mask and tissue segmentation for subject 3, child without ADHD" width="400" height="450">

Our project GitHub repository can be accessed here: https://github.com/brainhack-school2023/csun_project/ 

Our preprocessing scripts adapted from Erin Dickie’s SCanD_project: https://github.com/sunclara/SCanD_project-brainhack2023 

#### Deliverable 2: A jupyter notebook of the analysis codes and visualizations
 
Based on resources contained within Erin Dickie’s Krembil Centre for Neuroinformatics (KCNI) summer school slides and modules, we were able to produce graphs as well as brain images via the preprocessed data. For example, using nilearn, nibabel, and matplotlib, we were able to plot slices of the brain as well as a line graph which displayed fMRI signal vs time of any brain parcellation. In the context of our data, we chose to plot the somatomotor region vs the auditory region. 
 
The code for parcellation graph comparing fMRI signal vs. time with the somatomotor and auditory regions:

  <figure>
  <img src="code.png" alt="Code used to generate BOLD graph and connectivity matrix" width="700" height="450">
  </figure>                                                                                                 

BOLD fMRI signal over time for somatosensory and auditory regions:
  <figure>
   <img src="bold_graph.png" alt="Graph showing BOLD fMRI signal over time for somatosensory and auditory regions" width="600" height="200">
  </figure>                                                                                                     

#### Deliverable 3: A connectivity matrix based on one task
 
Once again, following Erin Dickie’s KCNI modules, we were able to create and compare connectivity matrices based on children with and without ADHD. The analysis code can be found within this repository under “brainhacks_connectivity matrix.ipynb”. Using a list, we were able to sum up the values of each participant with ADHD, average out these values (using numpy), and then plot the models using previous code in order to see a connectivity matrix. 

 Participant (subject 3) without ADHD:
 <!-- Adding the first kinda bougie connectivity matrix --> 
   <figure>
   <img src="connectivity_matrix.png" alt="fMRI connectivity matrix for subject 3, a neurotypically developing child" width="550" height="400">
  </figure>   

 
 Participants with ADHD:
 <!-- Add the sucky connectivity matrix --> 
  <figure>
   <img src="connectivity_matrix_ADHD.png" alt="fMRI connectivity matrix for children with ADHD" width="550" height="400">
  </figure>   
 
## Conclusion 

The personal objectives within this project were met as well as some deliverable goals. We all started Brainhacks with no previous knowledge on neuroimaging and the tools used with neuro-analysis on fMRI data. Moreover, most of us had limited skills with code. During our time in Brainhacks school, we were exposed to many different skills and techniques that we did not know existed. We learned lots from the modules such as the introduction to python and fMRI modules that set the foundation for our knowledge. We then applied these skills with the homework which prepared us for our project. We would like to take these skills that we learned over the course of a month in future personal projects over the summer, and develop them further. 


## Acknowledgements
We would like to thank Erin Dickie for leading and organizing Brainhacks school for the Toronto Hub and giving us the wonderful opportunity to be able to join. We would also like to thank our TAs who would join our online discord calls, and were always available to help whenever we needed it:
* Ju-Chi Yu
* Ryan Yeung

A special mention to the 12th floor and Major League Hacking for providing us with merch and pizza on our last day!

## References
Berlot E, Popp NJ, Diedrichsen J. A critical re-evaluation of fMRI signatures of motor sequence learning. Elife. 2020 May 13;9:e55241. doi: 10.7554/eLife.55241. PMID: 32401193; PMCID: PMC7266617.
  
Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC. A multi-modal parcellation of human cerebral cortex. Nature. 2016 Aug 11;536(7615):171-178. doi: 10.1038/nature18933. Epub 2016 Jul 20. PMID: 27437579; PMCID: PMC4990127.


