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
image: "reggie.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 1h30m for the basic content and 1h for the optional advanced content.

 - **Basic** - Be able to load and save different types of neuroimaging files in Nibabel. Know how to work with volumetric data.
 - **Advanced** - Understand the difference between array and array proxy images.
 - **Optional** - Acquire a passing familiarity with the structures of surface images, CIFTI-2 files and tractogram.

The prerequisites to take this module are:
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.
 * the [DataLad](/modules/datalad) module.
 * the [python data analysis](/modules/python_data_analysis) module (recommended for Python familiarity).

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server.
If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources

We will watch the presentation **NiBabel: Neuroimaging data and file structures in Python** from Neurohackademy 2020 by Chris Markiewicz.

The original presentation and the practical notebook can be found [here](https://github.com/effigies/nibabel-presentations).
In this exercise, we will use the notebook in the brainhack school repository. Follow the instructions below to run both. 

### Downlad data and jupyter notebook

You will need to install the example dataset with [DataLad](/modules/datalad).

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
wget -c https://raw.githubusercontent.com/school-brainhack/school-brainhack.github.io/main/content/en/modules/nibabel/requirements.txt
wget -c https://raw.githubusercontent.com/school-brainhack/school-brainhack.github.io/main/content/en/modules/nibabel/NiBabel.py

# make a temporary directory to dump things
mkdir ~/brainhackschool_nibabel/data/tmp
```

### Set up environment

You will need to create the environment with the `requirements.txt` file.

```
pip install virtualenv

cd ~/brainhackschool_nibabel/
virtualenv env
source env/bin/activate
pip install -r requirements.txt  # install the environment
```
From here you can launch `jupyter notebook` and navigate to the presentaion `Nibabel.py`, or launch the notebook directly using:
```
jupyter notebook Nibabel.py
```

## Material

Follow the `Nibabel.py` notebook along with the presentation.

The time stamps of this video are as follows.
You need to watch all the basic content to complete the excercise.
You can skip the optional sections.

 - 0:00 Introduction
 - 0:44 Brief introduction to NiBabel / some Neurohackademy related business
 - 2:01 Start of the talk
 - 3:01 Installation of NiBabel
 - 6:01 Learning objective of the original presentation
 - 7:32 Basic file input/output (I/O) (basic)
 - 12:03 Data array of spatial image (basic)
 - 20:11 Affine (basic)
 - 32:13 Header (basic)
 - 36:55 Create an image (basic)
 - 39:57 Break
 - 47:27 Array and array proxy (advanced)
 - 1:06:52 Slicing image (basic)
 - 1:13:13 Question time 
 - 1:14:17 Surface image (optional)
 - 1:25:36 CIFTI-2 image (optional)
 - 1:30:22 Tractogram (optional)
 - 1:34:38 Summary and ending

The video presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/Y6ulmOlW1FI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Exercise

 * Watch the video presentation by Chris Markiewicz and go over the `Nibabel.py` notebook.

 * In a separate notebook, complete the following exercises:

    * Use the nilearn library function `fetch_atlas_difumo` to get the 64 parcellation image. As we learned in the video, the data in this image is just a number array and you can maniputate it with numpy. Please extract the 16th region, binarize it, and save it as a new nifti image.

    * Use the slicer object to view the new nifti file we created in the three different views.

    * Bonus: in 200 words, describe the conceptual differences between array and array proxy images.

 * Follow up with your local TA(s) to validate you completed the exercise correctly.
 * 🎉 🎉 🎉 you completed this training module! 🎉 🎉 🎉

## More resources

Nilearn has some high level wrappers for nibabel I/O function, we encourage you to have a look:
https://nilearn.github.io/stable/manipulating_images/input_output.html#understanding-neuroimaging-data

Here are all the links mentioned in the presentations:

- https://nipy.org/nibabel/coordinate_systems.html
- https://nipy.org/nibabel/nibabel_images.html#the-image-data-array
- https://nipy.org/nibabel/images_and_memory.html
- https://neurohackademy.org/course/introduction-to-the-geometry-and-structure-of-the-human-brain/
