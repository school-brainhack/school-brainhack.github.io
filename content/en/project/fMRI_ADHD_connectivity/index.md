---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-09" # Date you first upload your project.
# Title of your project (we like creative title) <!-- changed here -->
title: Analyzing variability of working memory and reward processing in children with and without ADHD using fMRI data

# List the names of the collaborators within the [ ]. If alone, simple put your name within [] <!-- changed here -->
names: [Zara Khan, Fariah Sandhu, Clara Sun]

# Your project GitHub repository URL <!-- this is changed too -->
github_repo: https://github.com/brainhack-school2023/csun_project/

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty. <!-- changed here too -->
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`. <!-- changed here as well -->
# Please only lowercase letters
tags: [project, github, markdown, brainhack, jupyter notebook, preprocessing, ADHD, fMRI]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects.. <!-- this is changed as well -->

summary: "Our project aims to help develop our skillset on analyzing fMRI data on the OpenNeuro dataset chosen. This includes using ciftify, cifti_clean, jupyter notebook, and multiutudes of libraries within python. Project reports are incorporated in the BHS [website](https://school.brainhackmtl.org/project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bhs2020.png" 
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Attention Deficit Hyperactivity Disorder (ADHD) is one of the most common neurodevelopmental disorders worldwide. Moreover, there is a high prevalence of ADHD among children (Morkem et al., 2020). The characteristics symptoms of ADHD, namely poor working memory, greater reliance on external feedback, and abnormal reward processing are of interest to us because these characteristics have been associated with changes in brain activity patterns in distinct networks. In addition, previous studies also suggest that there are substantial individual differences in reactions to reward and feedback manipulation among those with ADHD (Hammer et al., 2015). 

<!-- add in image: "blah" here and Comment here when added -->

### Personal Goals <!-- Done -->
 * Understand the processing and application of the full neuroimaging workflow, specifically from raw fMRI data to data visualization
 * Build and develop skills in open science applications, particularly for future neuroimaging projects
 * Gaining insight into fMRI data applications, specifically in creating connectivity matrices and brain parcellations

### Tools <!-- Done -->

This project will rely on the following technologies:
<!-- testing thing here -->
<OL>
<LI>Open Neuro fMRI data - doi: 10.18112/openneuro.ds002424.v1.2.0
<LI>Python Scripts
<UL>
<LI>Nilearn - extractring and visualizing data
<LI>Pandas - manipulation and plotting 
<LI>Nibabel - loading images
</UL>
<LI>SciNet - Jupyter Notebook - to implement code for our data/ take first steps within our the Niagara (University of Toronto) cluster
<LI>Git and GitHub - practice sharing a workspace, fork repositories, version control 
<LI>Bash - Use Terminal for quick and easy access 
</OL>

### Data

For this project, we were working with a Neuroimaging Dataset on Working Memory and Reward Processing in Children With and Without ADHD from OpenNeuro (Lytle et al., 2020). 

The dataset contains 79 children at session T1 (mean age = 10.4, 14 female). A subset of the participants 48 individuals returned two years later to complete a follow-up standardized testing session (n = 48, mean age = 12.6, SD = 0.94). 35 participants at session T1 and 18 participants at session T2 had a diagnosis of ADHD. All participants diagnosed with ADHD were male. Participants were recruited from the greater Chicago area.

Participants completed eight n-back working memory tasks in the scanner which varied in three factors: reward amount, feedback delay, and judgment type. In all tasks, participants were presented with a series of letters one at a time. These letters were located in one of four positions around a fixation box. 

In the verbal working memory task (V), which is what we were looking at,  participants were asked to judge whether the letter that appeared on the screen was the same letter as the one presented n letters back.

Participants made responses by selecting one of two buttons on a right-handed button box. Prior to the beginning of each block, the program would indicate which task instructions were to be followed (1-back, 2-back or fixation) with varying amounts of trials and questions. 

Tasks also varied in reward amount. Participants were told that they would make $.02 or $.25 for every correct answer for the small (S) and large (L) reward tasks, although all participants were compensated the same by the end of the tasks. Participants were reminded of what reward amount was being offered by one of two images. For small reward tasks, the image was two coins, and for the large reward tasks, the was a stack of paper bills. 

Tasks contained one of two feedback times, immediate (I) or delayed (D). In the delayed feedback tasks, participants would continue to view a black fixation square. At the end of each experimental block, participants would be told their percentage of correct responses.

In all tasks, trial timing was adhered to. Participants were presented with the letter in one of the four corners, where the letter disappeared and only the fixation square remained. Participants then continued to see a fixation period of 600 ms. In delayed feedback, the fixation square remained black.
 
Some Limitations included:
* Right-handed
* Native English speakers
* Have normal or corrected to normal vision and have no history of neurological or psychological disorder
* Prematurity of less than 36 weeks
* Head injury causing overnight hospitalization
* Hearing loss, or contraindications for MRI
* Participants could not be taking medication affecting the central nervous system other than ADHD medication, and all participants with ADHD were required to be male

**Our Chosen Task:**
Our group had chosen to focus on one task from the eight- the Verbal, Large Reward, Delayed Feedback (VLD).  Of the 73 participants who completed the VLD task, 30 participants were diagnosed with ADHD as opposed to the 43 participants who were not. Due to problems our group ran into with preprocessing data (which will be discussed later), we were only able to obtain processed data for the first 10 participants, 4 of whom could not be used as a result of not completing the VLD task. Of our six participants, five individuals were diagnosed with ADHD.
 
 <!-- Add Data Images Hhere!!! Marks as Done when done -->
 
 

### Deliverables

<h1>Languages of the web</h1>
<h3>&check; HTML</h3>
<h3>&#10003; CSS</h3>
<h3>&#10003; JavaScript</h3>
<h3>&check; PHP</h3>


## Results

### Progress overview

The project was swiftly initiated by P Bellec, based on the existing template created in 2019 by Tristan Glatard and improved by different students. It was really not that hard. Community feedback is expected to lead to rapid further improvements of this first version.

### Tools I learned during this project

 * **Meta-project** P Bellec learned how to do a meta project for the first time, which is developping a framework while using it at the same time. It felt really weird, but somehow quite fun as well.
 * **Github workflow-** The successful use of this template approach will demonstrate that it is possible to incorporate dozens of students presentation on a website collaboratively over a few weeks.
 * **Project content** Through the project reports generated using the template, it is possible to learn about what exactly the brainhack school students are working on.

### Results

#### Deliverable 1: report template

You are currently reading the report template! I will let you judge whether it is useful or not. If you think there is something that could be improved, please do not hesitate to open an issue [here](https://github.com/brainhack-school2020/project_template/issues) and let us know.

#### Deliverable 2: project gallery

There is not yet a project gallery, as BHS 2020 is the first edition that will incorporate it on the website. You can still check out the [2019 BHS github organization](https://github.com/mtl-brainhack-school-2019)

##### ECG pupilometry pipeline by Marce Kauffmann

The repository of this project can be found [here](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann). The objective was to create a processing pipeline for ECG and pupillometry data. The motivation behind this task is that Marcel's lab (MIST Lab @ Polytechnique Montreal) was conducting a Human-Robot-Interaction user study. The repo features:
 * a [video introduction](http://www.youtube.com/watch/8ZVCNeX42_A) to the project.
 * a presentation [made in a jupyter notebook](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann/blob/master/BrainHackPresentation.ipynb) on the results of the project.
 * Notebooks for all analyses.
 * Detailed requirements files, making it easy for others to replicate the environment of the notebook.
 * An overview of the results in the markdown document.

##### Other projects
Here are other good examples of repositories:
- [Learning to manipulate biosignals with python](https://github.com/mtl-brainhack-school-2019/franclespinas-biosignals) by François Lespinasse
- [Run multivariate anaylysis to relate behavioral and electropyhysiological data](https://github.com/mtl-brainhack-school-2019/PLS_PV_Behaviour)
- [PET pipeline automation and structural MRI exploration](https://github.com/mtl-brainhack-school-2019/rwickens-sMRI-PET) by Rebekah Wickens
- [Working with PSG [EEG] data from Parkinson's patients](https://github.com/mtl-brainhack-school-2019/Soraya-sleep-data-in-PD-patients) by Cryomatrix
- [Exploring Brain Functional Activation in Adolescents Who Attempted Suicide](https://github.com/mtl-brainhack-school-2019/Anthony-Gifuni-repo) by Anthony Gifuni

#### Deliverable 3: Instructions

 To be made available soon.

## Conclusion and acknowledgement

The BHS team hope you will find this template helpful in documenting your project. Developping this template was a group effort, and benefitted from the feedback and ideas of all BHS students over the years.
