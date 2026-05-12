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

The estimated time to complete this training module is 2h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school.brainhack@gmail.com.

## Module material

This module uses material created by Software Carpentry; specifically, their [git Novice](https://swcarpentry.github.io/git-novice/) lesson.
While the full Software Carpentry lesson material covers a half-day of content, we only cover a subset of the episodes here.
Specifically, we cover:

1. Automated Version Control
2. Setting Up Git
3. Creating a Repository
4. Tracking Changes
7. Remotes in GitHub
8. Collaborating

A video of [Elizabeth DuPre](https://elizabeth-dupre.com/#/) presenting related material is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/fBgxmpk9C4I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Additional resources

For students who are interested in learning more about git and GitHub, we highly recommend reviewing the full Software Carpentry lesson.
Software Carpentry is also actively developing an [intermediate level git and GitHub lesson](https://carpentries-incubator.github.io/byte-sized-rse-git-intermediate/), for anyone hoping to dive deeper into git and GitHub practices.


## Exercise

 * send a request at the "Using Git and Github" module post at the modules channels of Discord server by typing "@<user-handle-of-your-TA> please add my <github-user-name>" to the github organization." This will alert your local TA(s) to add you to the [school-brainhack](https://github.com/brainhack-school2026/) organization.
 * create a new repository within the [school-brainhack](https://github.com/brainhack-school2026/) organization following the naming convention `<last_name>_project`. Don't worry, you will be able to change this name later, and possibly merge the content in another repository if you decide to team up with other people.
 * initialize your repo with a README and a LICENSE.
 * Create an issue for adding a short bio.
 * Using the command line, clone the repository locally to your computer.
 * Add a short bio to the README, including a picture of your github avatar. You can adapt the following snippet
 ```
<a href="https://github.com/lunebellec">
   <img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/>
   <br /><sub><b>Lune Bellec</b></sub>
</a>
 ```
 This is a bit of html, which gets rendered in markdown documents. You will need to click on your profile picture to figure out what to replace `1670887` with the ID of your profile picture. Don't forget to replace `lunebellec` by your github handle.
 * Using the command line, commit this change to your local repository. Make sure you registered your github user name and email address, so the commit is accurately credited to you when you push it on github.
 * Using the command line, push your changes to the github repository.
 * Using the github interface, mention your new commit in the existing issue.
 * Using the github interface, tag your local TA (by choosing their github handle among the listed ones) in the existing issue.
 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## Even more resources

* For more detailed instructions please check [GitHub's resources](https://docs.github.com/en)
* [The Turing Way](https://the-turing-way.netlify.app/collaboration/github-novice.html) discusses using for using GitHub for open research.
* For common Mistakes and Experiences with using Git and Github: [dangitgit.com](https://dangitgit.com/)
* Jenny Tou wrote a git concept module and initially presented her workshops at Brigham and Women's Hospital in 2019. The video found here is a shortern version of the original presentation ; please contact Jenny for the complete presentation materials.
<iframe width="560" height="315" src="https://www.youtube.com/embed/epFXYvPCrKU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* If you are curious to learn more advanced capabilities for git, you can check this tutorial "Effective use of git" by Ankur Sinha organized for the [INCF/OCNS software working group](https://ocns.github.io/SoftwareWG/2021/06/09/software-wg-tutorials-at-cns-2021-online-bash-git-and-python.html).
<iframe width="560" height="315" src="https://www.youtube.com/embed/CRCtRilX3NA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* [Here](https://learngitbranching.js.org/) is an interactive page to learn Git and visually observe how the branching works under version control.
