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

summary: "This repo includes a tutorial for working with dMRI data using DIPY"

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "dMRI.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 3.30h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.
 
If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources
This module was presented by Davide Momi during the of [Neuroimaging Carpentry](https://conp-pcno-training.github.io/neuroimaging-carpentry/) workshop series, and the associated notebooks are available [here](https://github.com/Davi1990/Intro_to_dMRI_workshop).

The video of the presentation is available below (duration 1h33).
<iframe width="560" height="315" src="https://www.youtube.com/embed/HM3lMplqTM4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Tutorial
This tutorial uses `Jupyter` notebooks. Follow the instructions to install the necessary dependencies in a virtual environment. 

1. Clone this repo using:

    ```bash
    git clone https://github.com/Davi1990/Intro_to_dMRI_workshop
    ```

2. Create an environment in the cloned repository:

    ```bash
    cd Intro_to_dMRI_workshop
    virtualenv env
    ```

    To activate the environment, use the following command in `Intro_to_dMRI_workshop/`

    ```bash
    source env/bin/activate
    ```

3. In the activated environment, install the dependencies and jupyter-lab:

    ```bash
    pip install -r requirements.txt
    pip install jupyterlab
    ```

5. Finally download the necessary data from OSF.
    Data from a single subject that's used in this tutorial is available and can be downloaded by running:

    ```bash
    mkdir ./data
    cd data
    osf -p cmq8a fetch ds000221_subject/ds000221_sub-010006.zip
    unzip ds000221_sub-010006.zip
    ```

   Note: you can also clone the full dataset with OSF. This will create a `data` folder at the root of the repository. Since the command clones the entire repository, this may be quite large and take a while to download.
    ```bash
    osf -p cmq8a clone ./data
    ```

## Extra steps

> ## Test the installation
>
> Installation information for a package can be checked by pip from the bash terminal:
> ```bash
> pip show dipy
> ```
>
> You can also see the packages and versions of all `pip`-installed dependencies
> by typing:
> ```bash
> pip freeze
> ```
>
> You can also imported the library in Python by
> running a python terminal:
> ```bash
> python
> ```
> and then import the module:
> ```python
> import dipy
> ```
>
> Alternatively, the package version can also be checked by running, for example:
> ```python
> import dipy
> print(dipy.__version__)
> ```
>

Make sure you are in the root of `Intro_to_dMRI_workshop`, and start the notebook server to run the notebook with `JupyterLab`.
```bash
jupyter-lab
```

In either case, the commands will print some information about the notebook
server in the terminal, and a web browser will be opened to the URL of the web
application (by default, http://127.0.0.1:8888). The users will be presented with
the directory structure of the current directory, and they will be able to run
the notebook of interest.

## Exercise

 * Read through the notebooks running all the cells

 * Complete the exercises in the notebooks

    * **Exercise 1** Get a list of all diffusion data in NIfTI file format (`01_introduction notebook`).

    * **Exercise 2** Plot the axial and radial diffusivity maps of the example given. Start from fitting the preprocessed diffusion image (`03_diffusion_tensor_imaging notebook`).

    * **Exercise 3** Simulate the ODF for two fibre populations with crossing angles of 90, 60, 45, 30, and 20 degrees. We have included helpful hints and code to help you get started (`04_constrained_spherical_deconvolution notebook`).

    * **Exercise 4** Repeat the tractography, but apply a binary stopping criteria (BinaryStoppingCriterion) using the seed mask. Visualize the tractogram (`05_deterministic_tractography notebook`)!

    * **Exercise 5** Set the color of the streamlines to display the values of the FA map and change the opacity to 0.05 (`05_deterministic_tractography notebook`).

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

 ## More resources

- For additional information about `Python` setups besides the package manuals, users are encouraged to read the [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) Carpentries lesson.
 - Other great resources to get started with dMRI:
    -  [DIPY](https://dipy.org/) website, including documentation and tutorials.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7Bl38jfBJu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
