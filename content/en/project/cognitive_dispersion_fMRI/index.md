---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-14" # Date you first upload your project.
title: "2025 Brainhack School (Mini-)Project - Cognitive Dispersion and Its Neural Correlates"
names: [Truc (Curt) Nguyen]
github_repo: https://github.com/curt-1711/Curt_brainhack_project
# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:
# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
tags: [neuropsychology, fMRI, cognitive dispersion, default mode network]
summary: "This mini-project for the 2025 Brainhack School is part of my PhD dissertation on Late-Life Cognitive Heterogeneity, where I examine the neural correlates of cognitive dispersion -- a measure of within-individual variability -- using neuropsychological and fMRI data from the Midnight Scan Club dataset (OpenNeuro ds000224)."
#image: ""
editor_options: 
  markdown: 
    wrap: 72
---

<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Cognitive dispersion is a measure of intra-individual fluctuations
across a range of neuropsychological tests, operationalized as the
standard deviation of scores across multiple cognitive domains or tasks
during one occasion. One of the most prevailing speculations regarding
the mechanism of dispersion is the disruption of functional
connectivity. However, these studies have primarily consisted of
cross-sectional findings, i.e., scans that were acquired at a single
time point, examined group-average brain, with RS-fMRI scan length
lasting 5–6 minutes—an approach that might not fully capture functional
brain organization at the individual level. While conventional fMRI
studies have strived to increase the sample size, more recent works have
directed attention towards *precision functional mapping*, i.e.,
collecting large amounts of data at the individual level.

Here I (a third year PhD student in Neuroscience at National Taiwan
University / Academia Sinica as of June 2025) propose to use
state-of-the-art precision functional mapping tools to determine brain
activity patterns associated with cognitive dispersion. As a
proof-of-concept (pilot) study, I will be using the neuropsychological
and fMRI data from the Midnight Scan Club dataset (OpenNeuro ds000224)
to examine the neural correlates of cognitive dispersion.

### Tools

-   MATLAB;
-   CONN toolbox, an SPM-based software for the analysis of functional
    connectivity;
-   Utilities by the authors of the Midnight Scan Club dataset
    ([github](https://github.com/MidnightScanClub/MSCcodebase/tree/master));
-   Tutorials to run the *precision functional mapping* pipeline (Lynch
    *et al., Nature* 2024;
    [github](https://github.com/cjl2007/PFM-Depression/tree/main)) and
    the *multi-session hierarchical Bayesian modeling* (Kong *et al.,
    Cereb Cortex* 2019;
    [github](https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Kong2019_MSHBM)).

### Data

The Midnight Scan Club dataset (Gordon *et al.*, Precision Functional
Mapping of Individual Human Brains, *Neuron* 2017; OpenNeuro
[ds000224](https://openneuro.org/datasets/ds000224/versions/1.0.4)).

### Deliverables

Presentation, R & CONN files.

## Results

### Progress overview

During the three weeks that I had to work on this mini-project, I ran
into multiple errors in MATLAB (details in the PDF file of my
presentation). After hours (and hours) of troubleshooting and as the
deadline to submit my project approached, I resorted to use the CONN
toolbox for a quick analysis of the resting-state fMRI data from
Midnight Scan participants.

### Tools I learned during this project

-   **Human Connectome Workbench** to visualize the CIFTI files
    (derivatives).
-   **MATLAB** running code and troubleshooting.
-   **CONN toolbox** for fMRI data preprocessing and functional
    connectivity analysis.

### Results

#### Deliverable 1: report presentation 

File name: *Truc Nguyen (Curt NTU TW D11B49004)\_BrainHack final
presentation.pdf*

#### Deliverable 2: R files to calculate dispersion 

File name: *curt_MSC_brainhack.R* and *MSC_test.xlsx* (Sheet 3)

#### Deliverable 3: CONN files 

File name: *conn_curt_project_01_to_04.mat* and
*CONN_methods_2025_06_10.html*

## Conclusion and acknowledgement

Many, many thanks to the 2025 Brainhack School Organizers (Faculty and
TAs)! I have learned so much from you and my peers this semester.
