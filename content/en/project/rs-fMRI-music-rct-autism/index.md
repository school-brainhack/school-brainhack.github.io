---
type: "project" # DON'T TOUCH THIS ! :)
date: "2022-08-07" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Workflow of resting state connectivity from a raw dataset to longitudinal visualization"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Kevin Jamey]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2022/jamey_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [resting state, workflow, music, autism]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "To aim of this project was to provide a full neuroimaging workflow from preprocessing of raw data to visualisation of results,
to explore longitudinal analysis between two treatments in this dataset and to visualise resting-state networks linked to the default mode network and attention. In my github repository you will find scripts and documentation about the the BIDS to NiFTY conversion, fMRI prep as well as resting-state visualisation of a single participant. There is also a powerpoint presentation slide to guide you through the work."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "pcc_seed_to_voxel_cor_post.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition


## _ABOUT ME_

My research interests are on new technologies for music-based cognitive training in children with neurodevelopmental disorders. I completed my MSc. on music perception abilities in children on the Autism Spectrum (AS) at the University of Montreal under the supervision of Krista L. Hyde. My doctoral thesis is supervised by Simone Dalla Bella and examines the neural correlates of a tablet-based rhythmic training game (RhythmWorkers) on executive functioning and speech in children on the AS. In my free time, I am a singer-songwriter, music producer/live act and I love to create powerful musical experiences where lyrics are inflected for rhythm and melody.

## _PROJECT SUMMARY_

### Main objectives

* Provide a full neuroimaging workflow from preprocessing of raw data to visualisation of results 
* To explore longitudinal analysis between two treatments in this dataset
* To analyse resting-state networks linked to joint attention (dorsal attentional, visual, DMN)

### Personal objectives

* To learn the full workflow of neuroimaging from converting raw data to preprocessing to data visualisation
* To set myself up with open science tools for neuroimaging work in the future
* To get familiar with the best practices of shareable open science kits and software

### Tools

* Git and Github for sharing project
* dcm2bids for converting raw data into NiFTY and a BIDS structure
* fMRIPrep for data preprocessing
* Alliance Canada for computing pre-processing
* Python Packages matplotlib, nilearn, plotly


### Data
Dataset was collected during my masters in 2016 at the MNI. I scanned
~50 participants with autism before and after either 12 weeks of music therapy or arts and crafts therapy. The data involves a weighted T1 scan and resting-state fMRI. 
A previous publication on this data set can be found [here](https://www.nature.com/articles/s41398-018-0287-3
).

### Project deliverables

* project workflow detailed in my [GitHub repository](https://github.com/brainhack-school2022/jamey_project)
* the bash code I used to run BIDS conversion and fMRIprep 
* a markdown file introducing the project, highlighting the results and a discussion with recommendations


## Results

### Progress overview

The project was workflow was set-up for a single participant over the course of the brainhack school. It will be adapted in the future in order to run multiple participants and do group seed-based resting state fMRI.

### Tools I learned during this project

 * **Project-Management** I learnt how to set-up the framework for making a shareable neuroimaging project using open science rules.
 * **Github workflow-** I learnt to use GitHub in order to share my project openly and invite people to collaborate on it.
 * **Project content** Here you will find all the key steps necessary to move from a raw imaging dataset to some cool visualisations.

### Results

#### Deliverable 1: report template

You are currently reading the report template! I will let you judge whether it is useful or not. If you think there is something that could be improved, please do not hesitate to open an issue [here](https://github.com/brainhack-school2022/jamey_project/issues) and let me know.


#### Deliverable 2: Visualisation using Nilearn

 After successfully convertion the raw data of this participant to BIDS and NiFTY, I preprocessed his data using fmriprep. You can see details about this in my [slides](https://github.com/brainhack-school2022/jamey_project/blob/main/docs/Project%20Final%20Presentation_PSY6983.pptx). I looked at a simple connectome before and after a music intervention for a child diagnosed on the austim spectrum. This is simply for illustration purposes since a large amount of participants are requited to make a meaningful connectome. Then visualized seed-based connectivity of the Posterior Cingulate Cortex before and after music therapy in this subject. You can see the visual results of my project [here](https://github.com/brainhack-school2022/jamey_project/blob/main/results/results.md). Behaviorally we found differences after the music therapy in [joint attention](https://www.researchgate.net/publication/349361961_Joint_engagement_and_movement_Active_ingredients_of_a_music-based_intervention_with_school-age_children_with_autism). In this single subject's seed-based conectivity there seems to be more connectivity in the medial prefrontal cortex, the visual cortex, and tempo-parietal network, which would be in line with improvement in joint attention. In order to further develop these findings for the experimental group, a seed-based connectivity for the entire experimental and control treatment will be conducted.  


## Conclusion and acknowledgement

I hope you find this projet useful in outlining a standard shareable workflow from imgages fresh out of the scanner to tangible visualisations of resting-state connectivity. Many thakns to the brainhack school instructors and students who helped make this prossible in such a short amount of time. I look forward to devling deeper into the foundations that are laid here during my PhD.
