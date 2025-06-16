---
type: "project" # DON'T TOUCH THIS ! :)
date: "16-June-2025" # Date you first upload your project.
# Title of your project (we like creative title)
title: Predicting general cognition from resting-state functional brain connectivity

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Ngieng Shih Yang]

# Your project GitHub repository URL
github_repo: https://github.com/NSYYYYY/BHS2025.git

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [regularized regression, resting-state, cognition, prediction]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: The purpose of the project is to compare various predictive models to compare the effectiveness of each predictive model and to identify important features that best contribute towards predicting general cognition. Additionally, the ideal number of features were also explored for each model.

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

This study was inspired by the potential to use various machine learning techniques to improve predictive performance of resting-state functional connectivity on various performances measures. Specifically for this project, 7021 features were utilised in an attempt to predict the cognition composite scores of children aged 9 - 10 years old. Participants were recruited as part of a larger multi-site study called the Adolescent Brain Cognitive Development (ABCD) study. This study aims to use the data obtained during the baseline assessment inconjunction with various regularized regression methods and predictive models in an attempt to better predict general cognition. The project consists of various steps such as 1) data consolidation and cleaning, 2) subsampling of data, 3) Training the model and 4)Results presentation.

### Tools

The "project template" project will rely on the following technologies:
 * Markdown, to structure the text.
 * Rstudio, for data cleaning, consolidation and visualization
 * Python (various packages) for model training, testing and visualization.
 * Adding the project to the website relies on github, through pull requests.

### Data
Permission has been granted for data use of the National Institute of Mental Health (NIMH) Data Archive.
The files utilise in this project were obtained from ABCD-HCP fMRI pipeline v0.0.2 by the DCANS lab team (Sturgeon et al., 2019) . Inclusion criteria included images that were not rejected due to incidental radiological findings, passing satisfactory protocol compliance, and passing FreeSurfer Quality Control. More details about the preprocessing process are detailed in prior work (Hagler et al., 2019).

The rsfMRI data was used to construct a matrix consisting of 119 x 119 nodes, based on parcellated cortical nodes from the schaefer 100 parcel, 17 network atlas (Schaefer et al., 2018; Thomas Yeo et al., 2011), with an addition of 19 subcortical nodes, including the cerebellum from the FreeSurfer Aseg Atlas, resulting in 7,021 unique connections.

### Deliverables

#### Steps for running the entire analysis to visualization.

##### Step 1: Data consolidation and cleaning
Open the data_cleaning_CogComp_T1.Rmd (in RStudio). The top of the Markdown file indicates the necessary files to consolidate and clean the data. 
Ensure that all the files that is required has been retrieved.
Once the Markdown file has been ran, files will be generated for the next step

##### Step 2: Subsampling of the data
Use the subsampling.ipynb to subsample the data into the preferred subsample size.
In this stage, the remaining sample will be saved as a different CSV file for potential future use.

##### Step 3: Training the model
Next, use the subsample_ml_v5.ipynb to train, test and visualize the model.
The labels for the model can be found in 7021Labels.csv.
The output will be saved as both .joblib files and .csv files for future use.

##### Step 4: Connectogram creation
This step uses the CSV files that were obtained from step 3 to create a connectogram in RStudio.
Use the Connectogram_Script_Rstudio_...v2.R to create th connectograms. (There are three different, one for each model)
This step requires an additional labelsFC_schaefer119.csv file (that I am not too sure if I am allowed to share, hence not available)


### Tools I learned during this project

 * **Scikit_learn-** This is such a powerful package for running machine learning modelling and various different forms of regression for predictive purposes.
 * **Matplotlib.pyplot-** Powerful visualization tool that allows generation of various different types of charts and figures to better visualize results that is otherwise very hard to understand.
 * **Tool_flexibility** Through the project I learnt to utilise various tools that are best able to do what I require. I learnt not to be too focused on just utilising only 1 specific tool and software and to explore various options that can best fit my workflow.

### Results
The results suggest that Elastic Net regression achieves the best results in balancing predictive performance and the number of features. Ridge regression achieves the best results as it utilizes all of the features to generate a prediction. Lasso regression is useful only when a small number of features were to be extracted and used for future predictions. SVR performance was poor likely due to the low sample size that was utilise for model creation due to time constraints.

## Conclusion and acknowledgement

Overall, the results seem to show low predictive performance of resting-state functional connectivity on predicting general cognition. This is somewhat to be expected as resting-state mri is task-free and does not involve and tasks for the participant to conduct during the mri scan. Even so, there does seem to be some merit in utilising such machine learning methods in predicting various abilities.
