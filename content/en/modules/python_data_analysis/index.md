---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to Python for data analysis"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [Python, data analysis]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This tutorial aims at introducing students to the programming language Python for data analysis. By the end of this module, students will be familiar with Python basic syntax and understand why Python serves well the purpose of data analysis."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "python.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:

* You should already have everything installed for this module!
* We will be using Jupyter Notebook which is a web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access 
to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Before starting:

1. Open the terminal
2. Type jupyter notebook
3. If you're not automatically directed to a webpage copy the URL printed in the terminal and paste it in your browser
4. Once on the webpage, click "New" in the top-right corner and select "Python 3"
5. You have Jupyter notebook 

The little box you see once in the notebook is called a "cell." You can enter (multi-line) code by typing in the cell, and then run the code by pressing "Shift+Enter."
To create a new cell, press the "+" button on lefthand side of the toolbar at the top of the screen!

You are ready for this tutorial and you are strongly encouraged to type along the presentation!

## Resources
This module was presented by [Ross Markello](https://rossmarkello.com/) during the QLSC 612 course in 2020.

All the tutorial notes related to the video below are available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/12-may/01-python-for-data-analysis/python-for-data-analysis.ipynb). 

<iframe width="560" height="315" src="https://www.youtube.com/embed/NcDcoiNMauc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercises
For this part, we will use the famous scikit-learn dataset iris which consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) with information about petal and sepal length and width stored in a 150x4 numpy.ndarray.

1. Before starting to write some code, you want to set-up the environment so that it load the required modules. In a Jupyter Notebook import the following libraries:
       
       # imports 
       import pandas as pd
       import numpy as np
       import matplotlib.pyplot as plt
       from sklearn.datasets import load_iris
       %matplotlib inline

       
2. Load the iris dataset

       iris = load_iris()

       
3. Explore the dataset using .keys()
4. Print the shape and type of 'data'
5. Store 'data' and 'features_names' in distinct variables
6. Create a pandas dataframe with 'data' and use 'feature_names' for column names
7. Get the summary statistics for this dataframe using .describe()
8. Subset the dataframe to keep only the first 50 rows 
9. Try to answer this question using the entire dataframe : Are there any extreme sepal length values? 
     * Reminder : extreme value are > 3.9 standard deviation. (value - mean) / std. For this one, you might need to use a for loop.
10. What about other features of the flowers? Try automating the previous operation by writing a function name find_extreme_values()
11. Read about the boxplot function in matplotlib to get familiar with python documentation. What does it tell us? 
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
12. Use this function to plot the boxplot distribution for features. Try adding a title and name for axis. 
12. Save dataframe in csv format and the plot as png.

Note: Internet is your best friend. Remember that whenever you are stuck, resources and blogs can help you figure it out (Stack Overflow). 

If you are done, you can play around with different functions (ex. other plotting functions). Try to answer interesting questions you might have using the data.

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

There are hundreds of excellent resources online for learning Python and/or data science. A few good ones:

- [CodeAcademy](https://www.codecademy.com) offers interactive programming courses for many languages and tools, including Python and git
- [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/) is an excellent intro to Python by Jake VanderPlas; Jupyter notebooks are available [here](https://github.com/jakevdp/WhirlwindTourOfPython)
- Another excellent and free online book is Allen Downey's "Think Python"
- Object Oriented Programming in Python 3
(https://realpython.com/python3-object-oriented-programming/) 
- Jake Vanderplas's Python Data Science Handbook is also available online as a set of notebooks
- [Kaggle](https://www.kaggle.com) maintains a nice list of data science and Python tutorials

- Neuromatch Academy also has great tutorials available for Python in a computational neuroscience context.
    - Tutorial 1: https://compneuro.neuromatch.io/tutorials/W0D1_PythonWorkshop1/student/W0D1_Tutorial1.html
    - Tutorial 2: https://compneuro.neuromatch.io/tutorials/W0D2_PythonWorkshop2/student/W0D2_Tutorial1.html
- Introduction to Python in French (https://www.youtube.com/watch?v=cjFxd-0idHo)

If you are curious, eiger to learn more, you can also try out this tutorial which inspired much of the content you saw today: [Introduction to Python](https://neurohackademy.org/course/introduction-to-python-2/)
