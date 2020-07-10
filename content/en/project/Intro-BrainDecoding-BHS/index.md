---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-05-16" # Date you first upload your project.
# Title of your project (we like creative title)
title: "An introduction to brain decoding and comparing the results of the seven different classifier on Haxby dataset"

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

summary: "Brain decoding is a neuroscience field that concerned about different types of stimuli from information that has already been encoded and represented in the brain by networks of neurons. My goal for this project is learning the fundamentals of brain decoding. Moreover, I compared the performance of seven different common classification approaches including Naive Bayes, Nearest Neighbours, Neural Networks, Logistic Regression, Support vector machine, Decision tree and finally the Artificial Neural Network on Haxby dataset."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "FlowerBouquet.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

# Intro to brain decoding and classification on Haxby dataset using seven different common approaches

<div align="center">
<img src="Brain_decoding.jpg" width="825" height="452" allowfullscreen> 
</div>

## Project definition

### Background
I have B.S in computer software engineering and currently I am a Master’s student in computer science at Université de Montréal (Jan. 2020). Since I am still in the early steps of my master’s project, my main goal is to learn as much as possible and making use of several tools that we have learned during BHS training courses.
<div align="center">
<img src="logo.png" width="700" height="100"> 
</div>


### Brain_decoding overview
Brain decoding or mind-reading using neuroimaging data has been an active topic for years. A part of this project focused on brain decoding using visual stimuli. In the human brain, the functional architecture of the object vision pathway can be investigated using fMRI. It can be done by considering the patterns of response in the ventral temporal cortex while subjects are looking at the different objects. Several studies indicate that the brain responses to the vision of each category of objects are widely distributed and overlapping. Therefore, a distinct pattern of response exists for each stimulus category in the ventral temporal cortex.

