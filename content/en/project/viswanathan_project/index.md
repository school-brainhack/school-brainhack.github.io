---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-05-16" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Resting State Functional network connectivity changes in reward network of adoloscents who are at risk for addiction."

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Subhasri Viswanathan]

# Your project GitHub repository URL
github_repo: https://github.com/subhasriviswa/viswanathan_project.git

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [resting- state, github, reward, brainhack]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project will walk you through visualizing functional network connectivity based on a custom mask of ROIs of interest and visualize those network changes across time"

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
Adolescence is characterized by significant brain developmental changes and I am interested in understanding the functional network connectivity changes from a developmental perspective and explore the influence of substance use on these developing brain networks.

### Main questions to answer

How does resting state functional network connectivity change as a function of development
### Objectives

To use nilearn to compute functional network connectivity measures
Visualization tools - plotly
To use Github for version control and data management


### Tools
 The following tools and libraries were used in this project

Github
Nilearn
Nibabel
Plotly

### Data
The data collected as a part of the Neuro Venture Trial where 155 adolescents were sub-sampled from the Co-Venture trial [Conrod, 2016](https://clinicaltrials.gov/ct2/show/NCT01655615) for a structural and functional neuroimaging study at three-time points namely T1 ( baseline), T2 ( 24 months from baseline ) and T3( 48 months from baseline). The study followed exclusion criteria of any major neuro-developmental disorders (e.g., autism), uncorrectable visual impairment or hearing deficits, severe mental health problems (e.g., schizophrenia, bipolar disorder), uninterruptible central nervous system medication, and any magnetic resonance imaging (MRI) contraindications like pregnancy or braces [Bourque et al., 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5153672/). All the participants underwent structural and functional neuroimaging with two cognitive tasks namely the Stop Signal task and the Monetary Incentive Delay Task at all three-time points. Timeline follow-back interviews were conducted face-to-face at each time point to assess alcohol and drug use patterns over the last 6 months.

### Deliverables

At the end of this project, we will have:
1. A Jupyter notebook : 
	The Jupyter notebook has cells explaining in detail the above mentioned steps with comments on each cell to navigate through this workflow
3. Documentation as Git Repo markdown: 
       This is the readme file which will be the overview of the project 
 

## Results

A sample of n = 20 was used for the sake of the project at Brain Hack School 2023. The preprocessed data at each time point namely baseline (Time point 1), Time point 2 and Time point 3 were used and the following steps were carried out
1. Using nilearn's NiftiMasker the data was first masked to remove any background and noisy voxels
2. Further the data was thresholded and inverse transformed back to a nibabbel supported image for further computations

For understanding the resting- state functional network connectivity in reward networks, a winner take all based parcellation co-ordinate atlas called the [Seitzman Atlas](https://www.sciencedirect.com/science/article/pii/S105381191930881X)was used. This atlas was choosen due to the fact that the Atlas included sub -cortical regions and an exsisting reward network definition. Thus with Atlas, it is easy for visualizing and computing functional network connectivity in reward network.

3. Further the Niftisphere masker was used to create a mask based on the reward network ROI information. With only MNI coordinates available for each ROI, closest possible anatomical label was taken from [Neurosynth](https://neurosynth.org)
4. The data was further fit in the custom mask based on the reward network 
5. Correlation coefficient for each participant was computed and average correlation coefficent for each time point was computed and ploted using libraries like nilearn and Plotly

![Screenshot 2023-06-09 at 1 26 38 AM](https://github.com/brainhack-school2023/viswanathan_project/assets/62513668/613e950d-2836-4d67-9254-cfc896dddf3c)


6. To understand the differences in connectivity matrixes across three time points, co-sine similarity matrix was computed for time point 1 and 2, 1 and 3 and 2 and 3. 
![Screenshot 2023-06-09 at 1 35 00 AM](https://github.com/brainhack-school2023/viswanathan_project/assets/62513668/ceaf8c31-9298-4cca-8e0e-139287701326)

7. Graph theory visualizations was done using the networkx library where a graph network was plotted based on correlation matrix at each time point where each ROI was an edge and at 0.5 threshold, we can see that different ROI pairs emerge at different time points. 

### Progress overview

The project was swiftly initiated by P Bellec, based on the existing template created in 2019 by Tristan Glatard and improved by different students. It was really not that hard. Community feedback is expected to lead to rapid further improvements of this first version.

### Tools I learned during this project

1. Nilearn
2. Nibabbel
3. Plotly
4. Networkx



## Conclusion and acknowledgement

Thus, this repo will walk you through visualizing functional network connectivity based on a custom mask of ROIs of interest and visualize those network changes across time
I would like to thank Brain Hack School 2023 team for their immense support and help. 

## References
1. Seitzman, B. A., Gratton, C., Marek, S., Raut, R. V., Dosenbach, N. U. F., Schlaggar, B. L., Petersen, S. E., & Greene, D. J. (2020). A set of functionally-defined brain regions with improved representation of the subcortex and cerebellum. NeuroImage, 206, 116290. https://doi.org/10.1016/j.neuroimage.2019.116290
2. Bourque, J., Baker, T. E., Dagher, A., Evans, A. C., Garavan, H., Leyton, M., Séguin, J. R., Pihl, R., & Conrod, P. J. (2016). Effects of delaying binge drinking on adolescent brain development: a longitudinal neuroimaging study. BMC psychiatry, 16(1), 445. https://doi.org/10.1186/s12888-016-1148-3
	

