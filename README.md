<a href="https://github.com/moqroq">
   <img src="https://avatars.githubusercontent.com/u/122383501?s=400&u=05796ff256ac58bd02476c922fdfc54ccf7f7ca4&v=4" width="100px;" alt=""/>
   <br /><sub><b>Roqa Moqa</b></sub>
</a> 



# Project Definition

## About Me

Hi, I am Roqa, from UdeM hub, PhD student at University de Montreal in biomedical sciences. Throughout my master's program, I specialized in medical imaging, which provided me with knowledge of diagnostic and imaging techniques utilized in the field. However, for my PhD, I need to familiarize myself with the state-of-the-art data science packages.

## Project Summary

My project aims to elucidate and compare the distinct functional connectivity patterns between individuals with Parkinson's disease and neuropsychiatric symptoms (PD+NPS) and those without the condition, using resting-state fMRI connectivity matrices.

### Specific Objectives Include:

- Characterizing the functional connectivity alterations in individuals with PD+NPS by examining the connectivity matrix derived from resting-state fMRI data.
- Identifying and mapping disrupted functional brain networks associated with PD+NPS and investigating their potential relevance to motor and neuropsychiatric symptomatology.
- Comparing the functional connectivity patterns between individuals with PD+NPS and healthy controls to delineate the specific network alterations unique to the PD+NPS population.

### Personal Objectives

- Familiarize myself with state-of-the-art data science packages and tools for neuroimaging analysis.
- Develop expertise in interpreting and visualizing resting-state fMRI connectivity data.
- Understand advanced visualization techniques for neuroimaging data.

## Abstract

This project aims to explore and compare the functional connectivity patterns in individuals with Parkinson's disease (PD) and neuropsychiatric symptoms (NPS) to those without the condition, utilizing resting-state functional magnetic resonance imaging (rs-fMRI) connectivity matrices. By examining the connectivity matrix derived from rs-fMRI data, we aim to identify potential alterations in functional brain networks associated with both PD and NPS, shedding light on the relationship between these conditions. The findings from this study may contribute to a better understanding of the underlying neural mechanisms and inform future research and clinical interventions.

## Result

## BIDS Validation in Raw Neuroimaging Dataset

The BIDS Validator is a tool that verifies if neuroimaging datasets adhere to the BIDS standard, promoting organized and correctly formatted data for enhanced data sharing and reproducibility in neuroimaging research. In the case of the "mp1014" subject dataset, it identified 2 errors and 1 warning in 62 files. I utilized the error log for subjectmp1014 and subsequently ran fmriprep for the dataset.

![BIDS Validator](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/BIDSvalidator.png)

## Running fMRIPrep with Docker: Preprocessing fMRI Data for Multiple Participants

I executed the following command on my local machine to run fMRIPrep using Docker for 5 subjects:

