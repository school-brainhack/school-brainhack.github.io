---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-11" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Grasp-And-Lift-EEG-Detection"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Rong-Xuan, Ye]

# Your project GitHub repository URL
github_repo: https://github.com/xuanxuan27/Grasp-And-Lift-EEG-Detection

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [EEG, BCI, machine learning, signal preprocessing]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "I try to use methods that I learn from Brainhack School or other classes to classify the human motion phase of grasp and lift objects. In the end, I got over 90% accuracy but I found some problems with it. All the predicted output are zeros, so it got the accuracy because most of the data got the output “zero”. That’s why I can got over 90% accuracy."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
Motor imagery is a crucial application method of brain-computer interfaces. The relationship between hand motion and EEG signals is significant.

### Tools
Those method I try in this project includes “Random Forest”, “Wavelet Transform”, “PCA”, “ICA”, “CNN”.
I combined these methods and try to get desired output. However, the result was not satisfied. 

### Data
The dataset is from Kaggle:
https://www.kaggle.com/competitions/grasp-and-lift-eeg-detection/data

There are 12 subjects in total, 10 series of trials for each subject, and approximately 30 trials within each series.
And the data is labeled with 6 phases of hand motion:
-	HandStart
-	FirstDigitTouch
-	BothStartLoadPhas
-	LiftOff
-	Eplace
-	BothReleased

### Deliverables

At the end of this project, we will have:
 - The current markdown document, completed and revised.
 - A gallery of the student projects at Brainhack 2020.
 - Instructions on the website about how to submit a pull request to the [brainhack school website](https://github.com/PSY6983-2021) in order to add the project description to the website.

## Results
### Progress overview

The project was swiftly initiated by P Bellec, based on the existing template created in 2019 by Tristan Glatard and improved by different students. It was really not that hard. Community feedback is expected to lead to rapid further improvements of this first version.

### Tools I learned during this project
-	MNE python: This is my first time implementing MNE python to process the data. I converted a csv file to BID format, made epochs and did ICA. I try to remove some component that I thought it may be eye movement component, however, I cannot determine if there is any different. I think the signal still looked the same.
-	ICA and PCA: I have heard these analysis methods before and I knew their function. During this project, I spent time to realize how they work, and the mathematics meaning behind them.
-	Random Forest: Actually, I have try random forest in other project before, I think it is a powerful method to classify data.
-	Wavelet transform and CNN: This is my first time using the wavelet and CNN model to classify data. For me, it’s an important experience because it made me know how to build the framework, why the wavelet transform is needed, and know how it works.

### Results
In the end, I got over 90% accuracy but I found some problems with it. All the predicted output are zeros, so it got the accuracy because most of the data got the output “zero”. That’s why I can got over 90% accuracy.

Although I don’t get the desired result, I think I learn a lot from this project. And I will keep trying to complete this challenge.

#### Deliverable 1: report template

You are currently reading the report template! I will let you judge whether it is useful or not. If you think there is something that could be improved, please do not hesitate to open an issue [here]( https://github.com/xuanxuan27/Grasp-And-Lift-EEG-Detection/issues) and let us know.

#### Deliverable 2: project gallery

You can check out the [2020 BrainHack School project gallery](https://psy6983.brainhackmtl.org/project/)


