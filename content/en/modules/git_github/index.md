---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Using git and github"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [git, github]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning the basics of version control using git, as well as the social coding platform called [github](https://github.com)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "git_github.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/terminal) module.

Contact Pierre Bellec if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by [Elizabeth Dupre](https://elizabeth-dupre.com/#/) during the QLSC 612 course in 2020, with content adapted from the software carpentries by [Elizabeth Dupre](https://elizabeth-dupre.com/#/).

All the tutorial notes are available [here](https://emdupre.github.io/git-course/).

The video of her presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/fBgxmpk9C4I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * send a request through discord on #general to be added to the github organization [PSY6983-2021](https://github.com/PSY6983-2021).
 * create a local repository following the naming convention `<last_name>_project`. Don't worry, you will be able to change this name latter, and possibly merge the content in another repository if you decide to team up with other people.
 * initialize your repo with a README and a LICENSE.
 * Create an issue for adding a short bio.
 * Using the command line, clone this repository locally on your computer.
 * Create a branch named after the issue, e.g. `iss1`.
 * Add a short bio to the README, including a picture of your github avatar. You can adapt the following snippet
 ```
 <a href="https://github.com/pbellec">
    <img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/>
    <br /><sub><b>Pierre bellec</b></sub>
 </a>
 ```
 this is a bit of html, which gets rendered in markdown documents. You will need to click on your profile picture to figure out what to replace `1670887` with the ID of your profile picture. Don't forget to replace `pbellec` by your github handle.
 * Using the command line, commit this change to your local repository. Make sure you registered your github user name and email address, so the commit is accurately credited to you when you push it on github.
 * Using the command line, push the branch and your changes to the github repository.
 * Using the github interface, open a new pull request with your changes. Use a descriptive name for the pull request, e.g. `iss1 - add bio`.
 * Using the github interface, request a review of your changes by `pbellec`.
 * Once pbellec has approved the review, merge the pull request to the `main` branch.
 * Close the issue.
 * Follow up with Pierre Bellec to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

If you are curious to learn more advanced capabilities for git, you can check this tutorial "Effective use of git" by Ankur Sinha organized for the [INCF/OCNS software working group](https://ocns.github.io/SoftwareWG/2021/06/09/software-wg-tutorials-at-cns-2021-online-bash-git-and-python.html).

<iframe width="560" height="315" src="https://www.youtube.com/embed/CRCtRilX3NA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
