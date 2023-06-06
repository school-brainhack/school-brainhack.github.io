---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Project management"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [open data, fair, license, standards, github]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning about the importance and benefits of project management adhering to community standards to achieve shareable science."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "fig_redpen_blackpen.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * the [open data](/modules/open_data) module.
 * the [terminal](/modules/introduction_to_terminal) module.
 * the [Git and GitHub](/modules/git_github) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school.brainhack [at] gmail [dot] com

## Resources

This module was presented by [Elizabeth Dupre](https://elizabeth-dupre.com/#/) during the QLSC 612 course in 2020, with content adapted from presentations by [Chris Gorgolewski](https://twitter.com/chrisgorgo).

The slides are available [here](https://github.com/neurodatascience/course-materials-2020/blob/master/lectures/13-may/01-standards-for-project-management/NDS2020_ShareableScience.pdf).

The video of her presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/aBMc8bgSK6o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

### Your understanding of project management 

Prepare your answers in an online document (e.g. using hackmd.io).
 * Let's pick a license...
   * you want to share code and make sure it can be used as widely as possible, but you still get credited. Which license do you pick and why?
   * you want to share data, get credited, allow for modifications but not commercial usage. Which license do you pick and why?
 * Pick a public dataset and explain if it is FAIR. You can pick from the list below if you need inspiration.
   * [ADNI](http://adni.loni.usc.edu/)
   * [UK biobank](https://www.ukbiobank.ac.uk/)
   * [CIMAQ](http://www.cima-q.ca/en/home/)
 * Find an example of a neuroimaging paper described on the open science framework (or somewhere else), with 1. Code available? 2. Documentation for data analysis available? 3. Data available? For each aspect, summarize briefly the standards followed (if any).


### Create a project template for your Brainhack School project 

We have learned about the community standard of data sharing in the previous exercise and how that improves communication and collaboration with researchers.
The same principle can be applied to your analysis code. Using a consistent project template will help when your project grow in the long run.
For this section, please prepare your answer as a GitHub repository. 
We will follow the first lesson [Set up your project](https://goodresearch.dev/setup.html) in the [Good Research Code Handbook](https://goodresearch.dev/index.html)

:memo: Please skip the [Install a project package](https://goodresearch.dev/setup.html#install-a-project-package) section. We recommend to revisit this part after completing the [python packaging](/modules/packaging) module.

The end result will be a logically organized project skeleton that's synced to version control.
The instructor should be able to verify your progress through 1. a public GitHub repository and 2. clone and test your project on their own machine.

 * Pick a short and descriptive name for your project....
   * Create a folder in your home directory.
   * You should have created a GitHub account when you completed the installation module. Now we want to create a GitHub repository of the same name, for convenience. 
   * Now you should see some suggestions on the GitHub page to help you initialise the project repository. Which one should you use?

 * The next step is to create a virtual environment and an associated file describing the environment, so you can reinstall everything if you need to start fresh. 
   * Create a conda environment of the same name of your project.
   * Activate this environment and install the same packages you did in the [installation](/modules/installation) module.
   * Export this environment and save it as a file named `environment.yml` at the root of your project repository.
   * Now commit and push this environment file to your GitHub repository.

* Next, let's create a `.gitignore` file with the help of GitHub magic.
   * On your GitHub repository page, click on `Add file` - `create new file`. 
   * Now enter `.gitignore` into the file name. You will see a drop down menu appear on the right hand side.
   * Pick the python template. Commit this file.
   * Now use the terminal and pull this change to your local directory. 
  
  :bulb: With the same principle, you can also create a `LICENSE` file through GitHub.

 * Next we will populate the directory with a project skeleton and some basic descriptions. 
   * Create the directories described in the lesson with command `mkdir`. 
   * Try to add these changes to git. You should notice empty directories are not added, this is because git will only push files.
   * To work around this issue, let's create a file named `.gitkeep` in each of the empty directory using command `touch`. 
   * Now try to add and commit these files again. 

 * (Optional) Creating a project package
   Creating a project package can be difficult for the first time, but the pay off is substantial: your project structure will be clean, you won’t need to change Python's path, and your project will be pip installable. This is the standard approach in the data science world.
   This is a minimal demo for a installable package. We encourage you to revisit [Install a project package](https://goodresearch.dev/setup.html#install-a-project-package) after completing the [python packaging](/modules/packaging) module.
    * Create a file under `src/` named `helloworld.py`, with one line `print('hello world')`.
    * Create a file under `src/` named `__init__.py`.
    * Create a `setup.py` file in the root directory with the following lines:
      ```
      from setuptools import find_packages, setup

      setup(
          name='src',
          packages=find_packages(),
      )

      ```
    * Finally, activate the project virtual environment you created earlier. Install your package:
      ```
      pip install -e .
      ```  
    * To verify the completion of this part, you should be able to run the following code from a python kernel as long as the virtual environment is activated:
      ```
      import src.helloworld
      >>> hello world
      ```

* Follow up with your local TA(s) to validate you completed the exercise correctly.
* :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

If you are curious to learn more about BIDS, check the [BIDS specifications](https://bids-specification.readthedocs.io/en/stable/). There will also be a training module on BIDS in week 2.
We encourage you to revisit [Install a project package](https://goodresearch.dev/setup.html#install-a-project-package) after completing the [python packaging](/modules/packaging) module.

Some documentation on standards for project organization:
 * the entire "the Turing way" documentation is relevant, but the section on [project design](https://the-turing-way.netlify.app/project-design/project-design.html) is the most important for this training module.
 * the [YODA principles](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html).
 * the [Good Research Code Handbook](https://goodresearch.dev/) has lots of resources to help you learn industry standard research code management.

Check out [this repository](https://github.com/SIMEXP/fmriprep-denoise-benchmark) which follows the principle of the project set up in the Good Research Code Handbook.

Finally, a [blog post](http://ivory.idyll.org/blog/2015-on-licensing-in-bioinformatics.html) on choosing a license for open science projects by Titus Brown.
