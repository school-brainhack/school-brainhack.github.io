---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-10" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Do you feel the words? An fMRI analysis on tactile vs non-tactile words in Mandarin Chinese"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Yusuke Taira]

# Your project GitHub repository URL
github_repo: https://github.com/NTUsuke/Yusuke_Taira_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI,parietal lobe, somatosensory cortex, tactile word]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Language consists of many thousands of words which differ in meaning and syntactic category. Some words may refer to reletevely touchable, hence concrete aspects of the world while others are abstract in meaning which do not have physical references. But which brain areas are associated with tactile word processing? This project aims to investigate brain activation of participants when listening to tactile vs non-tactile word stimuli. The preliminary result shows that large areas of parietal lobe is particularly activated to tactile words compared to non-tactile words"

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

This project aims to explore brain activation of participants when presented with tactile words in Mandarin Chinese. The data used is from an OpenNeuro dataset which contains 672 stimulus words and functional data of 11 Chinese participants. My personal goal of this project is to familiarize myself with python, statistics and basic fMRI analysis techniques since I had no experience in any of them. For data analysis, I used General Liniear Model analysis to investigate brain responses to the stimulus words.


### Tools

The project relies on the following technologies:
 * This README is built using [Markdown](https://guides.github.com/features/mastering-markdown/), to structure the text.
 * Extraction, analysis and visualization of fMRI data is done with `nilearn`
 * The detail of this project is stored in a [Jupyter Notebook](https://jupyter.org/index.html)

### Data

The dataset contains 672 words of Mandarin Chinese with semantic ratings ranged from 0-7 and functional data of 11 participants recorded while listening to the stimulus words.
The functional data are all preprocessed and available from [OpenNeuro website](https://openneuro.org/datasets/ds004301/versions/1.0.2)

### Deliverables

At the end of this project, I'll have :

 * Markdown README.md for the description of the current project
 * Jupyter notebook including the code, and the fMRI brain images

### Tools I learned during this project
 For completing this project, one will need:
 * **Nilearn** for loading and visualizing fMRI data
 * **Numpy** to manipulate arrays
 * **Pandas** to manipulate dataframe

### Results

Left hemisphere was more activated compared to the right in general as all the stimuli were speech sounds. 
In terms of activation areas compared to non-tactile words, tactile words activated large areas of parietal lobe where somatosensory cortex is located at but also partially activated visual cortex. It might be due to overlapping features of tactile and visual words.


![Alt text](fmri_tactile.png)

### Conclusion and Limitations

This project aimed to investigate brain activation when presented with tactile vs non-tactile words. Although there was a strong tendency that the somatosensory cortex was particulary activated, no area was significantly activated when setting a threshold as 3.0 in z-score which implies the necessesity of larger amount of data.  It is also unfortunate that my pc leads to kernal crash every time I try to analyze data of 5 or more runs and this inhibited me from second level analysis.

## Acknowledgements
This project taught me a lot and I can not believe that I could learn python, statistics, GLM and fMRI analysis at the same time in such a limited amount of time. About a few months ago, I had no idea where to start python and now I can use it to extract, analyze and visualize fMRI data! I'm quite sure that I couldn't have achieved this without Brainhack school.

In the end, I'd like to express my huge thanks to all of the organizers and TA's, especially Yu-Shiang without whom I could never have finished my project, and Dr.Josh and Dr. Lee, who hosted such as amazing program at National Taiwan University.

## References
[Wang, S., Zhang, Y., Zhang, X., Sun, J., Lin, N., Zhang, J., & Zong, C. (2022). An fMRI Dataset for Concept Representation with Semantic Feature Annotations. Scientific data, 9(1), 721.](https://doi.org/10.1038/s41597-022-01840-2)
