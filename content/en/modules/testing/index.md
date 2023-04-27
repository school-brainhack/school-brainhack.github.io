---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Software testing and continuous integration"

# Your project GitHub repository URL
github_repo: "https://github.com/gkiar/intro2testing"

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [testing, continuous integration, python]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Introduction to testing practices for software development and in particular continuous integration, with a guided hands-on example."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "testing.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 2h.

The prerequisites to take this module are:
 * the [Using git and github](/modules/git_github) module.
 * the [A brief introduction to the bash shell](/modules/introduction_to_terminal) module.

It is highly recommended to also have done the [python script](/modules/python_scripts) module, but that's not strictly necessary.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

## Resources
The [slides](https://drive.google.com/file/d/1M3nr4D0-cPCjHjL23vk-BXth2TqHshtj/view?usp=sharing) are adapted from the original QLSC 612 course in 2020 by [Greg Kiar](https://twitter.com/g_kiar)

The video of the presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/TIPIap8rZyE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Exercise

 * Fork [this repo](https://github.com/school-brainhack/testing_CI_module) for the hands on part.
 * Watch the video, and follow along the hands on material. You will implement the unit tests and the github action to execute the unit test.
 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

 **Bonus and addendum** : During the first part of the video I said we would implement unit tests, an integration test and an installation test. I forgot about the integration test during the hands on so I leave it to you as a bonus exercise, which corresponds to writing a test for the main function, since it integrates the other three functions. For the installation test, this one comes for free with the github action, as the action runs in a virtual machine and has to re-install the dependencies each time. 

## More resources

To learn more about pytest and all the nice things it offers, refer to the [pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html#toc). You can also check tutorials such as [this one](https://www.guru99.com/pytest-tutorial.html) or watch [this PyConDE keynote](https://www.youtube.com/watch?v=CMuSn9cofbI).

<br/>

<span style="font-size:0.8em;">Illustration by <a href="https://www.flaticon.com/authors/nikita-golubev">Nikita Golubev</a>.<span/>
