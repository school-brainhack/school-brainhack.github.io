---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Neuroimaging data and file structures in Python"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [python, neuroimaging, data analysis]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning the basics of neuroimaging file format with Nibabel."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "https://nipy.org/nibabel/_static/reggie.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 1h30m for the basic content and 1h for the optional advanced content.

The prerequisites to take this module are:
 * the [DataLad](modules/datalad/) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server.
If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources

We will watch the presentation **NiBabel: Neuroimaging data and file structures in Python** from Neurohackademy 2020 by Chris Markiewicz.

The original presentation and the practical notebook is can be found [here](https://github.com/effigies/nibabel-presentations).
In this exercise, we will use the note book in the brainhack school repository.

### Downlad data and jupyter notebook

You will need to install the example dataset with [DataLad](modules/datalad/).

```bash
# download open neuro dataset
mkdir ~/brainhackschool_nibabel
cd ~/brainhackschool_nibabel
mkdir data
cd data
datalad install ///openneuro
cd openneuro
datalad get -r ds000114/sub-01

cd ~/brainhackschool_nibabel/data
datalad install git@github.com:OpenNeuroDerivatives/ds000228-fmriprep.git
cd ds000228-fmriprep
datalad get -r sourcedata/freesurfer/sub-pixar001/surf
datalad get -r sourcedata/freesurfer/fsaverage5

datalad get sub-pixar001/anat/sub-pixar001_hemi-L_pial.surf.gii
datalad get sub-pixar001/func/sub-pixar001_task-pixar_hemi-L_space-fsaverage5_bold.func.gii
datalad get sub-pixar001/func/sub-pixar001_task-pixar_space-fsLR_den-91k_bold.dtseries.nii

# get the surface data from midnight scan club
cd ~/brainhackschool_nibabel/data
wget -c https://raw.githubusercontent.com/MidnightScanClub/MSCcodebase/master/Utilities/Conte69_atlas-v2.LR.32k_fs_LR.wb/Conte69.L.inflated.32k_fs_LR.surf.gii 

# get the tutorial
cd ~/brainhackschool_nibabel
wget -c https://raw.githubusercontent.com/school-brainhack/school-brainhack.github.io/tree/main/content/en/modules/nibabel/Pipfile
wget -c https://raw.githubusercontent.com/school-brainhack/school-brainhack.github.io/tree/main/content/en/modules/nibabel/Nibabel.py

# make a temporary directory to dump things
mkdir ~/brainhackschool_nibabel/data/tmp
```

### Set up environment

You will need to create the environment with the `Pipfile`.

```
pip install pipenv  # You need pipenv to create an environmnet
cd ~/brainhackschool_nibabel/
pipenv install Pipfile  # install the environment
pipenv run jupyter-notebook
```
From here you can navigate to the presentaion `Nibabel.py`

The first comment by Hao-Ting Wang includes time stamps of this video. 
The time stamps highlight the advance and optional sections if you wish to skip.
You can skip the irrelevant sections.
You need to watch all the basic content to complete the excercise.

 - **Basic** - Be able to load and save different types of neuroimaging files in Nibabel
 - **Basic** - How to work with volumetric data
 - **Advanced** - Understand the difference between array and array proxy images
 - **optional** - Acquire a passing familiarity with the structures of surface images, CIFTI-2 files and tractogram

The video presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=Y6ulmOlW1FI" title="NiBabel: Neuroimaging data and file structures in Python" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * Watch the video presentation by Chris Markiewicz and go over the slides.

 * In a separate notebook, complete the following exercises:

    * Use the nilearn library function `fetch_atlas_difumo` to get the 64 parcellation image. As we learned in the video, the data in this image is just a number array and you can maniputate it with numpy. Please extract the 16th region, binarize it, and save it as a new nifti image.

    * Use the slicer opject to view the new nifti file we created in the three different view.

    * Bonus: in 200 words, describe the conceptual differences between array and array proxy images.

 * Follow up with your local TA(s) to validate you completed the exercise correctly.
 * 🎉 🎉 🎉 you completed this training module! 🎉 🎉 🎉

## More resources

Nilearn has some high level wrappers for nibabel I/O function, we encourage you to have a look:
https://nilearn.github.io/stable/manipulating_images/input_output.html#understanding-neuroimaging-data

Here are all the links mentioned in the presentations:

https://nipy.org/nibabel/coordinate_systems.html

https://nipy.org/nibabel/nibabel_images.html#the-image-data-array

https://nipy.org/nibabel/images_and_memory.html

https://neurohackademy.org/course/introduction-to-the-geometry-and-structure-of-the-human-brain/
