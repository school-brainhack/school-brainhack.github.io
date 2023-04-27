---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to python packaging with `pipy`"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [python, packaging]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "In this module, you will learn how to package python modules using `pypi`. This will let you install some of your own code with `pip`, dealing cleanly with dependencies, as well as share publicly a package."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "python_packaging.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * [Installation module](/modules/installation).
 * [Introduction to python for data analysis](/modules/python_data_analysis/) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources
This module was presented by Valérie Hayot-Sasson during BrainHack School 2020. The slides are available [here](https://docs.google.com/presentation/d/18aMOZBbKEKTHtiZZA5bRPOBwxOVoPLRT1c5FaQZYLQI/edit?usp=sharing).

The video of the presentation is available below (57:51):
<iframe width="560" height="315" src="https://www.youtube.com/embed/f2quLtfcQoQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exercice

 * To run this exercise, you will need a small python module. You can create a toy python module by following this [tutorial](https://www.tutorialspoint.com/python/python_modules.htm). It would be better to start creating one (or a couple of) module(s) for your project, so you work directly with a meaningful code base.
 * Add your module to a new git repository under your personal account. This is not necessary, but putting code on git control should be second nature at this stage :) Note that the module will read in a folder inside the repository. The top level directory is for configuration files for the project, not the code itself.
 * Create and populate a `README.md` file
 * Create and populate a `license.txt` file
 * Fill a `requirements.txt` file. Include everything needed for development, including e.g. `jupyter-notebook` and `pytest`.
 * Fill a `pyproject.toml` file. Start from a [template](https://martin-thoma.com/pyproject-toml/). These two last steps are much more meaningful if you are working with a code base for your project, rather than a toy module with no dependencies.
 * Configure the meta-data of your project with `setup.cfg`. Check the [documentation of pypi](https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata) for more info.
 * Add on `__init.py__` in your module folder. See this [example](https://careerkarma.com/blog/what-is-init-py/)
 * Try installing your package locally by running `pip install -e .` in your repository.
 * **Optional**: You can try to create the distribution files and publish this package on a test server of `pypi`. This step is described in this [tutorial](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives). The pypi test server is made to test how publishing a package works - so don't worry if this is just a test or if you make mistakes, the server exists for that purpose. If you upload the package on pipy itself, anybody will be able to install your software by typing `pip install <my_package>` but beware! `pipy` is a community resource, and you should only publish serious, well tested projects on there.
 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

 * The official `pipy` [packaging documentation](https://packaging.python.org/tutorials/packaging-projects).
 * The [guidelines for modern packaging](https://gist.github.com/effigies/9bbb424535d6a1d838d6325191c0a736) by [Chris Markiewicz](https://github.com/effigies).
