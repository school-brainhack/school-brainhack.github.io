---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-11" # Date you first upload your project.
title: "Dynamic Functional Connectivity of the Default Mode Network in ADHD"

names: [Malikka Begum Binte Habib Mohamed]

github_repo: https://github.com/malikkabegum/malikkabegum_project

website:

tags: [brainhack, ADHD, neuroimaging, connectivity]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project examines dynamic functional connectivity (dFC) within the Default Mode Network (DMN) in children with ADHD using the ADHD-200 dataset. Key methods of analyses include time-varying correlation, clustering of connectivity states, and group comparisons to understand how brain network dynamics differ in ADHD"
image: "Deliverable 2_Brain regions.png"
---

## Project definition

Attention-Deficit/Hyperactivity Disorder (ADHD) is associated with disruptions in large-scale brain networks, particularly the Default Mode Network (DMN). While many studies focus on static connectivity, dynamic functional connectivity (dFC) offers a time-resolved view of how brain regions interact across time. This approach may uncover temporal patterns in connectivity that differ between typically developing children and those with ADHD.

This project leverages resting-state fMRI data (.1D) from the ADHD-200 dataset and investigates time-varying functional connectivity between DMN regions using the sliding window method. 

### Background

Resting-state fMRI data allows us to study intrinsic brain network connectivity without task constraints. The Default Mode Network (DMN, including regions such as the medial prefrontal cortex (mPFC), posterior cingulate cortext (PCC), and angular gyrus, has shown atypical patterns in children with ADHD. This project uses dynamic functional connectivity (dFC) methods to analyse how these patterns change over time in ADHD versus typically developing children. 

The data is from the publicly available ADHD-200 dataset (http://fcon_1000.projects.nitrc.org/indi/adhd200/) sample, using preposed time series data from the Athena pipeline and focusing on DMN-related ROIs based on the AAL atlas. 

### Tools

The "project template" project will rely on the following technologies:
 * Markdown, to structure and format the project description text.
 * The Hugo website framework which is used by the BHS website. This makes it possible to easily add the markdown project description to the website.
 * Adding the project to the website relies on github, through pull requests.

### Data

The ADHD-200 dataset was used for this project. Ultimately, this project template will be used by all BrainHack School (BHS) participants. Data from various projects will be aggregated on the following page, creating an example gallery for future BrainHack School students. 

### Deliverables

At the end of this project, we will have:
 - a completed and revised markdown document detailing the dynamic functional connectivity analysis of the Default Mode Network in ADHD using the ADHD-200 dataset. 
- a gallery entry showcasing this project alongside other student projects from BrainHack 2025.

## Results

Dynamic correlation matrices were computed for each participant using a sliding window approach.
Group-level state metrics (e.g., number of transitions, mean dwell time) were compared across ADHD and control groups.
Reduced DMN coherence in ADHD, particularly between the left medial superior frontal gyrus and PCC.
ADHD participants spend less time in strongly connected DMN states. 
The left medial superior frontal gyrus showed a statistically significant difference (p < 0.05) in connectivity strength - possibly indicating a regional hub alteration in ADHD.

### Progress overview

The analysis pipeline was implemented from scratch and validated using multiple test cases. Dynamic connectivity states were successfully derived from all participants, and significant group differences were identified in key metrics, particularly involving the mPFC-PCC connection. 

### Tools I learned during this project

How to extract and preprocess region-specific time series from fMRI.
Dynamic functional connectivity analysis using sliding windows.
Means clustering on correlation matrices.
Visualization of brain network dynamics.
Using Git and GitHub for documentation and reproducibility. 

### Results

#### Deliverable 1: significant differences between ADHD and typically developing children.

Reduced dwell time and lower connectivity strength in specific DMN states among ADHD participants (refer to images). 

#### Deliverable 2: specific affection regions

mPFC-PCC showed the most robust group difference, suggesting a central role in DMN disruption in ADHD (refer to images).

##### Dynamic Functional Connectivity in ADHD pipeline by Malikka Begum

The repository of this project can be found here (https://github.com/malikkabegum/malikkabegum_project). The objective was to investigate alterations in the dynamics of the Default Mode Network (DMN) in children with ADHD using resting-state fMRI data from the ADHD-200 dataset. The motivation behind this task is to study the dynamic properties of connectivity to offer deeper insights into the neural mechanisms underlying attentional instability and cognitive variability in ADHD. The repo features:
* a Jupyter notebook for the full dFC analysis pipeline using sliding window correlations, means clustering, statistical comparison scripts to assess group differences in state frequency, dwell time and ROI-ROI connectivity. 
* a detailed README
* figures showing state patterns and group comparisons
* Detailed requirements files, making it easy for others to replicate the environment of the notebook.

## Conclusion and acknowledgement

This project highlights altered dynamic network behaviour in ADHD, especially within the core DMN. It adds to growing evidence that temporal dynamic-not just static connectivity-may underlie attentional difficulties. Thanks to the BrainHack School Singapore and Taiwan teaching team, especially Prof Chen, Dr. Goh for their invaluable support and guidance and the supportive TAs for guidance throughout. 
