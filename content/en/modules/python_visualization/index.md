---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to data visualization in Python"

# Your project GitHub repository URL
github_repo:

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
This module was presented by Jacob Vogel during the QLSC 612 course in 2020, and the associated notebook is available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/14-may/01-data-visualization/python_visualization_for_data.ipynb). (Note: if you did the BIDS module, the dataset to download is the same - ds000228! A few functions now throw warnings, you can ignore these, or fix them if you like.)

The video of the presentation is available below (1h09):
<iframe width="560" height="315" src="https://www.youtube.com/embed/lJyFWTT7sCY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Tutorial

 * Download the jupyter notebook (save raw version from Github), or start a new jupyter notebook 
 * Watch the video and  run the cells in the notebook

## Exercice

For this next part, we will refer to the following [notebook](https://github.com/brainhackorg/school/blob/master/content/en/modules/python_visualization/python_visualization_intro_rmv_answ.ipynb).

For example purposes, we will make use of a phenotypic dataset from the ABIDE II consortium. This amazing international multi-site dataset contains data from individuals diagnosed with Autism Spectrum Disorder (ASD) and healthy controls. We will use a version of the phenotypic  [data](http://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html) from a single site (Kennedy Krieger Institute). To download the dataset, click on the link and then 'Kennedy Krieger Institute' on the right-hand side. Then, Downloads -> Phenotypic File. You will need an NITRC account - if you don't have one, you can create one in a few minutes [here](https://www.nitrc.org/account/register.php).

1. **Read through the notebook running all the cells**
2. **Complete the exercises in the notebook**

**Exercise 1** Create a figure with a single axes and replot the second scatterplot to group by sex instead of dx_group.

       Set the figure size to a ratio of 8 (wide) x 5 (height)
       Use the colors red and gray
       Set the opacity of the points to 0.5
       Label the axes
       Add a legend
     
**Exercise 2** Using a pairwise plot, compare the distributions of age, viq, and piq with respect to dx_group.

        Set a palette
        Set style to ticks
        Set context to paper
        Suppress the dx_group variable from being on the plot
        
**Exercise 3** Using a violin plot separate out viq as a function of sex and dx_group.

        Different dx_group should be on each half of each violin
        The x-axis should reflect the different sex categories.

**Exercise 4** Play around and make an interactive plot using plotly and your project data if you have any.

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

- Other great resources to get started with plotting in python:
   -  [dartbrains](https://dartbrains.org/content/Introduction_to_Plotting.html)
   -  [neurohackademy](https://github.com/neurohackademy/visualization-in-python/blob/master/visualization-in-python.ipynb)
   -  [PythonDataScienceHandbook](https://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb)
   -  [matplolib tutorial - rougier](https://github.com/rougier/matplotlib-tutorial)

<iframe width="560" height="315" src="https://www.youtube.com/embed/FwM_6oZo_2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Interactive plotting 
   - [Plotly](https://plotly.com/python/)
   - [Bokeh](https://docs.bokeh.org/en/latest/index.html)
   - [Altair](https://altair-viz.github.io/)
   
- Gallery
   - [seaborn gallery](https://seaborn.pydata.org/examples/index.html)
