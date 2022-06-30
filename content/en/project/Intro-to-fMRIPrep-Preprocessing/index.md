---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-06-12" # Date you first upload your project.
# Title of your project (we like creative title)
title: "fMRIPrep 101 - Pre-processing fMRI data and extracting connectivity matrices"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Frederic St-Onge]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2020/stong3_fMRI_processing

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fmri, fmriprep, connectivity, nilearn]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project aimed to understand how to pre-process fMRI data using fMRIPrep. Through this learning experience, a tutorial was created."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "bhs2020.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Having little experience with neuroimaging and my PhD thesis using fMRI, I wanted to be able to start from raw data (in BIDS format) and learn how to process the data until I obtain derivatives (i.e. connectivity matrices). Based on the current PhD project that I am working on, using various atlases leads to varying results. As such, I wanted to extract connectivity matrices from pre-processed time-series using Nilearn, which comes pre-loaded with several atlases of interest. Finally, as most of my work will involve large cohorts (which might not be feasible to do on a personal computer), I wanted to be able to realize these analyses on a HPC, where resources can be used appropriately. Please note that more information on the project is available on [Github](https://github.com/brainhack-school2020/stong3_fMRI_processing).

<iframe width="560" height="315" src="https://www.youtube.com/embed/PTYs_JFKsHI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Tools

The project used the following tools:
 * Docker (for bids-validator and fMRIPrep)
 * Bids-validator (to validate bids)
 * fMRIPrep (to pre-process data)
 * Jupyter notebook (for deliverables)
 * Nilearn (to extract connectivity matrices)
 * Github (to version control and share the project)

### Data

The data used is a single, anonymized, subject from the Prevent-AD. We used 2 fMRI visits. Data is not available for reproduction, but more details on the cohort can be found [here](https://portal.conp.ca/dataset?id=projects/preventad-open)

### Deliverables

At the end of this project, we will have:
 - A Jupyter notebook detailing the failed first project.
 - A Jupyter notebook detailing the current fMRIPrep project.
 - A complete GitHub repo detailing the process.

## Results

### Github repo

For more details on the deliverables, please refer to the GitHub repo available [here](https://github.com/brainhack-school2020/stong3_fMRI_processing).

The tutorial was designed to be: 1) Easy to use, 2) Comprehensive and 3) Hopefully fun!

## Conclusion and acknowledgement

In conclusion, I was able to learn a lot of new tools and gain a deeper understanding of fMRIPreprocessing. I was able to create a tutorial on using fMRIPrep that, hopefully, will also serve others learning this software!

I want to thank my instructor, Desiree Lussier, and all the BHS2020 team for allowing me to learn so much in a short span of a month!
