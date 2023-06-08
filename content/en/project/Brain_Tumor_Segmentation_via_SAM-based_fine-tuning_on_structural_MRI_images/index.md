---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-8" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Brain Tumor Segmentation via SAM-based fine-tuning  on structural MRI images"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Li-Xuan Alex Peng]

# Your project GitHub repository URL
github_repo: https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI), click `manage topics`.
# Please only lowercase letters
tags: [mri,segmentation,brain_tumor,foundation_model]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project is to learn how to perform brain tumor segmentation using fine-tuning on foundation models, I followed tutorials provided by [MedSAM](https://github.com/bowang-lab/MedSAM) and perform fine-tuning on open datasets."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "qualitative_results.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Of the most recent research in computer vision, Meta has released a foundation model i.e. [Segments Anything Model (SAM)](https://segment-anything.com/), capable of segmenting arbitrary semantics on any image.
Researchers from the University of Toronto later fine-tune the SAM model on medical images [(MedSAM)](https://arxiv.org/pdf/2304.12306.pdf) and reach a significant improvement on such tasks compared to the original SAM.


### Tools

Computation Resource and Running Environment:
  * Packages:  CUDA, Numpy, Nilearn, Pytorch,  SAM, MedSAM, Seaborn
  * Environment: Custom built JupyterLab server running on NV-Docker based container
  * Hardware: Nvidia Tesla A100 x2 (For training), Nvidia GTX 1080Ti  (For inference)


### Data

The two datasets below that I found in open-access data all provided 2D MRI images with corresponding ground-truth masks.
Empirically, their quantities and qualities are adequate for fine-tuning.
1. [Brain Tumor Segmentation@kaggle](https://www.kaggle.com/datasets/nikhilroxtomar/brain-tumor-segmentation) (Original Source and Credit: [Jun Cheng](https://github.com/chengjun583/brainTumorRetrieval) (For fine-tuning)
This brain tumor dataset containing 3064 T1-weighted contrast-enhanced images (.jpg)
from 233 patients with three kinds of brain tumor: meningioma (708 slices), 
glioma (1426 slices), and pituitary tumor (930 slices).
2. [BRaTS 2021 Task 1 Dataset@RSNA-ASNR-MICCAI BraTS Challenge 2021](https://www.synapse.org/#!Synapse:syn25829067/wiki/610863) (For evaluation)
Consist of 1666 scans with T1, T2, and T2-FLAIR MRI images, delivered as NIfTI files (.nii.gz) and their corresponding ground-truth masks. For detailed explanations please refer to BraTS challenge home page.


### Deliverables

At the end of this project, we will have:
 - The current markdown document, completed and revised.
 - Two Jupyter notebooks, one for fine-tuning and the other for inference and evaluation. All are adopted from [MedSAM](https://github.com/bowang-lab/MedSAM) with my own minor modifications.  Available on my [BHS github repository](https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI).
 - The fine-tuned model checkpoint (.pth) also provided via this [google drive folder](https://drive.google.com/drive/folders/1MbHo0qBfkQYARUhB-DAhbD5a4lhmYNqs?usp=sharing)
 - The introduction slides of this project.

## Results

### Progress overview

The SAM foundation model shows an amazing generalization ability to adapt downstream tasks even though the fine-tuning dataset is relatively small in scale.

### Tools I learned during this project

 * **Docker**: Building JupyterLab running environment using Docker container
 * **MRI**: Understand the basic concept of MRI imaging
 * **Nilearn**: Pre-process MRI image using Nilearn package
 * **Foundation Model**: Understand how foundation model works and perform domain specific adaptation on custom dataset
 * **Result Visualization**: Visualize the result in quantitative and qualitative perspectives


### Results

#### Deliverable 1: Introduction Slides

You can find the introduction slides of this project [here](https://docs.google.com/presentation/d/1SeMZCID98rrUaRF6O2B1kKdpq92b1gFhh22336PCRQY/edit?usp=sharing)

#### Deliverable 2: Jupyter Notebooks

You can find jupyter notebooks of this project at my [github repository](https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI)


#### Deliverable 3: Instructions

1. For fine-tuning on your own datasets, please follow the tutorial provided by [MedSAM](https://github.com/bowang-lab/MedSAM)
2. For reproducing my training results, please follow this [jupyter notebook](https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI/blob/main/Demo_BraTS.ipynb)

If you have any questions or suggestions, feel free to contact me via email <alexpeng517@gmail.com>

## Conclusion and acknowledgement

Thanks to [BoWang Team from University of Toronto](https://github.com/bowang-lab) for open sourcing their recent research, so I can learn how to fine-tune the model from their work.

Thanks to SNMG of Dept. CSIE, National Central University, for providing powerful computation resources to make this project practical.

Thanks to Professor Kevin Chun-Hsien Hsu, Institute of Cognitive Neuroscience, National Central University, giving me the oppotunity to attend BrainHackSchool 2023.

Thanks to all the Professors, Moderators, TAs and Classmates that make this BrainHackSchool happend!

