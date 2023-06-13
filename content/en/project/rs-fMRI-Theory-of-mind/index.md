---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-05" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Unveiling Children's Theory of Mind with rs-fMRI"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Wei-Hung Lin, Syuan-Yu Lin]

# Your project GitHub repository URL
github_repo: https://github.com/WeiHungLin/Unveiling_children_ToM_with_rsfmri

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website: 

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [theory of mind, rs-fmri, machine learning]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects.

summary: "Can functional connectivity bed used to predict children’s theory of mind (ToM)? This project utilizes supervised machine learning algorithms on the fMRI data to predict children’s ToM ability. For better visualization, the most contributing brain region connections are displayed on the brain."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "Cover_image_machine_learning.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Theory of mind (ToM) refers to the ability to understand people's mental states and use them to predict people’s behaviors; therefore, ToM plays a crucial role in social interactions, communication, and cognitive development. Previous study showed that people with higher ToM ability exhibit stronger functional connectivity than those with lower ToM ability (Marchetti et al., 2015). With this finding, we might be able to use children's functional connectivity signatures to predict their ToM ability. Thus, our project goal is to make use of the machine learning techniques we learned in Brainhack School to predict children’s ToM ability based on their resting-state functional connectivity.

### Tools

This project relys on the following technologies:
 * Matplotlib and seaborn for data visualization
 * Nilearn and scikit-learn for constructing machine learning algorithms
 * VS Code and Google Colab for programming
 * GitHub for Version Control

### Data

We selected a preprocessed resting-state fMRI dataset from Nilearn Development fMRI to conduct our project. This rs-fMRI dataset comes from a study focusing on investigating the development of functionally specialized social brain regions, and the participants watched a short film while undergoing fMRI in the study. All children completed a custom-made explicit ToM task to measure their ToM ability. In our project, we mainly focused on the relationship between children’s ToM scores and the functional connectivity of the brain regions. 

### Deliverables

At the end of this project, we will have:
 - Predictive models with evaluation scores and figure
 - Interactive figures
 - Presentation slides and video
 - Project Report

## Project Presentation

<iframe width="560" height="315" src="https://youtu.be/uibv_AtFWyc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Results

### Progress overview

This project was initiated by Wei-Hung Lin and Syuan-Yu Lin on 30th May 2023 as the part of the Brainhack school, and the final presentation was delivered on 1st June 2023. The deliverables include python code, interactive plot, presentation slides and video.

### Tools I learned during this project

 * Nilearn: Python package for processing and visualizing neuroimaging data
 * Scikit-learn: Python package for conducting machine learning and evaluating the predictive model
 * Jupyter Notebook: Creating project slides

### Results

#### Deliverable 1: Predictive models with evaluation scores and figure

![Regression figure and the model evaluation scores](https://github.com/WeiHungLin/Unveiling_children_ToM_with_rsfmri/blob/main/Regression_figure_with_evaluation_scores.png)

#### Deliverable 2: Static and interactive figures

![Feature matrix and contributing brain region connectomes](https://github.com/WeiHungLin/Unveiling_children_ToM_with_rsfmri/blob/main/Static_connectome.png)

![Interactive Brain Connectomes Video](https://github.com/WeiHungLin/Unveiling_children_ToM_with_rsfmri/blob/main/Interactive_Figure.mp4)


## Conclusion

This project aimed to employ the knowledge in data visualization and machine learning techniques we learned in Brainhack School 2023 with neuroimaging data. The results of machine learning models reveal the coherent functional connectivity findings, even though the model still requires improvement in predicting children’s ToM ability based on their functional connectivity. 

In this exploratory project, we observed the pivotal role of OFC connections in predicting ToM ability. This finding is intriguing as we did not set any ROIs in our machine learning analysis, yet our results are consistent with previous research suggesting the importance of the OFC/vmPFC in ToM ability (Abu-Akel & Shamay-Tsoory, 2011; Leopold et al., 2012). 

However, the regression figure and the evaluation scores indicate that the current model only explains limited variance in the given data, and there could be two reasons for this:

 * The ToM score is negatively skewed and may somehow violate the linear model assumption. In addition, age is the significant confounding variable in predicting ToM ability in children. To increase the model predictability, we can transform the ToM score and contain age into the model.
 * In the current study, a parcellation scheme comprising 64 brain regions was utilized, with a majority of regions located in the left hemisphere. Previous research indicates that the development of ToM ability is more closely associated with the left hemisphere compared to the right hemisphere (Marchetti et al., 2015). However, to capture a more comprehensive understanding of the relationship between functional connectivity and ToM ability, the use of a bilateral atlas can be considered. Alternatively, focusing on primary ROIs, such as the prefrontal cortex, may provide deeper insights into the association between functional connectivity and ToM ability.

Overall, this preliminary project provides some inspiring findings, but we still need to try other machine learning algorithms and more data to develop a more robust model to predict the ToM ability with functional connectivity.
 
## Acknowledgement
Gratitude to all the organizers, instructors, TAs, and fellow participants from all around the world who helped us learn all these cool open neuroscience tools and give us this opportunity to connect with all the great neuroscientists in the world. 

Special thanks to our instructor Charlene Lee, and our TA Ingrid Chuang for their inspiring work and assistance with our project.

## Reference
* Abu-Akel, A., & Shamay-Tsoory, S. (2011). Neuroanatomical and neurochemical bases of theory of mind. Neuropsychologia, 49(11), 2971-2984.
* Leopold, A., Krueger, F., dal Monte, O., Pardini, M., Pulaski, S. J., Solomon, J., & Grafman, J. (2012). Damage to the left ventromedial prefrontal cortex impacts affective theory of mind. Social Cognitive and Affective Neuroscience, 7(8), 871-880.
* Marchetti, A., Baglio, F., Costantini, I., Dipasquale, O., Savazzi, F., Nemni, R., ... & Castelli, I. (2015). Theory of mind and the whole brain functional connectivity: Behavioral and neural evidences with the Amsterdam Resting State Questionnaire. Frontiers in psychology, 6, 1855.