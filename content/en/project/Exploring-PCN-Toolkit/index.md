---
type: "project" # DON'T TOUCH THIS ! :)
date: "2022-07-29" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Exploratory Work on the Predictive Clinical Neuroscience (PCN) Toolkit"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Andjela Dimitrijevic]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2022/dimitrijevic_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [pcn-toolkit, github, hpc, brainhack cloud]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "My project consists of exploring the predictive normative modelling (PCN) toolkit via their numerous tutorials. It contains a markdown file for future new users of this package. It also includes steps on how to format your own data to use this toolkit. Finally, some cloud computing user guides will be touched upon."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "FSL_recon.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

# Project definition

## Background

The PCN toolkit aims at providing diffferent tools of **normative modelling** for understanding *psychiatric disorders* at the individual level including: <br />
- Data selection, 
- Data preparation, 
- Algorithm & modelling, 
- Evaluation & interpretation <br />

I was interesting in how to use this tool because it overlaps with my PhD work on trying to find a neuroimaging atlas for pediatric population. Hence, I wanted to see if it would be useful with the data I have. 

## Objectives 

The aim of this project will be decomposed into three sub-objectives:
* Start off with the available tutorial on the PCN toolkit documentation to get familiar to it
* Use another set of data if possible to follow through the available steps that this toolkit offers 
* Adapt some functionalities which were found to be less intuitive to work with  <br />
* Learn some new tools throughout this work

All of these three sub-objectives will be **documented** to be able to be **reproduced** in later or other exploratory works. 

### Tools
This project relied on numerous tools throughout its creation:
- [PCN Toolkit](https://pcntoolkit.readthedocs.io/en/latest/) and their [GitHub page](https://github.com/amarquand/PCNtoolkit) to explore their tutorials
- Google Colab to follow through some of the tutorials
- Bash Terminal constantly when moving files or using Git
- High performance computing (HPC) through accessing the BrainHack cloud
- Markdown to structure the tutorial guides
- Git and GitHub for version control and making the project reproducible

<img width="100" height="100" src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png">

<img width="100" height="100" src="https://lthub.ubc.ca/files/2021/06/GitHub-Logo.png">

<img width="80" height="80" src="https://avatars.githubusercontent.com/u/8958471?v=4">


## Data

In the end, this project does not use data a lot because guides for using some neuroimaging tools are presented instead. However, FreeSurfer was used on two subjects of the publicly available longitudinal [Calgary Preschool Dataset](https://osf.io/axz5r/).


## Results: Deliverables of this project

At the end of this BrainHack school, these files will be made available:
- A [GitHub page](https://github.com/brainhack-school2022/dimitrijevic_project) containing all the modifications that were made to the PCN-toolkit tutorials
 - A [markdown file](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/PCNTutorial_steps/where_to_start.md) on where to start with the PCN-toolkit tutorials and [another](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/PCNTutorial_steps/data_formatting.md) on how to format the data adequately all in the PCNTutorial_steps directory on GitHub
 - A [markdown file](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/BrainHackCloud_steps/get_connected.md) on getting connected to the BrainHack Cloud to access HPC clusters as well as [one](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/BrainHackCloud_steps/neurodesk_access.md) on testing out the Neurodesktop container all in the BrainHackCloud_steps directory on GitHub
 


## Progress overview

At first, I thought using the Calgary Preschool Dataset would have been enough to do the analysis with the PCN-toolkit. However, this dataset seems too small (only 64 subjects) for that type of analysis. Furthermore, it was lacking cortical thickness maps which is an essential feature to be analyzed. Hence, that's why I started connecting to the HPC during the last week of the BrainHack school to be able to run FreeSurfer recon-all function on all subjects. This too came with its specific challenges. First, getting connected to the BrainHack cloud from my own computer did not work directly. Second, it took quite long to run the wanted FreeSurfer command on the NeuroDesk test server on one subject. Also, FreeSurfer bases its cortical thickness maps on previous registration tasks using adult templates (by default the Talairach atlas). This can incorporate biases and render the results to be faulty as shown on the two figures below. Indeed, some regions are not well delineated whether it be for the white matter and gray matter segmentation on Fig. 1 or the wrong specific parcellations shown by the green rectangle on the second figure.

<div>
    <p style="text-align:center;"><img src="https://github.com/Andjelaaaa/school/blob/master/content/en/project/Exploring-PCN-Toolkit/SegExample.png?raw=1"  width="1000" class="caption">Fig. 1 Example of white matter segmentation on a subject</p>
    </div> 


<div>
    <p style="text-align:center;"><img src="https://github.com/Andjelaaaa/school/blob/master/content/en/project/Exploring-PCN-Toolkit/CorticalParcellationExample.png?raw=1"  width="1000"  class="caption">Fig. 2 Parcellations of the right and left hemisphere pial surface for cortical analyses </p>
    </div>  


The final presentation on this project is avaible via [this link](https://docs.google.com/presentation/d/1BBGOiibHYFYnNmN_DVhKsS1oMsixU5fQ7aqgNR5F5jc/edit?usp=sharing) for further details.


## Detailed actions

*Reported GitHub issue to alert the PCN-toolkit tutorial writers*

The BLR_protocol tutorial is more easily ran locally and does not work because of the older python version available on Google Colab. The solution of running it locally has all been explained in the [where_to_start md file](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/PCNTutorial_steps/where_to_start.md). To consult the reported issue click [here](https://github.com/predictive-clinical-neuroscience/PCNtoolkit-demo/issues/6)

*Accessed the neurodesktop via the BrainHack Cloud successfully*

The neurodesktop test server is great and easily accessible through the browser with various neuroimaging tools. Their test server is available via this [link](https://www.neurodesk.org/docs/neurodesktop/getting-started/play/) without any installation required. Also, installing and accessing this neurodesktop container through the BrainHack cloud was succesful. However, an important note is that running the NeuroDesk container via Docker should first be done on a virtual machine and NOT directly on the cloud.
 

*Obtained recon-all FreeSurfer results for one subject*

This was ran directly on the test server which is an interesting tool easily usable by everyone. The results could not be loaded as a zip file in the main GitHub repository for this project because of their size. However, this took approximately 7 hours to run because it was done on the available resources on the test server. Hence, using BrainHack cloud resources to parallelize everything is suggested.

## Future Work
Some future steps which will be done to follow through this project are presented below:

- Aggregating multiple pediatric datasets to have more subjects and also different sites to analyze with the PCN-Toolkit
- Submitting a job to the slurm scheduler to obtain cortical thickness maps of the data, but with an appropriate atlas
- Uploading this newly modified data via DataLad tools to make it more reproducible


## Conclusion and acknowledgement

To conclude, the initial objectives of this project have been slightly modified. However, I am still glab with all the new essential tools I have learned throughout the weeks during this BrainHack school. I would like to thank all the instructors, but specifically the ones from the group-analysis pod which made this experience smoother! :fireworks:
