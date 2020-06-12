---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-05-16" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Intro to brain decoding, artificial neural network, and classification of Haxby dataset using six different common approaches"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Shima Rastegarnia]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2020/BHS_project_SRastegarnia

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/BHS_project_SRastegarnia), click `manage topics`.
# Please only lowercase letters
tags: [fmri, machine Learning, deep learning, classification, artificial neural network, brain decoding, visual stimuli]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Brain decoding or mind-reading using neuroimaging data has been an active topic for years. It is a neuroscience field that concerned about different types of stimuli from information that has already been encoded and represented in the brain by networks of neurons. My goals for this project are learning the fundamentals of brain decoding, comparing the performance of six different classifiers including "Naive Bayes", "Nearest Neighbours", "Neural Networks", "Logistic Regression", "Support vector machine" and "Decision trees" classifiers and finally training the Artificial Neural Network (ANN) models on Haxby dataset. I plot confusion matrix to also checked cross validation accuracy for all the classifiers.
Among all mentioned classifiers SVM has the best and Decision Trees classifier shows the worst performance. You can find the codes and results of [data visualization](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Data-visualization.ipynb), [classifiers](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Classifiers.ipynb), [ANN train](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/ANN_onHaxby.ipynb), and my initial efforts in order to learn about [brain decoding](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/BHS_Haxby_BrainDecoding.ipynb) by following the Nilearn and Sklearn tutorials inside my repository in brain hack school Github."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "Brain_decoding.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

I am currently a Master’s student in computer science at Université de Montréal. Since I am still in the early steps of my master’s project, my main goal was to learn as much as possible and making use of several tools that we have learned during BHS training courses. For this purpose, I ran and compare the results of the six common classifiers on the Haxby dataset. During the classification stage, I was trying to find the best results for each approach by examining different parameters. As an example, for Neural Networks classifier, my accuracy result increased significantly when I changed some parameters (it is indicated in the Classifiers.ipynb). 
This change of accuracy made me curious about training ANN on
the Haxby dataset to examine its performance and learn better about this method, that wasn't my plan at the beginning. Moreover, to make the notebook reproducible and easy to follow for those who don't have a background of machine learning (similar to me before Brainhack school!), I have added a full description of each cell and a quick overview of each classifier's theory.

<iframe width="560" height="315" src="https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Images/Brain_decoding.png" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Tools
* Git/Github
* Nilearn & sklearn
* Python visualization, statistics and machine learning libraries (e.g. NumPy, Seaborn, scikit-learn, Matlplotlib, nibabel, graphviz, and pydotplus)
* Compute Canada/ Calcul Québec
* Binder

### Data
For BHS project I used Haxby dataset which is a high-quality block-design fMRI dataset from a study on face & object representation in the human ventral temporal cortex (This cortex is involved in the high-level visual processing of complex stimuli). It consists of 6 subjects with 12 runs per subject. In this experiment during each run, the subjects passively viewed greyscale images of 8 object categories, grouped in 24s blocks separated by rest periods. Each image was shown for 500ms and was followed by a 1500ms inter-stimulus interval.

### Deliverables

