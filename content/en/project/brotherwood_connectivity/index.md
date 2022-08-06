---
type: "project" # DON'T TOUCH THIS ! :)
date: "2022-08-06" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Classifying Neuropsychiatric Disorder Diagnoses Using Resting State BOLD fMRI Connectivity Data"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Peter Brotherwood]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2022/brotherwood_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [Machine-Learning, Connectivity, Diagnosis, Workflow]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Can functional connectivity data be used as a predictor for neuropsychiatric diagnosis? This project explores the usefulness of connectivity data in predicting ADHD, Bipolar Disorder, and Schizophrenia diagnoses using machine learning classification methods."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "connectivity_image.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## About Me

<a href="https://github.com/PeteBro">
   <img src="https://avatars.githubusercontent.com/u/64285401?v=4?s=100" width="100px;" alt=""/>
   <br /><sub><b>Peter Brotherwood</b></sub>
</a>

I am a first year PhD student at the University of Montreal studying in computational neuroscience. I come from a fairly different background, with a BSc in Genetics and an MSci in Bioinformatics from the University of Birmingham. Much of my current work is in perception, using machine learning based approaches to model representational spaces in individual subjects. My hope is that BHS will introduce me to tools and best prectices I need to learn in order to fully integrate into the field of computational cognitive neuroscience.
## Project Summary

### Introduction
Brain regions with correlated temporal activity are seen to form functional networks of varying scale and distribution. Regions correlated at rest form resting state networks. Aberrant functional connectivity of resting state networks has been observed in multiple populations sufering from neuropsychiatric disorders; including ADHD (Sudre *et al*., 2017), Bipolar Disorder (Syan *et al*., 2018), and Schizophrenia (Sheffield & Barch, 2016). Given these observed differences in resting state network connectivity, this project aims to apply machine learning methods to investigate if aberrations in resting state functional connectvitiy can be used to identify neuropsychiatric diagnoses.

### Main Objectives
- Provide a full neuroimaging workflow from preprocessing of raw data to visualisation of results.
- Emphasize reproducibility, making all elements of the project as reproducible as possible.
- Investigate ability of machine learning algorithms in predicting phenotype based on connectivity data.

### Personal Objectives
- Learn more about open data and project reproducibility.
- Gain an understanding of fMRI and neuroimaging database structures and best practices.
- Develop skills in proprocessing and analysis of fMRI data.
- Apply knowledge of machine learning to neuroscientfic studies.

### Tools
- Compute Canada for Job Submission
- Git and Github for Version Control
- DataLad for Reproducibility
- Singularity for Reproducibility
- fMRIPrep for data preprocessing
- Python Packages: `matplotlib`, `seaborn`, `scikit-learn`, `nilearn`

### Data
The dataset used in this study comes from the UCLA Consortium for Neuropsychiatric Phenomics LA5c Study (Poldrack *et al*., 2016). The dataset is comprised of fMRI data for 122 healthy individuals, and 142 individuals with neuropsychiatric disorders. Of these 139 individuals, 50 are diagnosed with schizophrenia, 49 with bipolar disorder, and 40 with ADHD. The dataset contains fMRI data collected at rest and over a series of attentional tasks. The fMRI data is in nifti format and the dataset is provided in BIDS format. More information on this dataset can be found at https://openneuro.org/datasets/ds000030/versions/1.0.0.

A summary of the dataset is as follows:

|              |Participants|Male|Female|Average Age|Age Std|
|:-------------|:----------:|:--:|:----:|:---------:|:-----:|
|Control       |122         |65  |57    |32.05      |10.28  |
|Schizophrenia |50          |38  |21    |35.29      |8.94   |
|Bipolar       |49          |28  |19    |31.59      |8.77   |
|ADHD          |40          |21  |12    |36.46      |8.79   |
|Total         |261         |152 |109   |33.29      |9.29   |

<p align="center">
<img src="population.png">
</p>

### Project Deliverables
- Reproducible project workflow, detailed in git repo and via datalad logs, reproducible via containers.
- Executable Python scripts for data preparation and machine learning
- Markdown file introducing the project and detailing project results

## Results

### Preprocessing using `fMRIprep`

Preprocessing of raw fMRI data was done using `fMRIprep` (Esteban *et al*., 2018) and executed via the `preprocessing.sh` script on Alliance Canada's Beluga HPC Cluster. Due to lack of resting state data for some subjects, 260 preprocessed resting state BOLD fMRI and their associated confound files were returned. fMRIprep was run using singularity 3.8 with the following steps:

- Brain masking and tissue segementation of T1w image
- Spatial normalization of the anatomical T1w reference
- Surface reconstruction using FreeSurfer
- Alignment of functional and anatomical MRI data
- Brain masking and confound extraction

### Getting Connectivity Data using `nilearn`

