---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to dMRI"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [DIPY, python, Tractography, BIDS, Tensor]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This repo includes tutorial for working with dMRI data using DIPY."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "dMRI.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 3.30h.

The prerequisites to take this module are:
 * Installations
 * [Introduction to dMRI](https://psy6983.brainhackmtl.org/modules/introduction_to_dMRI/) module.

Contact Davide Momi if you have questions on this module, or if you want to check that you completed successfully all the exercises.


## Resources
This module was presented by Davide Momi during the of [Neuroimaging Carpentry](https://conp-pcno-training.github.io/neuroimaging-carpentry/) workshop series, and the associated notebooks are available [here](https://github.com/Davi1990/Intro_to_dMRI_workshop)

The video of the presentation is available below (1h33):
<iframe width="560" height="315" src="https://www.youtube.com/embed/HM3lMplqTM4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Tutorial
If users choose to run the `Jupyter` notebooks locally, the following
dependencies will need to be installed:

- [ANTs] : used to register different anatomical data.
- [FSL] : used for different data preprocessing steps.
- [DIPY] : used for diffusion MRI data processing.
- [FURY] : used for anatomical data visualisation purposes.
- [Matplotlib] : used for data visualisation purposes.
- [Nilearn] : used for anatomical data visualisation purposes.
- [osfclient] : used to download the necessary data.
- [PyBIDS] : used to check the data structure [BIDS] compliance.


To run the code locally please follow the instructions:

1) Clone this repo using:
```
git clone https://github.com/Davi1990/Intro_to_dMRI_workshop
```

2) Install the required dependencies using:
```
pip install -r requirements.txt
```

3) Download the necessary data

Notebooks expect them to be placed in the `data` folder that exists in the root
of the repository.

Note that the above command clones the entire repository, which may be quite large and
take a while to download. Alternatively, data from a single subject is available
and can be downloaded by running:
~~~
$ cd ./data
$ osf -p cmq8a fetch ds000221_subject/ds000221_sub-010006.zip
$ unzip ds000221_sub-010006.zip
~~~
{: .language-bash}


## Extra steps

> ## Test the installation
>
> Test installation information for a package can be checked by running, for
> example:
> ~~~
> $ pip show dipy
> ~~~
> {: .language-bash}
>
> Similarly, it can be checked that a given package can be imported in Python by
> running, for example:
> ~~~
> $ python
> >>> import dipy
> ~~~
> {: .language-bash}
>
> Alternatively, the package version can also be checked by running, for example:
> ~~~
> $ python
> >>> import dipy
> >>> print(dipy.__version__)
> ~~~
> {: .language-bash}
>
> You can also see the packages and versions of all `pip`-installed dependencies
> by typing:
> ~~~
> $ pip freeze
> ~~~
> {: .language-bash}
{: .discussion}

In order to run the notebooks, the notebook server needs to be started. Once the
current directory changed to the root of the code directory, the server is
started running:
~~~
$ ipython notebook
~~~
{: .language-bash}

if using `IPython`, and running:

~~~
jupyter-lab
~~~
{: .language-bash}

if using `JupyterLab`.

In either case, the commands will print some information about the notebook
server in the terminal, and a web browser will be opened to the URL of the web
application (by default, http://127.0.0.1:8888). The users will be presented to
the directory structure of the current directory, and they will be able to run
the notebook of interest.

For additional information about `Python` setups besides the package manuals,
users are encouraged to read the [Programming with Python] Carpentries lesson.

The data used in the lesson is hosted in [OSF]. It can be downloaded by running:
~~~
$ osf -p cmq8a clone ./data
~~~
{: .language-bash}

## Exercise

1. **Read through the notebook running all the cells**
2. **Complete the exercises in the notebook**

**Exercise 1** Get a list of all diffusion data in NIfTI file format.

**Exercise 2** Plot the axial and radial diffusivity maps of the example given. Start from fitting the preprocessed diffusion image.

**Exercise 3** Simulate the ODF for two fibre populations with crossing angles of 90, 60, 45, 30, and 20 degrees. We have included helpful hints and code below to help you get started.

**Exercise 4** Repeat the tractography, but apply a binary stopping criteria (BinaryStoppingCriterion) using the seed mask. Visualize the tractogram!

**Exercise 5** Set the color of the streamlines to display the values of the FA map and change the opacity to 0.05.



 * Follow up with Natasha Clarke to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:


 ## More resources

 - Other great resources to get started with plotting in python:
    -  [DIPY](https://dipy.org/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/7Bl38jfBJu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
