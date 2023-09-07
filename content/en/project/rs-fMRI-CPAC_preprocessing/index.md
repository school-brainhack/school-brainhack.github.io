# BrainHack School 2023
Predict individual emotional changes in competitive tasks by using rs-fMRI connectivity data 

## Summary
This project aims to use resting-state fMRI connectivity matrices to predict individual mood changes across multiple contexts.

**Keywords:** *python*, *rs-fMRI*, *BIDS*, *C-PAC*, *connectivity*, *machine-learning*

## About me  
Hi, I'm Tsu-chun Yang (or you can call me Jim), from Taiwan hub, Postgraduate student at  National Taiwan University.

## Project definition

### Main Objectives:
- To provide a full neuroimaging workflow from preprocessing of raw data to visualization of results.
- To utilize the resting state of individuals to predict their reactions in various situations involving interpersonal interactions.
- To establish a predict model by machine learning method.

### Personal Objectives:
- Understand the structure of raw data and BIDS files, and learn how to converse raw datas to BIDS files.
- Learn the expertise to visualize resting-state fMRI connectivity data.
- Practical use the machine learning methods taught in class to build a classification model.

### Abstract  
The aim of this project is to investigate whether resting-state functional magnetic resonance imaging (rs-fMRI) data could be used to infer the mental state of subjects when faced with a competitive task with punishment. We manipulated win-lose conditions and punishments to induce different psychological states in participants, such as worry, envy, happiness, or luck. By using machine learning algorithms to identify specific patterns of brain activity associated with different mental states. This will allow us to develop a predictive model that can infer an individual's psychological state responses to different outcomes from their rs-fMRI data.

### Background
to be supplemented...

### Tools & Packages
- Vscode & Python - for coding and visualization
- Bash & Docker container - for rs-fMRI preprocessing 
- Packages: 
  - HeuDiConv
  - C-PAC
  - os
  - matplotlib
  - seaborn
  - nilearn
  - plotly
  - Nibabel
  - scipy
  - Pandas

### Data
- Full dataset: 46 subjects, include T1- and T2-weighted structural images, task-based and resting state fMRI images.
- Main dataset: 30 subjects, rs-MRI before performing a competitive task.
- Obtained from: [Pain and Somatosensory Laboratory](https://paingibms.weebly.com/), the Institute of Brain and Mind Sciences, National Taiwan University. 
- Status: Unpublished

### Deliverables
- A GitHub repository: containing all the elements of the project.
- A markdown file: for the project description.
- A HeuDiConv related file: to customize the name, format and location of of the IMA converted BIDS file.
- Some cpac output file: to demonstrate the functionality of cpac


## Result
The following contains the steps and results

### Converse IMA file to BIDS file with Docker in bash 
- More detail in [BIDS Tutorial Series: HeuDiConv Walkthrough](https://reproducibility.stanford.edu/bids-tutorial-series-part-2a/)
- The output file is in [HeuDiConv_related_file](https://github.com/r11454008/BHSTW_project/tree/main/HeuDiConv_related_file)

### BIDS-Validation
The BIDS Validator is a utility designed to validate whether neuroimaging datasets conform to the BIDS standard. In the case of the "p004" subject dataset, there is no error or warning, how lucky that is.  : )
  
![BIDS Validatation](https://github.com/r11454008/BHSTW_project/assets/130885549/27a2b4a3-b7c7-489f-89cf-b0749a833767)

### C-PAC
cpac is a powerful package dedicated to rs-fMRI data that can be used by both novices and experts. It not only can preprocessing rsMRI BIDS files, but also also perform some analysis on it own, such as:
- VMHC (Voxel-Mirrored Homotopic Connectivity)  
- ReHo (Regional Homogeneity)
- Network Centrality
- ALFF (Amplitude of Low Frequency Fluctuations) 
- SCA（Seed-based Correlation Analysis）
  
![CPAC Expected Output](https://github.com/r11454008/BHSTW_project/assets/130885549/08c44014-7459-4c8b-b7bb-7d7cbcd04874)

### Execute C-PAC
I executed the following command on my local machine to run cpac using Docker for 1 subject:
``` bash
PS C:\Users\USER> bash  
(base) tcyang@MSI:/mnt/c/Users/USER/Desktop/Brainhack/Brainhack_final$ my_path=$(pwd)
(base) tcyang@MSI:/mnt/c/Users/USER/Desktop/Brainhack/Brainhack_final$ cd /mnt/c/Users/USER/  
(base) tcyang@MSI:/mnt/c/Users/USER$ cpac run $my_path/Nifti $my_path/Nifti_output participant  
```
![CPAC execute](https://github.com/r11454008/BHSTW_project/assets/130885549/b3e54cdd-07fd-4060-99f6-4acb705daa75)  
  
Here are some output files from C-pac:
- [Dataset information](https://github.com/r11454008/BHSTW_project/files/11715797/cpac_individual_timing_cpac-default-pipeline.csv)
- [Expected Outputs list](https://github.com/r11454008/BHSTW_project/files/11715803/sub-004_ses-1_expectedOutputs.txt)
- The matrix of the preceding analysis (see [sub004/func](https://github.com/r11454008/BHSTW_project/tree/main/p004_output/output/cpac_cpac-default-pipeline/sub-004_ses-1/func))

### Python: Visualization of the data.
My functional connectivity matrix is derived from the matrix generated by cpac with seed-based correlation analysis (SCA). Unfortunately, because the version of CPAC changed, I couldn't find the default seed file of SCA, so I couldn't continue with the next steps. Currently I'm still looking for where the file is located.
![SCA Matrix](https://github.com/r11454008/BHSTW_project/assets/130885549/4166e897-ef91-4cfb-b51d-4c42f086342e)

> 2023.06.12 update!  
  According to the developer's reply, the current ROI file cannot be output with the analysis results.   
  It is necessary to wait for the next update.   
  So now I'm my planning to re-execute the c-pac by using an earlier version.

## List to do 
~□ Find the Region of interest (ROI) file~  
□ Re-execute C-PAC with different version  
□ Do the machine learning
