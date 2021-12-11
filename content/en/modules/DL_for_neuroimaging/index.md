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

summary: "How deep learning can be used in neuroimaging analyses ? A hands-on example using the nobrainer library."

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

Contact François Paugam if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by [Jakub Kaczmarzyk](https://twitter.com/jakubkaczmarzyk) during the QLSC 612 course in 2020, the slides are available [here](https://raw.githubusercontent.com/neurodatascience/course-materials-2020/master/lectures/15-may/02-applications-of-deep-learning/nobrainer-brainhackmtl-2020.pdf).

The video of the presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/XM1FT_oVDP0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * Follow along the video running the notebook presented in the hands-on part. This notebook can be run [from google colab](https://colab.research.google.com/github/neurodatascience/course-materials-2020/blob/master/lectures/15-may/02-applications-of-deep-learning/mtl_deep_learning_jakubkaczmarzyk.ipynb) (if you have a google account) which is recommended since it lets you have access to a GPU. Otherwise you can also run it remotely [on binder](https://mybinder.org/v2/gh/neurodatascience/course-materials-2020/master?filepath=lectures%2F15-may%2F02-applications-of-deep-learning%2Fmtl_deep_learning_jakubkaczmarzyk.ipynb) (but with no GPU). If you prefer to run it locally, you can download the .ipynb file :
 ```
 wget https://raw.githubusercontent.com/neurodatascience/course-materials-2020/master/lectures/15-may/02-applications-of-deep-learning/mtl_deep_learning_jakubkaczmarzyk.ipynb
 ```
 * Follow up with François Paugam to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

You can find more information about the nobrainer library on its [github repo](https://github.com/neuronets/nobrainer).

[A nature communications article](https://www.nature.com/articles/s41467-020-20655-6) on the superiority of deep learning over standard machine learning in neuromimaging tasks.

[A Neuroscience and Biobehavioral Reviews article](https://www.sciencedirect.com/science/article/pii/S0149763416305176) on deep learnging applications in neuroimaging studies of brain-based disorders. It has a good overview of the general framework of deep learning applications, and descriptions of the main kinds of architectures.
