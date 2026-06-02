---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to data visualization in Python"

# Your project GitHub repository URL
github_repo: https://github.com/school-brainhack/module_python_visualization

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [visualization, python, matplotlib, seaborn, plotly]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "In this module, we will introduce the basics of plotting in python with some of most commonly used packages such as matplotlib and seaborn."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "plotting.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 3h.

The prerequisites to take this module are:
 * [Installations](/modules/installation)
 * [Introduction to python for data analysis](/modules/python_data_analysis) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access 
to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources

This module is built around one Jupyter notebook and one set of exercises, all available in the [module repository](https://github.com/school-brainhack/module_python_visualization).

## Original lecture
This module was first presented by Jacob Vogel during the QLSC 612 course in 2020, and the associated notebook is available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/14-may/01-data-visualization/python_visualization_for_data.ipynb). (Note: if you did the BIDS module, the dataset to download is the same - ds000228! A few functions now throw warnings, you can ignore these, or fix them if you like.)

The video of the presentation is available below (1h09):
<iframe width="560" height="315" src="https://www.youtube.com/embed/lJyFWTT7sCY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exercise

In the exercise notebook (`exercise_visu_en.ipynb`), you will have to create static and interactive visualization to explore the phenotypic and fMRI data from the **ADHD200** dataset available through nilearn.

The exercise is structured as follows:
1. **Part 1 : Exploring phenotypic data**: you will visualize some clinical and demographic variables of the ADHD200 dataset.
2. **Part 2 : Exploring fMRI data**: you will explore the functional fMRI data from the ADHD200 dataset through visualizations.

**Important**: follow the parameter specifications given in each question exactly — the exercise uses automated grading that compares results to reference values.

Follow up with your local TA(s) to validate you completed the exercises correctly.

## More resources

- Other great resources to get started with plotting in python:
   -  [dartbrains](https://dartbrains.org/Introduction_to_Plotting/)
   -  [neurohackademy](https://github.com/neurohackademy/visualization-in-python/blob/master/visualization-in-python.ipynb)
   -  [PythonDataScienceHandbook](https://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb)
   -  [matplolib tutorial - rougier](https://github.com/rougier/matplotlib-tutorial)

- Interactive plotting:
   - [Interactive plots and the spectrum of data visualization](https://www.youtube.com/watch?v=FwM_6oZo_2g&t=1s)
   - [Plotly](https://plotly.com/python/)
   - [Bokeh](https://docs.bokeh.org/en/latest/index.html)
   - [Altair](https://altair-viz.github.io/)
   
- Gallery:
   - [seaborn gallery](https://seaborn.pydata.org/examples/index.html)
   - [Python Graph Gallery](https://python-graph-gallery.com/)
