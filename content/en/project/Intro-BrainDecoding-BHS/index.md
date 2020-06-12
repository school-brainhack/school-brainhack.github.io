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

<div align="center">
<img src="Brain_decoding.jpg" width="687" height="376" allowfullscreen> 
</div>


### Tools
* Git/Github
* Nilearn & sklearn
* Python visualization, statistics and machine learning libraries (e.g. NumPy, Seaborn, scikit-learn, Matlplotlib, nibabel, graphviz, and pydotplus)
* Compute Canada/ Calcul Québec
* Binder

### Data
For BHS project I used Haxby dataset which is a high-quality block-design fMRI dataset from a study on face & object representation in the human ventral temporal cortex (This cortex is involved in the high-level visual processing of complex stimuli). It consists of 6 subjects with 12 runs per subject. In this experiment during each run, the subjects passively viewed greyscale images of 8 object categories, grouped in 24s blocks separated by rest periods. Each image was shown for 500ms and was followed by a 1500ms inter-stimulus interval.

## Results
<div align="center">
<img src="Confusion_matrices.jpg" width="687" height="376"> 
</div>

<div align="center">
<img src="clfs.jpg" width="584" height="362"> 
</div>

### Progress overview
When I started this course I had almost no background of machine learning and deep learning also no personal experience about using Git/Github and compute Canada. During the first two weeks, I was trying to digest the information that I was given during BHS training week also practicing and learning by following different tutorials.
From third week I started to run the codes and push them on my repository, mostly by following Nilearn and sklearn tutorials, also I experimented and personalized them.
During the last two weeks, I tried to write my own codes by doing several classification approaches on the Haxby dataset. This goals for me needed a lot of reading to learn about classifiers algorithms and the way they work also their strengths and weaknesses to figure out why some classifiers perform better compared to the rest. In addition, I used some performance metrics in order to check my ML models such as "Classification Accuracy”, "Cross-Validation" and “Confusion Matrix”. In the end,  I added documentation to make my notebook easy to follow for those who are new in this field and plotted the results interactively. 
After doing all the mentioned tasks, I tried my first model training experiment and as I mentioned above I chose ANN. (I still need to work on this notebook since it dosen't return the good result)

Besides, I have wrote down all my goals divided per week in my repository README file under "TO-DO LIST " title.

### Tools I learned during this project

 * **Git/Github** 
 * **Terminal and Shell commands:** I feel more comfortable using commands.
 * **Compute Canada/Calcul Quebec** I learned how to upload files and run scripts on compute Canada.
 * **TensorFlow** I got exposed to TensorFlow but still need to learn more.
 * **New python libraries**
 * **Binder**
 
In general, this course taught me how to make a deliverable project based on open-science.

### Results

### Deliverables

* [Jupyter Notebook with code to produce plots of my results](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Data-visualization.ipynb)
* [Jupyter Notebook with code for comparing different classifiers](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Classifiers.ipynb)
* [Jupyter Notebook with code for Artificial Neural Network model training](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/ANN_onHaxby.ipynb)
* [Jupyter Notebook with code for introduction to brain decoding](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/BHS_Haxby_BrainDecoding.ipynb)
* [Batch script used on Compute Canada to run BHS_Haxby_BrainDecoding.py script](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/BHS_Batch.sh)
* [Github repository including project description with all mentioned Jupyter Notebooks clearly commented](https://github.com/brainhack-school2020/BHS_project_SRastegarnia)
* [First](https://drive.google.com/open?id=1ABaOXwWPks8xB28OlkiwDvqx7D0B2htQ) and [Final](https://drive.google.com/file/d/1qFHRrdjRLgfP-5dDYNs12vHyDhFCYVp6/view?usp=sharing) presentation slides
* Final report summarizing the entire project


##### Future plan
My future goal post brain hack school would be increasing my knowledge of machine learning and deeplearning and training and learning about different models including GCN!

## Special thanks to:
Pierre Bellec, Désirée Lussier,Valerie Hayot and Jacob Vogel for all their help and support during Brain hack school time!

## Aknowledgments

<img src="logo.png" width="1000" height="100"> 
