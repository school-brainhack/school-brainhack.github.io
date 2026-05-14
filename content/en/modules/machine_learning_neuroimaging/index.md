---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Machine learning for neuroimaging"

# Your project GitHub repository URL
github_repo: https://github.com/school-brainhack/module_machine_learning_neuroimaging

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website: https://school-brainhack.github.io/module_machine_learning_neuroimaging

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI, machine learning, neuroimaging, nilearn]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Application of machine learning to fMRI data analysis using nilearn. This module covers extracting functional connectivity features, building and evaluating predictive models with scikit-learn, and interpreting results in a neuroimaging context. Hands-on exercises apply these methods to ADHD classification."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "functional_connectome.png"
---

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * [installation](https://school-brainhack.github.io/modules/installation/) module
 * [introduction to python for data analysis](https://school.brainhackmtl.org/modules/python_data_analysis/) module
 * [introduction to machine learning](https://school.brainhackmtl.org/modules/machine_learning_basics/) module

Recommended but not mandatory:
 * [fmri connectivity](/modules/fmri_connectivity) module
 * [fmri parcellation](/modules/fmri_parcellation) module

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

Follow up with your local TA(s) to validate you completed the exercises correctly.

## Resources

This module is built around two Jupyter notebooks and one set of exercises, all available in the [module repository](https://github.com/school-brainhack/module_machine_learning_neuroimaging) and rendered as a [web book](https://school-brainhack.github.io/module_machine_learning_neuroimaging/):

### Tutorial 1: Functional connectivity with nilearn

An introduction to extracting functional connectivity features from resting-state fMRI data using nilearn. Topics covered:
- A brief introduction to fMRI and the challenge of feature extraction
- Computing time series from brain atlases with `NiftiLabelsMasker`
- Constructing and visualizing connectomes with `ConnectivityMeasure`

### Tutorial 2: Machine learning with nilearn

A complete ML pipeline applied to a developmental fMRI dataset (children vs. adults classification). Topics covered:
- Loading and exploring phenotypic data
- Extracting connectivity features across subjects
- Training a linear SVM classifier with scikit-learn
- Evaluating model performance with cross-validation
- Visualizing and interpreting results

The dataset used is the **NeuroDev** developmental fMRI dataset, preprocessed and packaged by **Elizabeth Dupre** and now integrated as one of nilearn's main tutorial datasets.

### Original lecture

This module builds on a lecture originally delivered by **Jacob Vogel** during the QLSC 612 course in 2020. The original video (2h13) is available below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/2wj9OJjEDy0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exercise

The exercise notebook (`exercises_adhd.ipynb`) has you build a complete ML pipeline to predict **ADHD diagnosis** from functional connectivity data, using the [ADHD200 dataset](https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_adhd.html) available through nilearn.

The exercise is structured as follows:

1. **Part 1 — Exploring phenotypic data**: examine clinical and demographic variables (number of subjects, ADHD diagnosis distribution, age, gender).
2. **Part 2 — Extracting functional connectivity features**: use an atlas-based masker to extract time series and compute a connectivity matrix per subject.
3. **Part 3 — Training and evaluating an SVM classifier**: split data, fit a linear SVM, and assess performance with accuracy, a classification report, and a confusion matrix.
4. **Challenge — Cross-validation**: re-evaluate using stratified k-fold cross-validation for a more robust performance estimate.

**Important**: follow the parameter specifications given in each question exactly — the exercise uses automated grading that compares results to reference values.

Follow up with your local TA(s) to validate you completed the exercises correctly.

## More resources

- [nilearn documentation](https://nilearn.github.io/stable/)
- [scikit-learn documentation](https://scikit-learn.org/stable/)
- [ADHD200 dataset on nilearn](https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_adhd.html)
- [NeuroDev / development fMRI dataset on nilearn](https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_development_fmri.html)
