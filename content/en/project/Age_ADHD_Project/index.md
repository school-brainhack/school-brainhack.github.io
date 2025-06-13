---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-20" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Age-Dependent EEG patterns for Predicting Treatment Response in ADHD"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Ingrid Campbell, Amanda/Tianyi Liu]

# Your project GitHub repository URL
github_repo: https://github.com/school-brainhack/Age_ADHD_Project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [adhd, eeg, age, brainhack]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Each project repository should have a markdown file explaining the background and objectives of the project, as well as a summary of the results, and links to the different deliverables of the project. Project reports are incorporated in the BHS [website](https://school.brainhackmtl.org/project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bhs2020.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Attention deficit hyperactivity disorder (ADHD) is one of the most common neurodevelopmental and psychiatric disorders. ADHD is characterized by significant neurophysiological differences that can be observed in electroencephalography (EEG) recordings. 
EEG is a neuroimaging technique used to extract features and patterns, such as power spectral bands, where there are five bands that represent different functional characteristics (delta, theta, alpha, beta, gamma). For example, the theta band is associated with deep sleep and the beta band is associated with awake states and concentration. The theta-beta ratio is a well-known pattern in ADHD along with the alpha peak frequency associated with focus.
A promising development in EEG research is the use of artificial intelligence (AI) and machine learning (ML) as an advanced signal processing tool. There are also age-related changes in quantitative EEG in ADHD. However, there is a lack of personalized treatment recommendations based on EEG patterns and age for individuals with ADHD


<iframe width="560" height="315" src="https://www.youtube.com/embed/PTYs_JFKsHI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Tools

The "project template" project will rely on the following technologies:
 * Markdown, to structure the text.
 * The Hugo website framework which is used by the BHS website. This makes it possible to easily add the markdown project description to the website.
 * Adding the project to the website relies on github, through pull requests.

### Data

Ultimately, the project template will be used by all BHS participants. Data on the different projects will be aggregareted on the [following page](https://school.brainhackmtl.org/project). This will serve as an additional example gallery in the years to come for future brainhack school students. Many reports from [BHS 2019](https://github.com/mtl-brainhack-school-2019) already used this template.

### Deliverables

At the end of this project, we will have:
 - The current markdown document, completed and revised.
 - A gallery of the student projects at Brainhack 2020.
 - Instructions on the website about how to submit a pull request to the [brainhack school website](https://github.com/BrainhackMTL/school) in order to add the project description to the website.

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