### Project
For BHS project, I ran and compared the results of six common classifiers ("Naive Bayes", "Nearest Neighbours", "Neural Networks", "Logistic Regression", "Support vector machine" and "Decision trees" classifiers) on Haxby dataset. During the classification stage, I was trying to find the best results for each approach by playing with parameters. As an example, for Neural Networks classifier, my accuracy result increased significantly when I changed some parameters (it is indicated in the Classifiers.ipynb). 
This change of accuracy made me curious about training ANN on Haxby dataset to examine its performance and learn better about this method (that wasn't a plan at the beginning). Moreover, to make the notebook reproducible and easy to follow for those who don't have a background of machine learning (similar to me before Brainhack school!), I have added a clear description for each cell and a quick overview of each classifier's theory.


### Tools
* Git/Github
* Nilearn & sklearn
* Python visualization, statistics & machine learning libraries (e.g. NumPy, Seaborn, scikit-learn, Matlplotlib, nibabel, graphviz, and pydotplus)
* Compute Canada/Calcul Québec
* Binder
* Terminal and Shell commands

### Data
For this project I used [Haxby et al.(2001)](http://data.pymvpa.org/datasets/haxby2001/) which is a high-quality block-design fMRI dataset from a study on face & object representation in the human ventral temporal cortex (This cortex is involved in the high-level visual processing of complex stimuli). The dataset consists of 6 subjects with 12 runs per subject. In this experiment during each run, the subjects passively viewed greyscale images of 8 object categories, grouped in 24s blocks separated by rest periods. Each image was shown for 500ms and was followed by a 1500ms inter-stimulus interval.

### Progress overview

**Week 1:** During BHS training week I was trying to use the new concepts that we learned, by practicing and following different tutorials. I started using Git & Github.

**Week 2:** In the second week, I created the README file, made slides and became prepare for the project draft presentation. Moreover, I started to play with brain decoding scripts, mostly by following Nilearn and sklearn tutorials. I explored how they work by experimenting and personalizing them.

**Week 3:** From the third week, I started to create my main jupyter notebook called [Classifiers.ipynb](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Classifiers.ipynb) to try six different classification methods on Haxby dataset and compare the results. For me, this approach was challenging not only because of writing scripts but also for understanding the classifiers algorithms and work follows. Since I am new in this field and have never had a machine learning course before, I had to read several references to figure out these approaches, their strengths, and their weaknesses. It gave me the opportunity to learn about several ML models and to get a much better understanding of the reasons that some classifiers return better results on certain datasets compared to the rest.

**Week 4 & 5:** During these weeks, I executed some performance metrics such as "Classification Accuracy”, "Cross-Validation" and “Confusion Matrix” in order to check my different ML model results. I added a quick review for each classifier algorithm to make my notebook reproducible and easy to understand for everyone even those without ML background.  

Additionally, I uploaded and ran one of my scripts on Compute Canada.

After finishing all the mentioned tasks, I decided to take advantage of the remaining time of the 5th week by training a multi-layer network. As was mentioned above, I chose the ANN model. This notebook can be found as [ANN_onHaxby.ipynb](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/ANN_onHaxby.ipynb). Similar to the previous notebook I added a quick review about the ANN algorithm and some explanation for all the cells in order to make it easy to follow.

*I have written down all my progressions in detail, divided per week, in my BHS repository [README](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/README.md) file under "TO-DO LIST " section.*

### Results
As depicted in the following image the support vector machine classification has the best performance comparing to the other mentioned classifiers, while the decision tree returned the worst accuracy, which is understandable considering the classifiers algorithms and the nature of the data.

<div align="center">
<img src="Classifiers_graphs.png" width="1242" height="310"> 
</div>


&nbsp;

The following figure demonstrates the six classifiers confusion matrices. 
<div align="center">
<img src="6classifiers_cm.png" width="990" height="543"> 
</div>

&nbsp;

Here, we see the ANN confusion matrix and the accuracy results. The accuracy is increased from each epoch to the next one that demonstrates how during this supervised phase, the network is taught what is the desired output. 

<div align="center">
<img src="ANN_cm_acc.png" width="850" height="290"> 
</div>

&nbsp;

However, some methods seem to work better than others, It shouldn’t be forgotten that the size and type of data play an important role in the results of different models. As an example, generally multi-layer networks have better results on big datasets. In this case, the results are desirable considering the small size of the input data.

&nbsp;

## Tools I learned during this project
Besides all the tools said earlier, I touched TensorFlow as well!

## Conclusion
Along with many open science tools that I have learned and used during this course; BHS was a great introduction to machine learning. I trained several machine learning classification methods to learn and compare their performance on the Haxby dataset that helped to strengthen my skills in Python and using ML/DL models.
 
In the beginning, I explored brain decoding scripts by following tones of tutorials (mostly from Nilearn and sklearn). In the next step, I created a notebook to improve my coding skills and ML knowledge by evaluating the performance of seven different classifiers. I used plotly for making interactable graphs to demonstrate the results.
In the end, I tried my first ever multi-layer algorithm which was an artificial neural network.
Additionally, the focus on reproducible science taught me how to make a deliverable project based on an open-science concept.

## Deliverables

* [Jupyter Notebook with code for comparing different classifiers](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Classifiers.ipynb)
* [Jupyter Notebook with code for Artificial Neural Network model training](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/ANN_onHaxby.ipynb)
* [Jupyter Notebook with code for introduction to brain decoding](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/BHS_Haxby_BrainDecoding.ipynb)
[Jupyter Notebook with code to produce plots of my results](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/Data-visualization.ipynb) (week three deliverable)
* [Batch script used on Compute Canada to run BHS_Haxby_BrainDecoding.py script](https://github.com/brainhack-school2020/BHS_project_SRastegarnia/blob/master/BHS_Batch.sh)
* [Github repository including project description with all mentioned Jupyter Notebooks clearly commented](https://github.com/brainhack-school2020/BHS_project_SRastegarnia) (Please use Binder to see all the results!)
* [First](https://drive.google.com/open?id=1ABaOXwWPks8xB28OlkiwDvqx7D0B2htQ) and [Final](https://drive.google.com/file/d/1qFHRrdjRLgfP-5dDYNs12vHyDhFCYVp6/view?usp=sharing) presentation slides
* The final report summarizing the entire project and my progression. 


## Future directions
My goals post brain hack school would be increasing my knowledge of machine learning and deep learning by training more complicated models including GCN on new datasets! Also, I hope to try more tools for neuroimaging analysis and preprocessing data.

## Aknowledgments
During BHS, I learned a lot of new tools and so many skills that I will definitely use in the future. I would like to thank all the BHS organizers, instructors, and TAs for sharing their knowledge and putting together this amazing course. Special thanks to Pierre Bellec and my clinic instructors Désirée, Valerie, and Jacob for helping me out with different aspects of my project.
Thanks for giving me this opportunity!

## References

1. Distributed and Overlapping Representations of Faces and Objects in Ventral Temporal Cortex, Haxby et al. 2001
2. https://machinelearningmastery.com/exploding-gradients-in-neural-networks/
3. https://medium.com/data-science-group-iitr/loss-functions-and-optimization-algorithms-demystified-bb92daff331c
4. https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484
5. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
6. https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
7. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
8. https://scikit-learn.org/stable/modules/svm.html
9. https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
10. https://towardsdatascience.com/introduction-to-artificial-neural-networks-ann-1aea15775ef9
11. https://towardsdatascience.com/building-your-own-artificial-neural-network-from-scratch-on-churn-modeling-dataset-using-keras-in-690782f7d051
12. https://nilearn.github.io/auto_examples
13. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
14. https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd
15. https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier
16. https://github.com/ncarlson01/chat_ML
17. https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html?highlight=kneighbors#sklearn.neighbors.KNeighborsClassifier
18. https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

