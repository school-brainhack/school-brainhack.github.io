---
type: "project" # DON'T TOUCH THIS ! :)
date: "2022-08-03" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Can we classify men and women based on the connectivity profile of their language network?"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Xanthy Lajoie]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2022/Lajoie_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [sex differences, language network, classification, resting-state]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Sex differences in the language network is a long lasting and unresolved debate in the neuroscience field. Clinical studies have shown that pathologies or developmental conditions affecting language functions can differently affect individuals based on their sex. Although the language network is bilaterally organized, the left hemisphere is dominant for language in most individuals. However, this lateralisation tends to vary between sexes.In the present project, we address the research question on whether young adults present differences in the pattern of rs-fMRI functional connectivity within the language network based on their sex. To address this issue, we propose to determine whether we can classify healthy young adults, men and women, based on their rs-fMRI functional connectivity profiles within the language network."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "brain.png"
---
# rs-fmri sex classification 

## Project Description

#### Background 
Sex differences in the language network is a long lasting and unresolved debate in the neuroscience field. Clinical studies have shown that pathologies or developmental conditions affecting language functions can differently affect individuals based on their sex (Cahill, 2006; Icer et al., 2020).

Although the language network is bilaterally organized, the left hemisphere is dominant for language in most individuals (Knect et al., 2000). However, this lateralisation tends to vary between sexes (Shaywitz et al., 1995). 

![image](https://user-images.githubusercontent.com/90349544/182665738-d16a1d47-5bb9-4498-aa71-eed6896e738d.png)


Differences between men and women in the functional language network could explain sex differences in clinical conditions and offer insight for the development of interventions based on individuals’ characteristics. Yet whether and how sex impacts the functional language network organization is still largely unknown.

#### Objectives
In the present project, we address the research question on whether young adult individuals present differences in the pattern of rs-fMRI functional connectivity within the language network based on their sex. To address this issue, we propose to determine whether we can classify healthy young adult men and women, based on their rs-fMRI functional connectivity profiles within the language network. 
#### Data
The rs-fMRI images were issued from the human connectome project (HCP) S1200 release datatbase (Van Essen et al., 2012). The rs-fMRI images of a total of 667 healthy adults (322 men and 345 women, age: 22-35 years) were included in the study. First, for each participant, we extracted the functional connectivity networks anchored in the core regions of the language network from rs-fMRI data. This step is completed. 

With the knowledge acquired from this class, I will test whether machine learning models can accurately classify men and women based on their functional connectivity language maps within the language network. Subsequently, I will determine which are the most discriminant functional connectivity features that allow this classification.

### My objectives 
- Familiarize myself with different softwares such as Git, Github, WSL
- Learn how to code with python, specifically for the neuroimaging field
- Have a better understanding of machine learning and its application in neuroimaging
- Get comfortable using the terminal to search for files and not the default file system on our laptops

### Deliverables 
-  Seed-to-voxel code 
-  Jupyter notebook containing Linear SVC model and accuracy 
-  Presentation slides
-  Project Report

## Results 
Using the seed-to-voxel correlations of 8 seeds of a sub-sample of 70 participants (40 M, 38 W).
Model pipeline: 

![image](https://user-images.githubusercontent.com/90349544/181608461-c8786fae-ab75-4604-a479-ab12e8fff9c7.png)

1. Results from the PCA determining the best number of features to include in our model. 
   In this case, 0 features represent the best number of features (basically using the whole brain)

![image](https://user-images.githubusercontent.com/90349544/181355670-ace0976a-4cae-40c4-a38d-f82f1b58c3fe.png)


2. Results from the Linear SVC classifier 

![image](https://user-images.githubusercontent.com/90349544/181356687-20731893-0c5a-48e5-9a9f-d460faf0657d.png)

Accuracy (r2) = 0.875

Interpretation: the classifier was able to sucessfully classify men and women with an accuracy of 87.5% 

### Tools Learned During This Project   
Open Science Software: I learned to use Git for local and remote control in order to share my project repository on Github. I was also able to navigate through different repositories to find the documentation needed for my project. I no longer send codes to myself via email or rely on my USB drive. 

Machine Learning Packages: I have a better understanding of how to use scikit-learn, nilearn and their different modules for machine learning and neuroimaging data manipulations.

Python Scripting: I was able to use different libraries (e.g. numpy, nibabel), code in a virtual environment with Jupyter Notebook. The course modules helped me understand data dimensionality and how to manipulate it.

Data Visualization: I learned to plot multiple static figures with matplotlib and seaborn and to generate interactive figures with plotly and also to plot connectomes.

![image](https://user-images.githubusercontent.com/90349544/181617392-92fb89ec-d210-4aab-a4d2-07f026ca2248.png)

## Conclusion

Apart from the main project, participating in Brainhack 2022 has had several benefits. I am more comfortable with shell coding, and the introduction to WSL makes it easier for me to work in Linux environments. I'm looking forward to trying more tools for neuroimaging analysis, such as fMRIprep for preprocessing, machine learning methods to try different classifiers and seed-to-voxel connectivity analyses. Although I've only had a brief introduction to many of these tools, I feel like they are more accessible with the knowledge Brainhack school has given me.


### Acknowledgements
I am immensely grateful to the entire team for all of their assistance and support throughout the course. François, Marie-Ève et Claudéric, thank you for your patience and for not sighing when I asked for help every 5 minutes. Without you, I don't know what I would've done. 
