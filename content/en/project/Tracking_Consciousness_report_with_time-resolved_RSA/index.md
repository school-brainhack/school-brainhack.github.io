---
type: "project" 
date: "2025-06-15"
title: "BHS_trRSA_project"
names: [Xu Peng]
github_repo: https://github.com/pengxu1308/BHS_trRSA_project
tags: [tr-rsa, consciousness, decoding, rsa]
summary: "Implementing Time-Resolved Representational Similarity Analysis to Track Cortical Representation of Consciousness Report"
image: "RSA.png"
---

## Project definition

### Background

Understanding the neural basis of consciousness remains a central challenge in cognitive neuroscience. A widely used framework is the study of Neuronal Correlates of Consciousness (NCC)—neural signals that reliably track the presence of conscious experience. Within EEG research, two ERP components have been proposed as NCCs: Visual Awareness Negativity (VAN) and Late Positivity (LP). These are often discussed in the context of the early-vs-late debate on the temporal onset of consciousness.

However, leading theories diverge in interpretation. Recurrent Processing Theory posits that consciousness arises when early visual signals are processed recurrently, not just feedforwardly. Yet this theory lacks direct EEG evidence linking such recurrent activity to VAN or LP. Meanwhile, Global Neuronal Workspace Theory suggests that consciousness emerges through a late, all-or-none “ignition” process—possibly reflected in LP—but similarly lacks precise mapping to ERP dynamics.

Recent studies challenge the binary view altogether, proposing that consciousness may unfold gradually over time. For example, Colombetti et al. identified multiple components contributing independently to awareness, while Cohen et al. modeled conscious access as a graded neural representation.

Given these perspectives, traditional ERP methods may be too limited to capture the full complexity of conscious processing. This project applies time-resolved Representational Similarity Analysis (RSA) to investigate whether VAN and LP reflect recurrent processing, ignition, or graded accumulation. By comparing neural and behavioral RDMs across time using whole-scalp EEG patterns, and leveraging tools from the BrainHack School RSA pipeline, this approach aims to provide new insights into the dynamics of visual consciousness.

### Tools

The tr-RSA project will rely on the following technologies:
 * EEG MNE-python. Most the analysis are done within MNE-python.
 * Open Science Framework. Where the data is downloaded.
 * Adding the project to the website relies on github, through pull requests.
 * The function is written in python script in vscode.
 * The environment is controlled by ANACONDA.


### Data

The data is download from [OSF](https://osf.io/xz8jr/). All the data is collected from a published paper by [Railo et al, 2021](https://onlinelibrary.wiley.com/doi/10.1111/ejn.15354). 

### Deliverables

After completing this project, we will obtain:

- Representational Dissimilarity Matrices (RDMs) of EEG data across time bins, aligned with behavioral factors.
- Well-documented RSA pipelines for both individual and group-level analysis, including split-half reliability tests, permutation tests, and more.
- Insights into cortical representations through time-resolved multivariate analysis.

## Results

### Progress overview

This project employs a multivariate pattern analysis (MVPA) approach to investigate the time series of conscious experience. Specifically, trial-by-trial neural Representational Dissimilarity Matrices (RDMs) were constructed for each 50 ms time bin. Principal Component Analysis (PCA) was applied for dimensionality reduction and result visualization, followed by split-half reliability testing to assess the consistency of neural patterns over time.

In parallel, three behavioral RDMs were created to capture the structure of participants’ stimulus-response relationships. Representational Similarity Analysis (RSA) was then conducted by comparing the neural and behavioral RDMs to quantify their correspondence.

### Tools I learned during this project

 * **EEG data analysis** I learn how to deal with EEG data from 0.
 * **Representational Similarity Analysis-** Basic concepts of doing RSA.
 * **Dimension reduction method** Through this project, I compared different methods of dimensionality reduction and evaluated various options for variance retention.

### Results

The RSA results revealed that the neural-behavioral correlation began to increase around 250 ms after stimulus onset, particularly with respect to the subjective clarity ratings. The correlation peaked around 400 ms, followed by a slight dip, and then entered a plateau phase between approximately 600–1000 ms. Notably, nearly the entire EEG epoch exhibited significant RSA values.

These findings suggest a strong relationship between neural representations and subjective clarity reports. Future analyses—especially those incorporating reaction time or additional behavioral measures—are encouraged and may benefit from consulting the original data contributor for more detailed behavioral response information.

#### Deliverable 1: Neural RDMs for each subject with vairas validation method.

You can find out a interactively visualization results in the Jupyter Notebooks. Futhermore, the notebooks contain validation cells that users can play around with to find different results(such as changing to 90% variance retainsion within dimension reduction.)

#### Deliverable 2: Behavioral RDSm for each sunject

In the notebooks, you can also find out the behavioral RDM to see the response pattern for participants.

#### Deliverable 3: Individaul RSA and group-level RSA

Not only the individual RSA is done but also the group level RSA is implemented to see the trend of the time series from consciousness response.

## Conclusion and acknowledgement

In conclusion, although the analysis was carried out successfully, the interpretation of the results remains limited due to the absence of participants’ reaction time data. Without precise behavioral response timing, it is difficult to fully understand or contextualize the RSA values.








