---
type: "project" # DON'T TOUCH THIS ! :)
date: "2025-06-18" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Brian Tumor Detection in MRI Using Faster R-CNN"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Yadollah (Amir) Zamanidoost]

# Your project GitHub repository URL
github_repo: https://github.com/Amirzamani4096/Zamanidoost_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/AlexPeng517/BHS2023_Project_SAM_MRI), click `manage topics`.
# Please only lowercase letters
tags: [MRI,Brain Tumor Detection,Faster R-CNN]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project presents a deep learning-based pipeline for detecting brain tumors in MRI scans using a customized Faster R-CNN architecture. Project reports are incorporated in the BHS (https://psy6983.brainhackmtl.org/project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: " "
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->
---

<a href="https://github.com/Amirzamani4096">
   <img src="https://avatars.githubusercontent.com/u/84202242?v=4" width="100px;" alt=""/>
   <br /><sub><b>Yadollah (Amir) Zamanidoost.</b></sub>
</a>

I'm Yadollah (Amir) Zamanidoost, a PhD student in Computer Engineering at Polytechnique Montréal. My research focuses on early-stage lung cancer detection using deep learning techniques on CT scan images. I’m passionate about applying AI in healthcare and excited to expand my skills in neural data science. I joined Brainhack School to learn new tools, collaborate with others, and explore how open science practices can support impactful research.

---
# Brian Tumor Detection in MRI Using Faster R-CNN


## Project definition

The goal of this project is to develop an automated and accurate brain tumor detection system using deep learning techniques. Leveraging the power of Faster R-CNN, the model detects tumors in MRI images by learning spatial features and distinguishing abnormal regions from healthy tissue. This tool is designed to assist radiologists by reducing diagnostic time and minimizing false positives.

### Background
Brain tumors are among the most challenging medical conditions to detect and treat. Accurate identification of tumor regions in MRI scans is crucial for diagnosis, surgical planning, and treatment monitoring. Traditional methods rely heavily on expert interpretation, which can be time-consuming and prone to inter-observer variability. Deep learning approaches, especially object detection frameworks like Faster R-CNN, offer a promising alternative by automating tumor localization and classification. In this project, we enhance the classical Faster R-CNN pipeline with a false positive reduction (FPR) stage to improve robustness and reliability.
![Framework Overview](Images/overall_framework.png)

### Objective

The main objective of this project is to accurately detect brain tumors in MRI scans using the Faster R-CNN object detection framework. By leveraging deep convolutional neural networks, this project aims to enhance early diagnosis and assist medical professionals in identifying tumor regions with high precision.

### Tools

- **Programming Language**: Python 3.x  
- **Deep Learning Framework**: PyTorch  
- **Computer Vision Libraries**: OpenCV, torchvision  
- **Annotation Tool**: LabelImg, Nibabel 
- **Visualization**: Matplotlib, Seaborn  
- **Notebook Environment**: Jupyter Notebook  
- **Hardware**:
  - **Training RPN**: Tesla V100 GPU (via terminal-based access)
  - **Inference and Evaluation**: CPU
- **CUDA**: Used during RPN training for GPU acceleration  

### Data

This project uses publicly available datasets containing 2D T1-weighted contrast-enhanced MRI images of brain tumors along with their ground-truth labels. The data is sufficient in both quantity and quality to allow for effective training and fine-tuning of object detection models such as Faster R-CNN.

1. [Brain Tumor Segmentation @ Kaggle](https://www.kaggle.com/datasets/nikhilroxtomar/brain-tumor-segmentation)  
   - **Original Source & Credit**: [Figshare](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427)  
   - **Description**: This dataset contains 3064 T1-weighted contrast-enhanced brain MRI images in `.png` format, with manually labeled tumor regions provided via ground-truth masks.  
   - **Use Case**: Used for training and fine-tuning the Faster R-CNN model.

All images were preprocessed and annotated for object detection tasks by converting segmentation masks into bounding box labels.

### Deliverables

At the end of this project, the following materials will be available:

-  A completed and well-documented `README.md`.
-  Several Jupyter Notebooks.
     - For training the RPN and FPR models using GPU acceleration (Tesla V100).
     - For inference, post-processing, and evaluation (executed on CPU).
- Performance metrics including precision, recall, F1-score, and FROC curves.
- The slide presentation introducing the problem, dataset, model architecture, and key findings.

## Results

### Progress Overview

The Faster R-CNN model demonstrates strong localization capability in detecting brain tumors from MRI scans, even with limited annotated data for training. Our custom RPN training and false positive reduction significantly improved precision without sacrificing recall.

### Tools I Learned During This Project

Throughout this project, I gained hands-on experience with several essential tools and libraries in deep learning and medical image analysis, including:

- **PyTorch** – for building and training the Faster R-CNN and custom RPN models

- **Torchvision** – for using pretrained VGG16 and manipulating datasets

- **OpenCV** – for image processing and visualization tasks

- **Matplotlib & Seaborn** – for plotting training metrics and visual results

- **scikit-learn** – for computing classification metrics like precision, recall, and F1-score

- **Git & GitHub** – for version control and project collaboration

- **Markdown** – for documenting the project and creating a structured README

- **Jupyter Notebooks** – for training, evaluation, and presenting visual results step-by-step

### Results

#### Deliverable 1: Introduction Slides
 You can find the introduction slides of this project [here](Slides/Zamanidoost_final_Presentation.pdf)

#### Deliverable 2: Jupyter Notebooks
You can find jupyter notebooks of this project at my [github repository](https://github.com/Amirzamani4096/Zamanidoost_project)

#### Deliverable 3: Instructions
   
1. **Install Required Libraries**  
   Before running the notebooks, install all required libraries [`requirements.txt`](requirements.txt)

2. **Data Acquisition & Tumor Size Analysis**  
   Refer to [`Data_Acquisition.ipynb`](Data/Data_Acquisition.ipynb) for organizing the datasets and analyzing tumor size.

3. **Preparing Data for Training and Testing**  
   Use [`Create_Input_Data.ipynb`](Data/Create_Input_Data.ipynb) to generate structured datasets for the RPN model.

4. **Region Proposal Network (RPN) - Training**  
   Train the RPN model using [`RPN_Training_Model.ipynb`](RPN_model/RPN_Training_Model.ipynb), which extracts candidate regions.

5. **RPN Inference and Evaluation**  
   Use [`RPN_Test_Results.ipynb`](Results/RPN_Test_Results.ipynb) to evaluate the performance of the RPN model.

6. **FPR Dataset Creation**  
   Generate patches for false positive reduction training using [`patches.ipynb`](FPR_model/patches.ipynb).

7. **False Positive Reduction (FPR) Model - Training**  
   Train the FPR classification model using [`FPR_Training_model.ipynb`](FPR_model/FPR_Training_model.ipynb) to refine RPN outputs.

8. **Final Inference and Results**  
   Run [`RPN_FPR_Test_Results.ipynb`](Results/RPN_FPR_Test_Results.ipynb) to obtain and visualize the final tumor detection results after combining RPN and FPR outputs.

#### Deliverable 4: Results

The proposed two-stage detection framework—based on Faster R-CNN with a False Positive Reduction (FPR) module—demonstrates improved performance in detecting brain tumors from 2D MRI slices. As illustrated in the sample detection images, the FPR model significantly reduces incorrect predictions while preserving true tumor regions.
![Results1](Results/Result1.png)
![Results2](Results/Results2.png)
![Results3](Results/Results3.png)

## Conclusion and acknowledgement

This project presents a two-stage deep learning pipeline for accurate brain tumor detection in MRI images, combining the Faster R-CNN architecture with a False Positive Reduction (FPR) model. Through fine-tuning and evaluation on open-access datasets, the system achieves promising detection performance, with enhanced precision and reduced false positives.

Many thanks to the BrainHack School Professor ([Dr. Eva Alonso Ortiz](https://neuro.polymtl.ca/team/faculty/eva-alonso-ortiz.html)), TA (Sebastian Rios), instructors, and fellow participants for their support, feedback, and inspiration throughout this project.

