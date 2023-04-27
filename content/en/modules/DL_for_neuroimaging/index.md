---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Applications of deep learning in neuroimaging"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fmri, deep leatning, neuroimaging, nobrainer]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "How deep learning can be used in neuroimaging analyses? A hands-on example using the nobrainer library and Montreal AI-Neuroscience workshop material."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "DL_for_neuroimaging.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 2h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to python for data analysis](/modules/python_data_analysis) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources
This module will be using the [MAIN educational workshop on brain encoding and decoding](https://main-educational.github.io/brain_encoding_decoding/intro.html).

## Exercise
Let's have a look at application on functional data with the [MAIN educational workshop on brain encoding and decoding](https://main-educational.github.io/brain_encoding_decoding/intro.html). We will look at the **decoding** modules. This part is independent from the video above.
 * Please follow the [introduction](https://main-educational.github.io/brain_encoding_decoding/intro.html#), set-up your environment and clone the material from GitHub. Please provide your answers in jupyter notebooks.
 * Throughout this tutorial you will be using the Haxby data set. Please read through and understand how to access it [here](https://main-educational.github.io/brain_encoding_decoding/haxby_data.html) and go through the [original support-vector machine analysis](https://main-educational.github.io/brain_encoding_decoding/svm_decoding.html) of the study and complete the exercises. 
 * After understanding the workflow of functional data, please go through the [Multi-Layer Perceptron](https://main-educational.github.io/brain_encoding_decoding/mlp_decoding.html) and complete the relevant exercise. If you want a challenge, please feel free to do the harder questions, or do both lessons :tada:.

 * (Optional) You can learn about the [Graph Convolution Network](https://main-educational.github.io/brain_encoding_decoding/gcn_decoding.html) and how to work with timeseries data!

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

This demo was presented by [Jakub Kaczmarzyk](https://twitter.com/jakubkaczmarzyk) during the QLSC 612 course in 2020, the slides are available [here](https://raw.githubusercontent.com/neurodatascience/course-materials-2020/master/lectures/15-may/02-applications-of-deep-learning/nobrainer-brainhackmtl-2020.pdf).

The video of the presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/XM1FT_oVDP0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can find more information about the nobrainer library on its [github repo](https://github.com/neuronets/nobrainer).

[A nature communications article](https://www.nature.com/articles/s41467-020-20655-6) on the superiority of deep learning over standard machine learning in neuromimaging tasks.

[A Neuroscience and Biobehavioral Reviews article](https://www.sciencedirect.com/science/article/pii/S0149763416305176) on deep learnging applications in neuroimaging studies of brain-based disorders. It has a good overview of the general framework of deep learning applications, and descriptions of the main kinds of architectures.

[An overview article](https://pubmed.ncbi.nlm.nih.gov/35722548/) on the challenges associated with applying deep learning models to neuroimaging applications, especially fMRI data. Three new methods are presented which could potentially help incorporate these models into clinical practice.

[MAIN educational workshop on brain encoding and decoding](https://main-educational.github.io/brain_encoding_decoding/intro.html) covers deep learning application to analyse a classic neuroimaging dataset. The tutorial also incorporates useful features from the `nilearn` library to process your neuroimaging data, as well as doing decoding analysis.
