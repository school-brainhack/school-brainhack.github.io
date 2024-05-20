---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-10" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Multimodal Investigation of Neural Correlates of Athletic Performance"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Arunim Guchait]

# Your project GitHub repository URL
github_repo: https://github.com/ArunimGuchait/BrainHack-School-2023-Project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI, fslvbm, dMRI Analysis in Python, athletes]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project investigates the neural correlates of athletic performance using fMRI, dMRI, and FSLVBM to compare grey matter volume and white matter connectivity between athletes and non-athletes. The study aims to identify brain regions associated with athletic performance, explore white matter connectivity differences, and examine the relationship between brain structure and specific athletic skills. The dataset included nine Indiana University football players and nine controls."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "project_image.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

The relationship between athletic performance and brain structure and function has been a topic of interest in the field of neuroscience. Understanding the neural correlates of athletic performance can provide valuable insights into the development of training programs and interventions to enhance physical and cognitive abilities. In this project, I propose to use functional magnetic resonance imaging (fMRI), diffusion MRI (dMRI), and FSL's Voxel-Based Morphometry (FSLVBM) to investigate the differences in grey matter volume and white matter connectivity between elite athletes and non-athletes. I will perform the analysis using Python-based tools, such as Nilearn and Dipy.  

### Tools

This project relied on numerous tools such as:
1. Git and Github for Version Control
2. FSLVBM to preprocess and analyse grey matter volume differences
3. FSL FIRST tool for automatic segmentation of a number of subcortical structures.
4. Python-based tools, such as Dipy and Nilearn, to preprocess the data, perform tractography analysis, and investigate white matter connectivity differences
5. Google Colab and Jupyter Notebook

### Data

I've used a publicly available dataset on college-level athletes for this project. From the dataset, I have chosen data of nine Indiana University (IU) football players (American football) and nine controls (non-athletes) and wish to carry out an AmFB>NonAth comparison as well as NonAth>AmFB comparison.

Please check the Participants' Info Used in this Project here:
Results/Participants_INFO.csv

Information about Dataset:
https://www.nature.com/articles/s41597-021-00823-z

Link to download the dataset:
https://brainlife.io/pub/5f2c3765beafe924c962dd8d

### Deliverables

At the end of this project, these files will be made available:
- Reproducible project workflow, detailed in the GitHub repository with codes
- Jupyter notebooks of the analysis codes and visualisations
- Figures of the results

## Results

### Progress overview

**Data Preprocessing**
> MRI data have been preprocessed using FSL tools.

![Data Preprocessing](Images/005.png)

**Voxel-Based Morphometry (VBM) Analysis**
> Grey matter volume differences between athletes and non-athletes have been investigated using FSLVBM [FMRIB's Software Library - Voxel-Based Morphometry]

OUTPUT

NonAth>AmFB

Showing the local differences in grey matter volume between the two groups:

![VBM_Analysis](Images/010.png)

To obtain statistical data, identify the region of significant difference and validate that:

[1] E2 - Running randomise and displaying cluster-based thresholding results
> Reference: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLVBM/UserGuide

OUTPUT

![VBM_Analysis](Images/011.png)

[2] Reporting Cluster Information
> Reference: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Cluster#reporting

OUTPUT

![VBM_Analysis](Images/012.png)

**Vertex Analysis**
> Automated segmentation of subcortical structures in the brain has been completed using FSL FIRST [a model-based segmentation/registration tool] tool.

OUTPUT

![Vertex_Analysis](Images/001.png)

Using this vertex analysis, marked differences in shape have been found in the two following areas: 

[1] Left-Putamen

![Vertex_Analysis](Images/L_Puta_first_02.png)

[2] Left-Thalamus

![Vertex_Analysis](Images/L_Thal_first.png)

### Future Work
**dMRI Analysis in Python**
> White matter connectivity will be explored using tractography methods implemented in Python-based tools such as Dipy and Nilearn.

### Tools I learned during this project

During the BrainHack School Project, I learned the following tools:

* **Python:** I learned how to use Python to analyse and manipulate data.
* **FSLVBM:** I learned how to operate FSLVBM to analyse grey matter volume differences between groups.
* **Nilearn:** I learned how to utilise Nilearn to perform functional MRI analysis and visualise data.
* **Dipy:** I learned how to use Dipy to perform diffusion MRI analysis and tractography.
* **Git and Github:** I learned how to use Git and Github for version control and collaboration.
* **Bash Terminal:** I learned how to employ the Bash Terminal to navigate and manipulate files and directories.
* **FSL FIRST tool:** I learned how to utilise the FSL FIRST tool for subcortical segmentation.
* **Google Colab and Jupyter Notebook:** I learned how to use Google Colab and Jupyter Notebook for interactive coding and data analysis.

## Conclusion and acknowledgement
Regarding the project, there are some promising results I've got. The short time at BrainHack School is overwhelming and challenging. But I am pleased with the new skills and knowledge I have gained throughout the program. I'll continue working on this project and try to investigate more athletes from different types of sports. 

I sincerely thank my advisor Professor Neil Muggleton and all the instructors and TAs (special shout-out to the Taiwan Hub) who have generously shared their expertise and provided guidance and support throughout the program. Thank you so much for this amazing opportunity.

## References
### Tools / Tutorials 
**FSLVBM**

1. https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLVBM
2. https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLVBM/UserGuide
3. https://www.youtube.com/watch?v=L1B3Wm-wnyQ&ab_channel=FSLCourse

**dMRI Analysis in Python**

1. https://school-brainhack.github.io/modules/dmri_intro/
2. https://davi1990.github.io/talks/2021-11-05-dMRI_analysis_in_Python
3. https://carpentries-incubator.github.io/SDC-BIDS-dMRI/aio/index.html

**Relevant Research Papers**

1. https://www.frontiersin.org/articles/10.3389/fnhum.2014.00594/full
2. https://www.sciencedirect.com/science/article/pii/S0960982214009798
