---
type: "project" # DON'T TOUCH THIS ! :)
date: "2024-06-21" # Date you first upload your project.
# Title of your project (we like creative title)
title: "ADHD diagnosis prediction using machine learning"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Iangola Andrianarison]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2024/andrianarison_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [machine learning ,fmri, classification, adhd]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project trains machine learning classification models to make predictions of adhd diagnosis from brain fRMI connectivity measures which are obtained from a resting state ADHD dataset . The main goals of this project are to get more practice with machine learning tools and to learn how work with brain data more precisely fMRI data."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "brain_image.jpeg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

I am a MSc student at  the University of Montreal studying computer science. I completed my BSc in neuroscience at the University of Toronto and I am interested in the intersection between the two fields and hoping to learn more about the application of machine learning in neuroscience.    

This project's goal is to train classification machine learning models to make predictions of ADHD diagnosis from fMRI data in order to learn how to work with fMRI brain data and become more familiar with machine learning tools. 

### Tools

The project rely on the following technologies:
 * Git and Github for version control 
 * Python libraries such as ScikitLearn for machine learning, Nilearn for fMRI connectivity analysis and Pyplot, Ploty Express and Seaborn for data visualization
 * Jupyter Notebook 

### Data

The data used for this project is the Nitric ADHD resting-state dataset which is preprocessed and available through Nilearn. The preprocessed data contains data from 30 subjects (13 ADHD, 17 control).

Information about the dataset: https://nilearn.github.io/dev/modules/description/adhd.html

Information on how to access the data : https://nilearn.github.io/dev/modules/description/adhd.html

### Deliverables

 - Jupyter notebook containing the code and visualization plots for the exploration of the data as well as the fMRI connectivity analysis
 - Python script for the training, testing and evaluation of the machine models
  - Figures and results summarizing the performances of the models 
  - [Github repo](https://github.com/brainhack-school2024/andrianarison_project)
 
## Results

### Tools I learned during this project

 * **Machine learning with scikitlearn** 
 * **Github workflow** 
 * **Getting fMRI connectivity using nilearn** 
 * **Data visualization using pyplot, ploty express and seaborn** 

### Results

#### Getting connectivity data using nilearn

Brain connectivity measures were obtained using nilearn. The BASC multiscale atlas with 64 regions of interest (ROIs) was used for masking.

Information about the atlas can found at: https://nilearn.github.io/dev/modules/description/basc_multiscale_2015.html 

A plot of the atlas can be seen below:
![atlas](atlas.png)

A region x region correlation matrix was obtained for each subject. These matrices were used as features for the machine learning models (targets are adhd diagnosis). The feature matrices for adhd and controls subjects can be seen below: 
![features](features.png)

#### Classification models performances 

For each model, the accuracy score (# corrected prediction / total # predictions) and F score (2 * (precision * recall / precision + recall)) were calculated. The best models were the decision tree and the random forest with accuracy score of 0.67 and F1 score of 0.75.
![performances](classifier_performance_comparison.png)

A confusion matrix for each model was obtained and can be seen below. The matrices shows the counts of true positive, true negative, false positive, and false negative predictions for each model.
![confusion_matrices](confusion_matrices.png)

## Conclusion and acknowledgement

Because of the very small size of the data, the results of this project are not significant in term of making predictions using machine learning. To have more meaningful results a much bigger dataset would be needed so that the models can train with low risk of overfitting and underfitting. However, completing this project was still meaningful in terms of learning how to use to tools and working with neuroscience data for the first time. 

Thank you to all the instructors, teaching assistants and organizers for this learning opportunity. 
