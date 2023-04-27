---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Research data management using DataLad"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [datalad, RDM, week2]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning the basics of the [DataLad](http://handbook.datalad.org) version control system for research data. DataLad is a community project built on top of git and [git-annex](https://git-annex.branchable.com/) and a critical tool for reproducible cognitive neuroscience."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "datalad.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 3h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.
 * the [introduction to git and github](/modules/git_github) module can help, but not required.
 * the [project management](/modules/project_management) module is recommended, but not required.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school.brainhack [at] gmail [dot] com.

## Resources
This module was presented by [Adina Wagner](https://twitter.com/AdinaKrik) during the HBM Brainhack in 2020.

The material of the tutorial is available [here](http://handbook.datalad.org/en/latest/code_from_chapters/OHBM.html).

The video of her presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/QsAqnP7TwyY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For the installation of the DataLad please follow the instructions in the [DataLad Handbook](http://handbook.datalad.org/en/latest/intro/installation.html)

## Exercise
 * Follow along the tutorial with Adina. You can copy paste the commands from the DataLad handbook section linked above, while following the video.
   * **Warning 1**: The url for one of the books in the tutorial (`byte-of-python.pdf`) is broken, so the pdf is unreadable. This does not impact the tutorial, but just don't be surprised if that document does not open. Also it shows how important it is to create persistent URLs when you release material, such as those offered on platforms like `zenodo`, `osf` or `figshare`.
   * **Warning 2**: Follow the tutorial you may need to install new command line tools, such as `tree`.
   * **Warning 3**: To be able to clone the some repositories throughout the hands on parts of the lecture you will need to produce a SSH key and register it with your github account. To be able to create your SSH key please follow the [instructions from Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key). From the Git Bash terminal (a bash emulation that comes with the installation of Git) go to where the ssh key file is stored and run `cat ~/.ssh/id_rsa.pub` command to see the key. It will be a very long string of letters and numbers starting with an indicator `ssh-rsa`. Copy the whole chunk of the key string and go to your  GitHub account, from Settings> SSH & GPG keys menu click to the New SSH key button. Paste the copied key into the `Key` text box and give a title to your key such as `home_laptop_github_key`. And click the `Add SSH Key` button to save it. Now you have your SSH key is settled for the current operating system environment and you are ready to run `datalad clone` command by using `git@github.com:...` links listed throughout the tutorial. 
   *  Follow up with your local TA(s) to validate you completed the exercises correctly.
   *  :tada: :tada: :tada: You completed this training module! :tada: :tada: :tada:
   
## More resources

If you want to learn more, check:
 * The [DataLad handbook](http://handbook.datalad.org), which features lot of additional resources as well!
 * The [DataLad datasets](https://github.com/datalad-datasets) github organization, which provides an easy access to a number of data resources. This type of DataLad repositories are the easiest way to get access to datasets.
 * The [DataLad lecture series](https://www.youtube.com/playlist?list=PLEQHbPfpVqU5RSPiyFuPdDlSUEd-XoPV-)
 * The [DataLad Course Material](https://github.com/datalad-handbook/datalad-course)
 * Note that for the last part of the tutorial you will need to install [singularity](https://sylabs.io/singularity/) and the `datalad-container` extension (installable through `pip`).
 * All of the Open Neuro datasets available on the [Open Neuro](https://github.com/OpenNeuroDatasets) github organization.
 * You can also read about the [YODA](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html) principles for reproducible papers.
