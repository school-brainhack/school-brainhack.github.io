+++
title = "Setup"
type = "setup"
+++

## General computing requirements

There are a few computing requirements for the course that are absolutely necessary (beyond the few software packages we would like you to install, described below):

1. You must have administrator access to your computer (i.e., you must be able to install things yourself without requesting IT approval).
1. You must have at least 40 GB of free disk space on your computer (but we would recommend more, to be safe).
1. If you are using Windows you must be using Windows 10; Windows 7 and 8 will not be sufficient for this course.

If you foresee any of these being a problem please reach out to one of the instructors for what steps you can take to ensure you are ready for the course start on May 11th.

## Required software

To get the most out of our course, we ask that you arrive with the following software already installed:

- A command-line shell: Bash
- A version control system: Git
- A remote-capable text editor: VSCode
- Python 3 via Miniconda
- A virtualization system: Docker
- A GitHub account
- Slack
- Zoom
- A modern browser

If you already have all of the above software tools/packages installed, or are confident you’ll be able to install them by the time the course starts, you can jump straight to [checking your install](#checking-your-install).
The rest of this page provides more detail on installation procedures for each of the above elements, with separate instructions for each of the three major operating systems (Windows, Mac OS, and Linux).

### Some quick general notes on instructions

- There is no difference between `Enter` and `Return` in these instructions, so just press whatever the equivalent on your keyboard is whenever one is stated
- If you already have some of these things installed on your computer already that should (theoretically) be okay.
  However, you need to make sure that you are able to complete the steps described in [checking your install](#checking-your-install) without issue.
  - For example, having multiple different Python installations on your computer can lead to incredibly frustrating issues that are very difficult to debug.
    As such, if you have already installed Python via some other application (not Miniconda/Anaconda), we strongly encourage you to uninstall it before following the instructions below.
    You _must_ have Python installed via Miniconda for this course.

### OS-specific installation instructions

Select the tab that corresponds to your operating system and follow the instructions therein.

**Note**: If the instructions below aren't working and you have spent more than 15-20 minutes troubleshooting on your own, reach out on the #help-installation channel on the BHS Slack with the exact problems you're having.
One of the instructors will try and get back to you quickly to help resolve the situation.
If they're unable to help via Slack, you may be directed to attend one of the installation office hours during the week of 4-8 May.

{{< tabs tabTotal="3" tabID="setup" tabName1="Windows" tabName2="Mac OS" tabName3="Linux" >}}
{{< tab tabNum="1" >}} {{% content "setup/windows.md" %}} {{< /tab >}}
{{< tab tabNum="2" >}} {{% content "setup/mac.md" %}} {{< /tab >}}
{{< tab tabNum="3" >}} {{% content "setup/linux.md" %}} {{< /tab >}}
{{< /tabs >}}

### GitHub account

Go to https://github.com/join/ and follow the on-screen instructions to create an account.
It is a good idea to associate this with your university e-mail (if you have one) as this will entitle you to sign up for the [GitHub Student Developer Pack](https://education.github.com/pack) which comes with some nice free bonuses.

### Slack

Go to https://slack.com/downloads/ and download and install Slack.
You will be invited to the BrainHack School Slack channel via the e-mail with which you registered for the course.

### Zoom

Go to https://zoom.us/download and download and install the Zoom client.

### Modern web browser

Install Firefox or Chrome.
(Safari will also work.)
Microsoft Edge is not modern, despite what Microsoft might try and otherwise tell you.

## Checking your install

Now that you've installed everything it's time to check that everything works as expected!
Type the following into your terminal:

``` bash
bash <( curl -s https://neurodatasci-course-2020.netlify.app/resources/nds_check_install.sh )
```

If you installed everything correctly you should see a message informing you as such.
If any problems were detected you should receive some brief instructions on what is wrong with potential suggestions on how to remedy it.
If you followed these instructions step-by-step and cannot resolve the issue please contact one of the course instructors for more help.