Brain masking and connectivity data retrieval was done using `nilearn` (Abraham *et al*., 2014). The BASC multiscale deterministic atlas (Bellec *et al*., 2009) with 64 regions of interest (ROIs) was used to mask the preprocessed voxel-wise BOLD activity data, in order to reduce the complexity of the features. A plot of this atlas can be seen below:


<p align="center">
<img src="atlas.png">
</p>


Confounds detected by `fMRIprep` were loaded using `nilearn`'s `load_confounds_strategy` method and regressed out during masking. Following this, connectivity matrices showing correlations in BOLD timeseries activity between ROIs were generated for each subject. The impact of confound removal strategy on the output connectivity matrices can be seen below:


<p align="center">
<img src="confounds.png">
</p>


The upper triangular vector (UTV) of each subject's connectivity matrix forms a set of features which will serve as input to the machine learning step. The UTVs of all matrices can be combined to form a feature matrix:


<p align="center">
<img src="connectivity.png">
</p>


### Machine Learning using `scikit-learn`

Phenotype was learned and predicted using a support vector classifier with a linear kernel from `scikit-learn` (Pedregrosa *et al*., 2011). 30% of individuals were used as unseen test data, and a grid search with 5-fold cross validation was performed on the remaining 70% of subjects to find the optimum value for the the `C` regularizer. This process was done once with the full dataset, and once with a stratified dataset, as seen below:


<p align="center">
<img src="stratification.png">
</p>

Using each model to predict the unseen test data, the folllowing multi-label confusion matrices were obtained:


<p align="center">
<img src="conf_matrices.png">
</p>


With the corresponding classification summaries:


**All Subjects**

Accuracy: 0.456

|              |Control| ADHD |Bipolar Disorder|Schizophrenia|Macro Average|Weighted Average|
|:-------------|:-----:|:----:|:--------------:|:-----------:|:-----------:|:--------------:|
|Precision     |0.528  |0.0   |0.083           |0.583        |0.299        |0.374           |
|Recall        |0.757  |0.0   |0.067           |0.467        |0.323        |0.456           |
|F1 Score      |0.622  |0.0   |0.074           |0.519        |0.304        |0.404           |
|Support       |37     |12    |15              |15           |             |                |


**Stratified Subjects**

Accuracy: 0.316

|              |Control| ADHD |Bipolar Disorder|Schizophrenia|Macro Average|Weighted Average|
|:-------------|:-----:|:----:|:--------------:|:-----------:|:-----------:|:--------------:|
|Precision     |0.384  |0.176 |0.294           |0.500        |0.338        |0.347           |
|Recall        |0.333  |0.250 |0.333           |0.333        |0.313        |0.316           |
|F1 Score      |0.357  |0.207 |0.313           |0.400        |0.319        |0.325           |
|Support       |15     |12    |15              |15           |             |                |


Following this, SVC coefficients were extracted to identify those features which had the most extreme weights when predicting phenotype:

**Control vs Schizophrenia**


<p align="center">
<img src="cont_schz_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/Control_vs_Schizophrenia_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Control_vs_Schizophrenia_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Control_vs_Schizophrenia_feature_connectome_interactive.html) for an interactive connectome.

**Control vs ADHD**


<p align="center">
<img src="cont_adhd_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Control_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Control_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Control_feature_connectome_interactive.html) for an interactive connectome.

**Control vs Bipolar Disorder**


<p align="center">
<img src="cont_bipo_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Control_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Control_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Control_feature_connectome_interactive.html) for an interactive connectome.

**Schizophrenia vs ADHD**


<p align="center">
<img src="schz_adhd_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Schizophrenia_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Schizophrenia_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Schizophrenia_feature_connectome_interactive.html) for an interactive connectome.

**Schizophrenia vs Bipolar Disorder**


<p align="center">
<img src="schz_bipo_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Schizophrenia_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Schizophrenia_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/Bipolar_vs_Schizophrenia_feature_connectome_interactive.html) for an interactive connectome.

**ADHD vs Bipolar Disorder**