docker run -ti --rm \
  -v $HOME/subjectmp1014:/data:ro \
  -v $HOME/outputmp1014:/out \
  -v $HOME/freesurfer/license.txt:/opt/freesurfer/license.txt \
  nipreps/fmriprep:latest \
  /data /out \
  participant --participant_label {sub-mp0010,sub-mp0011,sub-mp0012,sub-mp0013,sub-mp0014 --skip-bids-validation

![Brain-mask-fmriprep](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/Brain-mask.png)
![Spatial-normalization-fmriprep](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/Spatial-normalization.png)
![Alignment-functional-anatomical-fmriprep](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/Alignment-functional-anatomical.png) 

## Functional Connectivity Analysis and Group Comparison using Harvard Atlas

This analysis aimed to investigate functional connectivity patterns and group differences using the Harvard atlas. The preprocessed data and confound information were imported from the specified directory. The Harvard atlas was utilized for defining brain regions of interest. The functional connectivity matrix was extracted, and subjects were divided into depressed and non-depressed groups based on BDI scores.
Connectivity matrices were computed for each subject, and mean matrices were calculated for the depressed and non-depressed groups. 
![Connections with Dependencies](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/connectionsdep.png)
![Connections](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/connections.png)

## Data Processing and Grouping based on BDI Scores for Connectivities Analysis

Data processing and grouping based on BDI scores were performed to investigate connectivities. The data consisted of preprocessed functional connectivity data and BDI scores obtained from participants. The functional connectivity matrix was computed, and subjects were categorized into depressed and non-depressed groups based on their BDI scores.
Connectivity matrices were created for each subject, and group-level analyses were conducted. The results demonstrated distinct patterns of connectivity between the depressed and non-depressed groups. These findings highlight the potential differences in brain network organization associated with depression.
Updating and Filtering Correlation matrix for Analysis
![Connectivities](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/connectivities.png) 

## Updating and Filtering Correlation matrix based on label of interest

Updating and filtering the correlation matrix to focus our analysis on specific regions of interest and their associations with neurobehavioral data, improved the accuracy and relevance of the data, allowing us to uncover meaningful insights and generate hypotheses for further investigation.

![Non-Dependencies](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/nonDep.png)
![Dep](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/Dep.png)

## Ploting of Functional Connectivity in Depressed and Non-Depressed Groups

The aim of this analysis was to visualize atlas-based coordinates for depressed and non-depressed groups. Coordinates were obtained using the specified atlas, and separate visualizations were created for each group. The connectivity patterns and spatial distribution of these coordinates were examined.
The visualizations revealed distinct patterns of connectivity and spatial organization in the depressed and non-depressed groups. These findings provide valuable insights into the differences in brain network architecture associated with depression. The visualizations serve as a powerful tool for understanding and interpreting the complex connectivity patterns in different brain states.

![Plot](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/plot.png)
![View](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/view.png)

## Connectivity Distribution by Group: Depressed vs. Non-Depressed

This analysis aimed to explore the distribution of connectivities between depressed and non-depressed groups. The connectivities were obtained from participants belonging to these two groups. A box plot was created to visualize and compare the connectivity distributions.

The results of the T-test revealed a significant difference in connectivities between the depressed and non-depressed groups (T-Statistic: -2.1286, P-Value: 0.0348). This indicates that there are distinct patterns of brain connectivity associated with depression.
These findings suggest that neuroconnectivity analysis could potentially serve as a valuable tool for understanding and identifying markers of depression. 

![Connection by Group](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/conn%20by%20group.png)


## Linear Regression Model for MCI Prediction

This study aimed to predict Mild Cognitive Impairment (MCI) using connectivities and BDI scores. The dataset was split into training and test sets (80% training, 20% test). A linear regression model was created, trained on the training set, and used to predict MCI values for the test set.
The model's performance was evaluated using Mean Squared Error (MSE) and R-squared (R2). The MSE was 0.279, indicating the average squared difference between predicted and actual MCI values. The R2 value was -0.115, suggesting the model did not explain much variance in MCI.
In summary, the linear regression model showed limited success in predicting MCI using connectivities and BDI scores. 

![LM](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/lm.png)

Mixed Effects Linear Regression Model for MCI Prediction:

A mixed effects linear regression model was developed to predict Mild Cognitive Impairment (MCI) using connectivities and BDI scores. The dataset was split into training and test sets (80% training, 20% test). 
After fitting the model, predictions were made on the test set. The evaluation of the model yielded a Mean Squared Error (MSE) of 0.250 and an R-squared (R2) value close to zero. The MSE represents the average squared difference between predicted and actual MCI values, while R2 indicates the proportion of variance in MCI explained by the model.
In summary, the mixed effects linear regression model showed limited success in predicting MCI using connectivities and BDI scores. The convergence warning suggests potential issues with model estimation.

![Mixed](https://github.com/brainhack-school2023/Moqadam_project/raw/main/outputs/mixed.png)

## Tools

- Jupyter notebook for coding and visualization
- Docker container
- fMRIPrep for rs-fMRI preprocessing
- Python Packages: matplotlib, seaborn, nilearn, plotly, Nibabel, scipy, Pandas
- Git and Github for Version Control

## List to do

    Accessing Big Data:
        PPMI - Parkinson's Progression Markers Initiative

    Running fmriprep on NIAGARA

    Learning the Statistical Part of My Project

    Becoming More Familiar with Machine Learning
