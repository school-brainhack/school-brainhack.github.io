---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-05-20" # Date you first upload your project.
# Deep Electrode Mapper: Using Deep Learning to Localize EEG Electrodes' Coordinates

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Joel P. Diaz-Fong, Lucas Vidal Murakami, Aijia Ivy Zhong]

# Your project GitHub repository URL
github_repo: https://github.com/JOEwithanL/DeepElectrodeMapper

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [electrode localization, deep learning, clustering, preprocessing tools]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects.

summary: "Accurate source localization in EEG requires electrode's coordinates. However, currently this process requires skill and experience in dealing with different methods and softwares, which can be expensive, laborious and time consuming (Tveter et al., 2024). The Deep Electrode Mapper’s objective is to solve the electrodes’ localization issue by implementing deep learning to segment the electrodes from multiple image formats and find their coordinates via clustering. Currently the project is still in progress, and its development will be shared via its repository. 

References:

Tveter, M., Tveitstøl, T., Nygaard, T., Kulashekhar, S., Bruña, R., Hammer, H. L., Hatlestad-Hall, C., & Haraldsen, I. R. H. (2024). EEG electrodes and where to find them: automated localization from 3D scans. Journal of Neural Engineering, 21(5), 056022."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

When using EEG for clinical or research analysis of brain activity the problem of associating a recording to a specific brain region (i.e., source localization) needs to be addressed for meaningful analysis. Although dependent on some variables, knowing the coordinates of the electrodes (i.e., where the signal is being recorded) precisely and accurately is central for source localization (Hirth et al., 2020). However, currently getting electrodes' coordinates are either time-consuming, requiring manual labeling of each electrode, or using specilzed software that are expensive to use (Tveter et al., 2024), adding to the skills and experience required in either method. In addition, there are multiple file formats that can be used for extracting the electrodes' coordinates, for example, MRI volumes (Pinte et al., 2021), 3D scans and photogrammetry (Hirth et al., 2020). Therefore, having a a pipeline that is less labour intensive and expensive, while accounting for the multiple set-ups and file formats would be an ideal improvement in the process of electrodes' localization.
There has been development in improving the electrodes' localization process, for example pipeline using phones as portable scanners, algorithms that predict other electrode coordinates based on a smaller subset for multiple channels' setups (Hirth et al., 2020), and even the usage of deep learning to localize the coordinates from MRI scans (Pinte et al., 2021). 
In light of such developments, this project aimed to use deep learning to perform localization of electrodes, while accounting that the pipeline is generalizable for different file formats and set-ups, so it can be used inspite of the methodology used.

References:

Everitt, A., Richards, H., Song, Y., Smith, J., Kobylarz, E., Lukovits, T., Halter, R., & Murphy, E. (2023). EEG electrode localization with 3D iPhone scanning using point-cloud electrode selection (PC-ES). Journal of Neural Engineering, 20(6), 066033.

Hirth, L. N., Stanley, C. J., Damiano, D. L., & Bulea, T. C. (2020). Algorithmic localization of high-density EEG electrode positions using motion capture. Journal of neuroscience methods, 346, 108919. https://doi.org/10.1016/j.jneumeth.2020.108919.

Pinte, C., Fleury, M., & Maurel, P. (2021). Deep learning-based localization of EEG electrodes within MRI acquisitions. Frontiers in Neurology, 12, 644278.

Tveter, M., Tveitstøl, T., Nygaard, T., Kulashekhar, S., Bruña, R., Hammer, H. L., Hatlestad-Hall, C., & Haraldsen, I. R. H. (2024). EEG electrodes and where to find them: automated localization from 3D scans. Journal of Neural Engineering, 21(5), 056022."

<iframe width="560" height="315" src="https://www.youtube.com/embed/PTYs_JFKsHI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Tools

The Deep Electrode Mapper project will rely on the following technologies:
 * GitHub, to share our progress as a group and for other possible users.
 * VS Code and Jupyter Notebook for coding the various steps to develop the project.
     * Created tools for aliging electrodes and their labels to head scan.  
     * Open3D library - Convert surface and volume data into 3D point cloud format (.ply and .npz).
     * h5py package - Transform unlabeled and labeled 3D Point Cloud into HDF5
     * PointNet++ - Train deep learning model on electrode localization and segementation and test on the data set.
     * K-Means Clustering Algorithm - Find centroids and its coordinates.

### Data

Our data comprises of 144 3D scanned head models acquired with a portable 3D scanner (.obj files), of which 39 have T2-weighted MRI scans while participants wore the EEG cap (.nii). Our data is from the study Alpha oscillations and working memory deficits in ADHD: A multimodal imaging investigation (R01MH116268) - https://nda.nih.gov/edit_collection.html?id=3101.

### Deliverables

At the end of this project, we will have:
 - GitHub repository with our tools and code.
 - Documentation on how to train and test on different datasets.

## Results

### Progress overview

Currently we worked on the preparation of the data to train the PointNet++, preparing the PointNet++ for training, and developing the clustering for the extraction of the centroids coordinates for when the PointNet++ output will be ready. A subset of the dataset had the electrodes manually labelled so we could have labelled and unlablled data for training and testing the deep learning model. This allowed the creation of two tools for aligning the electrodes to a head model. For the data to be compatible to the deep learning model we transformed data into PointCloud and then HDF5 format both containing labels or not (the script accepts multiple file formats for generalizability). Lastly, we developed a python script to perform clustering of the PointCloud data to extract the centroids and their coordintes, which should be once we have the segmented electrodes from the deep learning model, the coordinates of the electrodes. For next steps we aim to train and test the deep learning model. Moreover, due to limited amount of data set we are still pondering the possibility of increasing the training dataset with synthetic data.

### Tools I learned during this project

* **GitHub** We learned how to use GitHub to share the code and scripts that each of us were working on.
* **Jupyter Notebook** Learned how to code using Jupyter Notebook, to have a more modular, step by step structure of coding, which was quite helpful in separating the different functions. Moreover, it was useful to debug when there was a problem, as it was easier to identify where the issue was occuring.
* **VSCode** Throughout the coding for the project using VSCode was very helpful in, as it contained multiple functionalities in one place, beuing able to use the terminal, and code in different files, as well as being able to directly install any necessary packages.

### Results

#### Deliverable 1: GitHub repository

Although the project is still in progress, which signifies that the GitHub repository does not yet have all the final version of the scripts or the trained model, we were able to add some tools for aligning the electrode lables with the 3D scan, as well as some of the scripts for preparing the data for training the deep learning model, and for the clustering of the segmented data after the deep learning output model for achiebing the electrode coordinates.

#### Deliverable 2: Documentation

As the deep learning model was not yet trained or tested, we did not yet wrote the documentation, but we will do once the project advances.

## Conclusion and acknowledgement

To conclude, it would be a relevant step in the clinical and research application of EEG to have a generalizable and accessible tool for localizing the electrodes' coordinates. Although implementing a solution with deep learning is promising, it comes with certain limitations, for example the requirements of having a large dataset for training, and specific set-up to use it. Nevertheless it presents the possibility of having a generalizable solution for different file contents and EEG caps. Therefore, we will still continue to attempt to develop the project and assess the viability of the solution.
We would like to thank the study Alpha oscillations and working memory deficits in ADHD: A multimodal imaging investigation (R01MH116268) for providing and allowing us to use the data for our project. Moreover, we would like to thank the BrainHack School for giving us the space, time, and support to pursue and collaborate on this project.
