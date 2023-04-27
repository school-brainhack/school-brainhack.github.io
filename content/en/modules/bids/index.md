---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "The brain imaging data standards and applications"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [bids, pybids, week2]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning the basics of the [brain imaging data structure](https://bids.neuroimaging.io/), the [pybids](https://bids-standard.github.io/pybids/user_guide.html) interface to interact with a BIDS-compliant dataset as well as the [BIDS apps](https://bids-apps.neuroimaging.io/apps/) - a collection of software designed to operate on BIDS datasets."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bids.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 2h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/terminal) module.
 * the [python for data analysis](/modules/python_data_analysis) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources
This module was presented by [Christopher J. Markiewicz](https://effigies.github.io/) during the QLSC 612 course in 2020.

The slides are available [here](https://effigies.github.io/bids-ecosystem).

The video of his presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/ceB3Nne-MDo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exercise
 * Download a few subjects (n=3) from the dataset [DS000228](https://openneuro.org/datasets/ds000228/versions/1.1.0) on openneuro. Hint: the dataset is available with datalad from this [git](https://github.com/OpenNeuroDatasets/ds000228) repository.
 * Check that the resulting folder is a bids-compliant dataset using the bids validator (using a web browser or a local `npm` install). Did you get any warnings? Explain what they are and whether they are a concern.
 * Install pybids. Use pybids to get a list of all BOLD `nii.gz` files for subject `pixar003`. In which folder did you find them? is it logical? You may want to have a look at the [BIDS documentation](https://bids.neuroimaging.io/) to familiarize yourself with the BIDS standard.
 * Using pybids, get a list of the flip angles in `DS000228`.
 * Clone a Midnight Brain Scan dataset from this [git](https://github.com/OpenNeuroDatasets/ds000224) repository. Use `pybids` to load the `participant.tsv` file as a pandas dataframe in python.
 
 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

If you want to learn more about BIDS and pybids, check:
 * the [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/index.html#),
 * the [BIDS documentation](https://bids.neuroimaging.io/),
 * the [dicom2bids](https://unfmontreal.github.io/Dcm2Bids/) converter - we have local support for this one.
 * the [pybids documentation](https://bids-standard.github.io/pybids/user_guide.html)