<p align="center">
<img src="adhd_bipo_coefs.png">
</p>

Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Bipolar_image_interactive.html) for an interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Bipolar_3D_interactive.html) for a 3D interactive map.
Click [here](https://brainhack-school2022.github.io/brotherwood_project/ADHD_vs_Bipolar_feature_connectome_interactive.html) for an interactive connectome.

## Conclusions

### Can we predict diagnosis from fMRI data?
While in this instance, the model was unable to accurately classify neuropsychiatric diagnoses based on resting state fMRI connectivity data, various factors should be considered when answering such a question. Factors such as the nature and composition of the data, the features selected for model fitting, choice of mask and confounding strategy, choice of model, and choice of performance metric should all be considered when implementing such a pipeline as this.

### Objectives, Tools, and Deliverables
In terms of objectives to achieve, tools to learn, and deliverables to produce I believe the project was a success. The output is a comprehensive pipeline from raw data to visualization of results, utilising all of the tools I had aimed to learn. The deliverables are fulfilled, with a comprehensive walkthrough of the project, and reproducible python scripts for replicable use. While complete containerization of the environment using Singularity was not possible, the following reproducibility guide serves as an adequate substitute for this.

## Guide to Reproducibility
All scripts used in the analyses are located in the `scripts` directory of the [git repo](https://github.com/brainhack-school2022/brotherwood_project) and are executable in the Linux command line. Each script is written such that it can be executed using fMRI data from alternative functional tasks from the same dataset, or with similar datasets conforming to BIDS formatting standards. The `requirements.txt` file provides all neccesary dependencies for execution of scripts following preprocessing using fMRIprep.

A basic example of running the contents of the `scripts` directory on a Linux machine is as follows:

### Running fMRIprep

To run `mriprep.sh` it is highly recommended to use a HPC cluster, more instructions on preprocessing requirements and how to properly format `mriprep.sh` can be found at https://www.nipreps.org/apps/singularity/.

Following correct installation and formatting, preprocessing can be run by running `$ sbatch mriprep.sh`

### Setting up a virtual environment for running the python scripts
```
$ cd <path_to_cloned_repo> # go to project directory

$ python3 -m venv <venv_name> # initialize virtual environment

$ source <path_to_venv>/bin/activate # enter the virtual environment

(<venv_name>) $ pip install --upgrade pip # upgrade the package manager

(<venv_name>) $ pip install -r requirements.txt # install project dependencies
```

*What follows is a basic usage tutorial on `.py` scripts in the `scripts` directory; for more information on each script and its associated parameters use:* `scripts/<script_name>.py -h`

### Getting connectivity data
```
$ source <path_to_venv>/bin/activate # enter the virtual environment

(<venv_name>) $ scripts/format_data.py <path_to_derivatives_file> <preprocessed_bold_file_suffixes> # create an index file in the derivatives folder for use with other python scripts

(<venv_name>) $ scripts/get_connectivity_data.py <path_to_derivatives_file> <path_to_atlas> # get individual subject connectomes
```

### Fitting a Support Vector Classifier
```
$ source <path_to_venv>/bin/activate # enter the virtual environment

(<venv_name>) $ scripts/fit_svm.py <path_to_derivatives_file> # perform a parameter search and find the best fitting model
```

### Troubleshooting
In the instance that attempting to run a script returns `permission denied`, it may be neccesary to run `(<venv_name>) $ chmod +x scripts/<script_name>.py`. Alternatively running `(<venv_name>) $ python3 scripts/<script_name>.py <args>` will execute the scripts.

## Acknowledgements
I would like to thank the Brainhack team of 2022 for their continued support throughout the course. With particular thanks to Hao-Ting Wang and Natasha Clarke for providing their support and expertise throughout the project.

## References
Abraham, A., Pedregosa, F., Eickenberg, M., Gervais, P., Mueller, A., Kossaifi, J., Gramfort, A., Thirion, B. and Varoquaux, G., 2014. Machine learning for neuroimaging with scikit-learn. *Frontiers in Neuroinformatics*, 8.

Bellec, P., Rosa-Neto, P., Benali, H. and Evans, A., 2009. Multi-level bootstrap analysis of stable clusters (BASC) in resting-state fMRI. *NeuroImage*, 47, p.S123.

Esteban, O., Markiewicz, C., Blair, R., Moodie, C., Isik, A., Erramuzpe, A., Kent, J., Goncalves, M., DuPre, E., Snyder, M., Oya, H., Ghosh, S., Wright, J., Durnez, J., Poldrack, R. and Gorgolewski, K., 2018. fMRIPrep: a robust preprocessing pipeline for functional MRI. *Nature Methods*, 16(1), pp.111-116.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V. and Vanderplas, J., 2011. Scikit-learn: Machine learning in Python. *The Journal of machine Learning research*, 12, pp.2825-2830.

Poldrack, R., Congdon, E., Triplett, W., Gorgolewski, K., Karlsgodt, K., Mumford, J., Sabb, F., Freimer, N., London, E., Cannon, T. and Bilder, R., 2016. A phenome-wide examination of neural and cognitive function. *Scientific Data*, 3(1).

Sheffield, J. and Barch, D., 2016. Cognition and resting-state functional connectivity in schizophrenia. *Neuroscience; Biobehavioral Reviews*, 61, pp.108-120.

Sudre, G., Szekely, E., Sharp, W., Kasparek, S. and Shaw, P., 2017. Multimodal mapping of the brain’s functional connectivity and the adult outcome of attention deficit hyperactivity disorder. *Proceedings of the National Academy of Sciences*, 114(44), pp.11787-11792.

Syan, S., Smith, M., Frey, B., Remtulla, R., Kapczinski, F., Hall, G. and Minuzzi, L., 2018. Resting-state functional connectivity in individuals with bipolar disorder during clinical remission: a systematic review. *Journal of Psychiatry and Neuroscience*, 43(5), pp.298-316.
