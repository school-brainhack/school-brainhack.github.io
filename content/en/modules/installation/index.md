---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Installation"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [install, setup]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Instructions to install and setup all the tools required for the BrainHack summer school."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "installation.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## General computing requirements

There are a few computing requirements for the course that are absolutely necessary (beyond the few software packages we would like you to install, described below):
 1. You must have administrator access to your computer (i.e., you must be able to install things yourself without requesting IT approval).
 1. You must have at least 40 GB of free disk space on your computer (but we would recommend more, to be safe).
 1. If you are using Windows you must be using Windows 10 or 11; Windows 7 and 8 will not be sufficient for this course.

If you foresee any of these being a problem please reach out to one of the instructors for what steps you can take to ensure you are ready for the course.

## Required software
To get the most out of our course, we ask you to install the following software:
* A command-line shell: Bash
* A version control system: Git
* A remote-capable text editor: VSCode
* Python 3 via Miniconda
* A virtualization system: Docker
* A GitHub account
* Discord
* A modern browser

**Note** Miniconda and VSCode are not strictly required, if you already have python and prefer to use pip, or if you already have a favorite text editor for programming, feel free to use that instead.

If you already have all of the above software tools/packages installed, or are confident you’ll be able to install them by the time the course starts, you can jump straight to [checking your install](#checking-your-install). The rest of this page provides more detail on installation procedures for each of the above elements, with separate instructions for each of the three major operating systems (Windows, Mac OS, and Linux).

## OS-specific installation instructions

Select the tab that corresponds to your operating system and follow the instructions therein.

Note: If the instructions below aren't working and you have spent more than 15-20 minutes troubleshooting on your own, reach out on the `#help-installation` channel on the BHS Discord with the exact problems you're having.

{{< tabs tabTotal="3" tabID="setup" tabName1="Windows" tabName2="Mac OS" tabName3="Linux" >}}
{{< tab tabNum="1" >}} {{% content "content/en/modules/installation/windows.md" %}} {{< /tab >}}
{{< tab tabNum="2" >}} {{% content "content/en/modules/installation/mac.md" %}} {{< /tab >}}
{{< tab tabNum="3" >}} {{% content "content/en/modules/installation/linux.md" %}} {{< /tab >}}
{{< /tabs >}}

### GitHub account

Go to https://github.com/join/ and follow the on-screen instructions to create an account.
It is a good idea to associate this with your university e-mail (if you have one) as this will entitle you to sign up for the [GitHub Student Developer Pack](https://education.github.com/pack) which comes with some nice free bonuses.

### Discord

Go to https://discord.com/download and download and install Discord.
You will be invited to the BrainHack School Discord server via the e-mail with which you registered for the course. If you have not received the invitation, please reach out to one of the instructors.

### Modern web browser

Install Firefox or Chrome.
(Safari will also work.)
Microsoft Edge is not modern, despite what Microsoft might try and otherwise tell you.

## Checking your install

Now that you've installed everything it's time to check that everything works as expected!
Type the following into your terminal:

``` bash
bash <( curl -s https://raw.githubusercontent.com/brainhackorg/school/master/content/en/modules/installation/nds_check_install.sh )
```

If you installed everything correctly you should see a message informing you as such.
If any problems were detected you should receive some brief instructions on what is wrong with potential suggestions on how to remedy it.
If you followed these instructions step-by-step and cannot resolve the issue please post in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com..
