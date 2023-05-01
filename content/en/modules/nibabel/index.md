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

summary: "Learning the basics of open data and open resource discovery."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "open_data.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

## Resources

We will watch the presentation **NiBabel: Neuroimaging data and file structures in Python** from Neurohackademy 2020 by Chris Markiewicz.

The original presentation and the practical notebook is can be found here: https://github.com/effigies/nibabel-presentations

You will need to install the example dataset with [DataLad](modules/datalad/).

```bash
mkdir ~/data
cd data
datalad install ///openneuro
cd openneuro
datalad get -r ds000114/sub-01

cd ~/data
datalad install git@github.com:OpenNeuroDerivatives/ds000228-fmriprep.git
cd ds000228-fmriprep
datalad get -r sourcedata/freesurfer/sub-pixar001/surf
datalad get sub-pixar001/anat/sub-pixar001_hemi-L_pial.surf.gii
datalad get sub-pixar001/func/sub-pixar001_task-pixar_hemi-L_space-fsaverage5_bold.func.gii
datalad get sub-pixar001/func/sub-pixar001_task-pixar_space-fsLR_den-91k_bold.dtseries.nii
```

You will need to create the environment with the 
```
pip install pipenv  # You need pipenv to create an environmnet
pipenv install Pipfile  # install the environment
pipenv run jupyter-notebook
```

Please follow the installation instrution

    Watch the video and follow along: https://www.youtube.com/watch?v=Y6ulmOlW1FI

The video presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=Y6ulmOlW1FI" title="NiBabel: Neuroimaging data and file structures in Python" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * Watch the video presentation by Sebastian Urchs and go over the slides.
 * 🎉 🎉 🎉 you completed this training module! 🎉 🎉 🎉

## More resources

https://nilearn.github.io/stable/manipulating_images/input_output.html#understanding-neuroimaging-data

https://nipy.org/nibabel/coordinate_systems.html

https://nipy.org/nibabel/nibabel_images.html#the-image-data-array

https://nipy.org/nibabel/images_and_memory.html

https://neurohackademy.org/course/introduction-to-the-geometry-and-structure-of-the-human-brain/