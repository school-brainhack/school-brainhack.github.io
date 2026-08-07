---
type: "project" # DON'T TOUCH THIS ! :)
date: "2026-06-09" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Task-Based Functional Connectivity for ME-ICA"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [John Lio, Arshiya Khurmi, Kelei Xiao, Pirinthiya Thayaparan]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2026/ME-ICA_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fmri, r-code, motor-task, functional-connectivity]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project develops a functional connectivity pipeline in R using multi-echo ICA (ME-ICA) denoising on a hand-grasp motor task fMRI dataset from openneuro (n=8). Using the Schaefer 200-parcel atlas, we extract ROI time series, apply confound regression and bandpass filtering, and compute Fisher z-transformed connectivity matrices across 2 runs per subject. Run-to-run consistency is assessed via Pearson r, and precentral gyrus (M1) connectivity is analyzed as a potential biomarker relevant to Parkinson's disease and stroke detection"

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "brainhackimage.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
Our group --> We are a group of undergraduate students conducting summer projects at the Centre for Addiction and Mental Health (CAMH) as a part of the Institute of Medical Science at the University of Toronto’s Summer Undergraduate Research Program (IMS SURP). Collectively, our summer projects focus on the various neurobiological mechanisms and outcomes associated with psychiatric conditions.

### Purpose
Project background --> Motor task functional magnetic resonance imaging (fMRI) is widely used to investigate motor function in neurological disorders such as Stroke and Parkinson's disease. However, these populations often exhibit increased head motion during motor tasks, producing signals which can obscure true neural activity, subsequently reducing the reliability of neuroimaging findings. A particular challenge is task-correlated motion, which occurs when head movement coincides with task performance, such as during hand-grasp movements, making it difficult to distinguish motion-related artifacts from task-associated neural activity. Multi-Echo Independent Component Analysis (ME-ICA) addresses this issue by combining multi-echo fMRI acquisition with independent component analysis (ICA) to separate blood oxygenation level-dependent (BOLD) signals from non-BOLD sources of noise, including head motion and physiological fluctuations. By removing noise-related components while preserving neural signals, ME-ICA may improve the accuracy and interpretability of motor-task fMRI analyses in populations prone to excessive movement.

### Tools
This project utilizes a variety of tools to support development and open access research practices -->
- RStudio: Core environment for building connectivity matrices and seed-based analysis
- Terminal: Unlocking the dataset from openneuro, and pushing the project onto Github
- Github: Communication and storage of project files

### Data
This project uses fMRI data from a study completed by Reddy et al., which aims to compare ME-ICA with other denoising tools in addressing noise associated with task-correlated motion. (https://doi.org/10.1101/2023.07.19.549746). The data and subject files come from the OpenNeuro dataset --> https://github.com/OpenNeuroDatasets/ds007661 / https://openneuro.org/datasets/ds007661/versions/1.0.0

## Results

### Progress overview
The final presentation of this project was delivered on June 5, 2026. All planned deliverables were completed and are available in the project’s GitHub repository.

### Tools we learned during this project
- RStudio & R: Throughout the course, we were grateful to have had hands-on experience using RStudio in processing neuroimaging data to produce connectivity matrices and ROI analyses.
- Terminal & Bash: We primarily learned how to use datalad to store larger datasets, which was particularly helpful as our computer storage was limited. 
- Github & Git: We learned how to use git push, git pull, and git commit to keep our project organized.

### Deliverables
Our main deliverables are available in a GitHub repository containing all figures (in the ["mfigures"](https://github.com/brainhack-school2026/ME-ICA_project/tree/main/mfigures) folder), connectivity matrices, ROI analyses, and R markdown files.
- (https://github.com/brainhack-school2026/ME-ICA_project)

## Conclusion and Acknowledgement
We would like to thank BrainHack School 2026 for providing us with immense amounts of support throughout our project. Particularly we are grateful for the TA team, who were particularly compassionate in their feedback and mentorship as we navigated the learning experience.

***

#### References
- Esteban, O., Markiewicz, C.J., Blair, R.W. et al. fMRIPrep: a robust preprocessing pipeline for functional MRI. Nat Methods 16, 111–116 (2019). https://doi.org/10.1038/s41592-018-0235-4 
- Neha A Reddy, Kristina M Zvolanek, and Molly G Bright (2026). Motor Task Multi-Echo fMRI - fMRIPrep Derivatives. OpenNeuro. [Dataset] doi: https://doi.org/10.18112/openneuro.ds007661.v1.0.0 
- Neha A. Reddy, Kristina M. Zvolanek, Stefano Moia, César Caballero-Gaudes, Molly G. Bright bioRxiv 2023.07.19.549746; doi: https://doi.org/10.1101/2023.07.19.549746
- Reddy, N. A., Zvolanek, K. M., Moia, S., Caballero-Gaudes, C., & Bright, M. G. (2023). Denoising task-correlated head motion from motor-task fMRI data with multi-echo ICA. bioRxiv. https://doi.org/10.1101/2023.07.19.549746