For this project I have provided:
* Github repository including project description and all mentioned Jupyter Notebooks clearly commented.
* [First](https://drive.google.com/open?id=1ABaOXwWPks8xB28OlkiwDvqx7D0B2htQ) and [Final](https://drive.google.com/file/d/1qFHRrdjRLgfP-5dDYNs12vHyDhFCYVp6/view?usp=sharing) presentation slides
* Data visualization notebook with several plots
* BATCH script and running the BHS_Haxby_BrainDecoding.py on compute canada
* Final report summarizing the entire project

## Results

### Progress overview
When I started this course I had almost no background of machine learning and deep learning also no personal experience about using Git/Github and compute Canada. During the first two weeks, I was trying to digest the information that I was given during BHS training week also practicing and learning by following different tutorials.
From third week I started to run the codes and push them on my repository, mostly by following Nilearn and sklearn tutorials, also I experimented and personalized them.
During the last two weeks, I tried to write my own codes by doing several classification approaches on the Haxby dataset. This goals for me needed a lot of reading to learn about classifiers algorithms and the way they work also their strengths and weaknesses to figure out why some classifiers perform better compared to the rest. In addition, I used some performance metrics in order to check my ML models such as "Classification Accuracy”, "Cross-Validation" and “Confusion Matrix”. In the end,  I added documentation to make my notebook easy to follow for those who are new in this field and plotted the results interactively. 
After doing all the mentioned tasks, I tried my first model training experiment and as I mentioned above I chose ANN. 

Besides, I have mentioned all my goals divided per week in my repository README file under "TO DO LIST " title.

### Tools I learned during this project

 * **Meta-project** P Bellec learned how to do a meta project for the first time, which is developping a framework while using it at the same time. It felt really weird, but somehow quite fun as well.
 * **Github workflow-** The successful use of this template approach will demonstrate that it is possible to incorporate dozens of students presentation on a website collaboratively over a few weeks.
 * **Project content** Through the project reports generated using the template, it is possible to learn about what exactly the brainhack school students are working on.

### Results

#### Deliverable 1: report template

You are currently reading the report template! I will let you judge whether it is useful or not. If you think there is something that could be improved, please do not hesitate to open an issue [here](https://github.com/brainhack-school2020/project_template/issues) and let us know.

#### Deliverable 2: project gallery

There is not yet a project gallery, as BHS 2020 is the first edition that will incorporate it on the website. You can still check out the [2019 BHS github organization](https://github.com/mtl-brainhack-school-2019)

##### ECG pupilometry pipeline by Marce Kauffmann

The repository of this project can be found [here](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann). The objective was to create a processing pipeline for ECG and pupillometry data. The motivation behind this task is that Marcel's lab (MIST Lab @ Polytechnique Montreal) was conducting a Human-Robot-Interaction user study. The repo features:
 * a [video introduction](http://www.youtube.com/watch/8ZVCNeX42_A) to the project.
 * a presentation [made in a jupyter notebook](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann/blob/master/BrainHackPresentation.ipynb) on the results of the project.
 * Notebooks for all analyses.
 * Detailed requirements files, making it easy for others to replicate the environment of the notebook.
 * An overview of the results in the markdown document.

##### Other projects
Here are other good examples of repositories:
- [Learning to manipulate biosignals with python](https://github.com/mtl-brainhack-school-2019/franclespinas-biosignals) by François Lespinasse
- [Run multivariate anaylysis to relate behavioral and electropyhysiological data](https://github.com/mtl-brainhack-school-2019/PLS_PV_Behaviour)
- [PET pipeline automation and structural MRI exploration](https://github.com/mtl-brainhack-school-2019/rwickens-sMRI-PET) by Rebekah Wickens
- [Working with PSG [EEG] data from Parkinson's patients](https://github.com/mtl-brainhack-school-2019/Soraya-sleep-data-in-PD-patients) by Cryomatrix
- [Exploring Brain Functional Activation in Adolescents Who Attempted Suicide](https://github.com/mtl-brainhack-school-2019/Anthony-Gifuni-repo) by Anthony Gifuni

#### Deliverable 3: Instructions

 To be made available soon.

## Conclusion and acknowledgement

The BHS team hope you will find this template helpful in documenting your project. Developping this template was a group effort, and benefitted from the feedback and ideas of all BHS students over the years.

## Conclusion and acknowledgement
Plotting the used stimuli Haxby dataset: #https://nilearn.github.io/auto_examples/02_decoding/plot_haxby_stimuli.html#sphx-glr-auto-examples-02-decoding-plot-haxby-stimuli-py

Plot Haxby masks: https://nilearn.github.io/auto_examples/01_plotting/plot_haxby_masks.html#sphx-glr-auto-examples-01-plotting-plot-haxby-masks-py

Decoding with ANOVA + SVM: https://nilearn.github.io/auto_examples/02_decoding/plot_haxby_anova_svm.html#sphx-glr-auto-examples-02-decoding-plot-haxby-anova-svm-py

ROI-based decoding analysis: https://nilearn.github.io/auto_examples/02_decoding/plot_haxby_full_analysis.html#roi-based-decoding-analysis-in-haxby-et-al-dataset

Different multi-class strategies: https://nilearn.github.io/auto_examples/02_decoding/plot_haxby_multiclass.html#sphx-glr-auto-examples-02-decoding-plot-haxby-multiclass-py

Preparing the data: https://nilearn.github.io/auto_examples/plot_decoding_tutorial.html

k-Nearest Neighbours:

train_test_split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

KNeighborsClassifier(): https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

accuracy_score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html

LogisticRegression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

Support Vector Machine: 
https://scikit-learn.org/stable/modules/svm.html 

https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC

Neural Network:
https://scikit-learn.org/stable/modules/neural_networks_supervised.html 
MLPClassifier: 
https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier
