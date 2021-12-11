---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Machine learning for neuroimaging"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fMRI, machine learning, neuroimaging]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Application of machine learning to fMRI data analysis. In this module, we will go over extracting features (X) and target (y), fitting the model to the data with cross-validation and tweaking our models."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "regr_image.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * installations
 * [introduction to python for data analysis](https://psy6983.brainhackmtl.org/modules/python_data_analysis/) module.
 * [introduction to machine learning ](https://psy6983.brainhackmtl.org/modules/machine_learning_basics/) module

Recommanded but not mandatory : 
 * [fmri connectivity ](https://psy6983.brainhackmtl.org/modules/fmri_connectivity/) module
 * [fmri parcellation ](https://psy6983.brainhackmtl.org/modules/fmri_parcellation/) module

Contact Andréanne Proulx if you have questions on this module, or if you want to check that you completed successfully all the exercises.


## Resources
This module was presented by Jacob Vogel during the QLSC 612 course in 2020, the slides are available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/14-may/03-intro-to-machine-learning/ML_Regression_Tutorial.ipynb).

The video of the presentation is available below (2h13):
<iframe width="560" height="315" src="https://www.youtube.com/embed/2wj9OJjEDy0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

If you need to resfresh some machine learning concepts before this tutorial, you can find the link to the slides from the introduction to machine learning here: https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/14-may/03-intro-to-machine-learning/IntroML_BrainHackSchool.pdf


## Exercise

 * 1. Download the jupyter notebook (save raw version), or start a new jupyter notebook 
 * 2. Watch the video and test the code yourself

Using the same dataset 
 * Tweak the pipeline in the tutorial, by applying PCA , keeping 90% of the variance, instead of SelectPercentile to reduce the dimensionality of features (feature selection). Refer to scikit-learn documentation. https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

  
        model = Pipeline([
        ('feature_selection',SelectPercentile(f_regression,percentile=20)),
        ('prediction', l_svr)
                      ])


 * Implement cross-validation, but this time changing to leave-one-out. Here is to give an idea as to where changes need to be made in the code.

        # First we create 10 splits of the data
        skf = KFold(n_splits=10, shuffle=True, random_state=123)

 * What are the features we are using in this model? What are the numbers representing the shape of the time series (168, 64), the shape of the connectivity matrix (64 x 64), and of the feature matrix (155, 2016)?
      
 * Using the performance of the different polynomial fit (MSE) for train and test error, try to explain why increasing complexity of models does not necessarily lead to a better model. 
 
 * Remember we talked about regularization in the introduction to machine learning? Variance of model estimation increases when there are more features than samples. This especially relevant when we have > 2000 features ! Apply a penalty to the SVR model. Refer to the documentation https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html. 
 
 * Follow up with Andréanne Proulx to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

- Dataset used : https://openneuro.org/datasets/ds000228/versions/1.0.0
- scikit-learn documentation (https://scikit-learn.org/stable/)
- Python Data Science Handbook's chapter on machine learning by Jake VanderPlas is an excellent resource, althought not openly available online

