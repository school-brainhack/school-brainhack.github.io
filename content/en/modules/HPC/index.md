---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "High Performance Computing"

# Your project GitHub repository URL
github_repo: https://github.com/calculquebec/cq-formation-premiers-pas

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [HPC, computecanda, alliancecanada, brainhackcloud]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Introduction to HPC infrastructure and parallel computing, using Alliance Canada (formerly Compute Canada), or Brainhack Cloud."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "alliancecanada_logo.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 4h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

Follow up with your local TA(s) to validate you completed the exercises correctly.

:warning: It should be noted that recently Compute Canada changed its name to Alliance Canada.
That does not change the relevance of the exercises presented here, but it can make some naming conventions outdated.
For example, the documentation website for the clusters is no longer https://docs.computecanada.ca/wiki/Technical_documentation but https://docs.alliancecan.ca/wiki/Technical_documentation. However for now the old URLs redirect to the new ones so using the old names doesn't seem to create issues, but that might not stay true in the long run.

:warning: A notable exception to the name change are the hostnames of the clusters for ssh connections. You still have to use the `.computecanada.ca` domain name. So for example if you want to connect to Beluga, you still need to type :

`ssh <username>@beluga.computecanada.ca`

:warning: :warning: If you reside outside of Canada and don't have access to a local HPC you can apply to access [Brainhack Cloud](https://brainhack.org/brainhack_cloud/). Some detailed steps for connecting to their cloud are available on this [GitHub repository](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/BrainHackCloud_steps/get_connected.md). Subsequently anytime the lecture material below refers to location-specific inputs you will have to adjust your inputs accordingly (e.g. the ssh connection).

### Alliance Canada account

If you are following BrainHack School through a canadian institution, please follow the instructions below to create an account on Alliance Canada. Otherwise, see the :warning: warning above.

To create an Alliance Canada account, you will need a sponsor, likely your PI. If your PI does not already have an account on Alliance Canada, please contact your local TA(s). Otherwise, you will have to follow [this link](https://ccdb.alliancecan.ca/security/login) and click on *Register*. You will then have to fill a form. To make sure you are selecting the proper user role, please check out [this documentation](https://alliancecan.ca/en/services/advanced-research-computing/account-management/user-roles-access-resources-and-services-federation). You will also need to specify your sponsor's account number. Once submitted, you will have to wait for your sponsor to accept your form.


## Resources
This module was presented by [Félix-Antoine Fortin](https://github.com/cmd-ntrf) during the QLSC 612 course in 2020.

The slides are available [here](https://docs.google.com/presentation/d/1toGlTfi4zqavPGHZ9NV3Va7MuT-rmXdv3NHAyQGINdk/edit#slide=id.g3461d16a8f_0_8).

The video of his presentation is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/J9VCHe1ovBg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

 * Download the tutorial zip file :
 ```
 wget https://raw.githubusercontent.com/brainhackorg/school/master/content/en/modules/HPC/cq-formation-premiers-pas-slurmcloud.zip
 ```
 * Copy the file to the beluga cluster :
 ```
 scp cq-formation-premiers-pas-slurmcloud.zip <username>@beluga.computecanada.ca:
 ```
 *Note*: You could have directly downloaded the file from the beluga cluster, but being familiar with the scp command is very useful.
 * Connect to the beluga cluster :
 ```
 ssh <username>@beluga.computecanada.ca
 ```
 * Unzip the tutorial zip file :
 ```
 unzip cq-formation-premiers-pas-slurmcloud.zip
 ```
 * You can remove the zip file :
 ```
 rm cq-formation-premiers-pas-slurmcloud.zip
 ```
 * Do the exercises in the `cq-formation-premiers-pas-slurmcloud` folder, you can see the original instructions in the README files, for example :
 ```
 cd cq-formation-premiers-pas-slurmcloud/1-base
 cat README.en
 ```
 Updated instructions can also be seen here, with slightly more detailed explanations :

 {{< tabs tabTotal="6" tabID="instructions" tabName1="0-setting-up" tabName2="1-base" tabName3="2-sequentielles" tabName4="3-gnu-parallel" tabName5="4-lot-de-taches" tabName6="5-tache-mpi" >}}
 {{< tab tabNum="1" >}} {{% content "content/en/modules/HPC/0-setting-up.md" %}} {{< /tab >}}
 {{< tab tabNum="2" >}} {{% content "content/en/modules/HPC/1-base.md" %}} {{< /tab >}}
 {{< tab tabNum="3" >}} {{% content "content/en/modules/HPC/2-sequentielles.md" %}} {{< /tab >}}
 {{< tab tabNum="4" >}} {{% content "content/en/modules/HPC/3-gnu-parallel.md" %}} {{< /tab >}}
 {{< tab tabNum="5" >}} {{% content "content/en/modules/HPC/4-lot-de-taches.md" %}} {{< /tab >}}
 {{< tab tabNum="6" >}} {{% content "content/en/modules/HPC/5-tache-mpi.md" %}} {{< /tab >}}
 {{< /tabs >}}


 <br>

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

## More resources

The [Alliance Canada wiki](https://docs.alliancecan.ca/wiki/Technical_documentation) is a great source of tutorials, advice and good practices. Be sure to head there first before asking the staff for help. You can also ask the instructors in the BrainHack school discord.
