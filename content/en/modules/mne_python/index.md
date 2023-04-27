---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Working with MNE-Python and EEG-BIDS"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [MNE, python, EEG, BIDS, brain dynamics]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This repo includes a tutorial for Working with MNE-Python and EEG-BIDS."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "brain_dynamics.gif"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 2.30h.

The prerequisites to take this module are:
 * Installations
 * Creting a virtual environment:
       - if you are using Conda, please a Conda virtual environment by following instructions [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
       - otherwise ceate a new Python virtual environment by following the instructions [here](https://docs.python.org/3/library/venv.html).
 * Install MNE and MNE-BIDS:
       - Install MNE by following instructions [here](https://mne.tools/stable/install/manual_install.html)
       - Install MNE-BIDS by following the instructions [here](https://mne.tools/mne-bids/stable/install.htm)
       - if you are using conda environment with `conda create --strict-channel-priority --channel=conda-forge --name=mne mne-base`
       - otherwise with `pip install mne`.
       
If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school.brainhack [at] gmail [dot] com.

## Resources
This module was presented by Davide Momi during the [Brainhack Toronto](https://brainhackto.github.io/global-toronto-12-2022/), and the associated notebooks are available [here](https://github.com/Davi1990/mne_eeg_workshop)

The video of the presentation is available below (1h33):
<iframe width="560" height="315" src="https://www.youtube.com/embed/du1XezR246w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Tutorial
To run the code locally please follow the instructions
 * Download the folder using:
```
git clone https://github.com/Davi1990/mne_eeg_workshop/
```

```
cd folder_path_to_the_cloned_repo
```

 * Install the required dependencies using:
```
pip install -r requirements.txt
```

 * Download the required [data folder](https://drive.google.com/drive/folders/1DO-dXfIXzGDzmgcWRMtYvX30ZECYzRYd?usp=sharing)

 * Download the [raw file](https://drive.google.com/file/d/1-RSyaXp2Chx0zLuaAnlgK8o1VMo3enx8/view?usp=share_link)

 * Start a new jupyter notebook. For this follow the instructions below:
       - Open the terminal
       - Type jupyter notebook
       - If you’re not automatically directed to a webpage copy the URL printed in the terminal and paste it in your browser
       - Once on the webpage, navigate to the `mne_eeg_workshop` you cloned.
       - upload the notebook associated with notebook.
       
## Exercise

1. Read through the notebook running all the cells
2. Complete the exercises in the notebook

**Exercise 1** Check information on the MNE-BIDS file that was saved as part of Tutorial 01 and fill the cells in the notebook with your answers to the questions below.

       How many channels do you have for each type of sensor?
       What is the sampling frequency?
       Have the data been filtered?
       What is the frequency of the line noise?
       Is there any bad channel?
       

**Exercise 2** Import a new epoched file and generate figure of both evoked response and principal components

        Read the file 'sub-s01_task-faceFO_eeg.fif' as an epoched object
        Make a joint plot of the time-series?
        Create a variable with the array of the evoked data
        Decompose the data using SVD (use the function numpy.linalg.svd)
        Make a matplotlib figure with 1 row and 5 columns and plot the first 5 components using the function mne.viz.plot_topomap


After finishing each of your exercise, rename the notebook and save it to your local with your answers to share with your TA(s).
Follow up with your local TA(s) to validate you completed the exercises correctly
 :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:


 ## More resources

 - Other great resources to get started with plotting in python:
    -  [MNE-Python](https://mne.tools/stable/auto_tutorials/index.html)
    -  [Neurodesk](https://www.neurodesk.org/tutorials/electrophysiology/eeg_mne-python/)

 <iframe width="560" height="315" src="https://www.youtube.com/embed/MYcCRhEb5Ic" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
