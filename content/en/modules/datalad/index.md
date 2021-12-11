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

Contact Pierre Bellec if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by [Adina Wagner](https://twitter.com/AdinaKrik) during the HBM brainhack in 2020.

The material of the tutorial is available [here](http://handbook.datalad.org/en/latest/code_from_chapters/OHBM.html).

The video of her presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/QsAqnP7TwyY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exercise
 * Follow along the tutorial with Adina. You can copy paste the commands from the datalad handbook section linked above, while following the video.
   * **Warning**: the url for one of the books in the tutorial (`byte-of-python.pdf`) is broken, so the pdf is unreadable. This does not impact the tutorial, but just don't be surprised if that document does not open. Also it shows how important it is to create persistent URLs when you release material, such as those offered on platforms like `zenodo`, `osf` or `figshare`.
   * **warning 2** to follow the tutorial you may need to install new command line tools, such as `tree`.
 * Check with Pierre Bellec to validate that the history of your datalad repository includes all the steps of the tutorial.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

If you want to learn more, check:
 * the [datalad handbook](http://handbook.datalad.org), which features lot of additional resources as well!
 * the [datalad datasets](https://github.com/datalad-datasets) github organization, which provides an easy access to a number of data resources. This type of DataLad repositories are the easiest way to get access to datasets.
 * note that for the last part of the tutorial you will need to install [singularity](https://sylabs.io/singularity/) and the `datalad-container` extension (installable through `pip`).
 * all of the Open Neuro datasets available on the [Open Neuro](https://github.com/OpenNeuroDatasets) github organization.
 * you can also read about the [YODA](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html) principles for reproducible papers.
