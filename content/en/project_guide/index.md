+++
title = "Project guide"
type = "page"

github_repo = "https://github.com/brainhack-school2022/project_template"
+++

# Project template

The project template was added in the [BHS gallery](https://school.brainhackmtl.org/project/template/). You can also help improve the template by posting an issue on the [template repo](https://github.com/brainhack-school2022/project_template/issues). Project repositories are hosted in the Brainhack school 2022 [github organization](https://github.com/brainhack-school2022).

# Adding your project to the gallery

The gallery can be found [here](project). Instructions to push your project to this gallery through a pull request to the [BHS website](https://github.com/brainhackorg/school) are now available! Keep reading:

Last but not least, the final deliverable that will be displayed in the [Project Gallery](https://school.brainhackmtl.org/project). We don't want you to write new stuff, you have done more than enough :raised_hands:. In fact, this page should reflect your final report (aka your README.md).

PS: You don't have to install Hugo to add your document and make the pull request. The file you will have to edit has all the instruction embedded for the two different sections you need to fill in. (e.i, the frontmatter or *header* of the document, and the content section).

This document will guide you through the whole Git/Github workflow that you are probably becoming expert at ;).

- [ ] Fork the BrainHack school website repository @ https://github.com/BrainhackMTL/school
- [ ] Clone your newly forked repo on your computer.
- [ ] Go in `school/content/en/project/`. Then, copy and paste the `template/` directory in `school/content/en/project/`.
- [ ] Change the name of the `template copy/` directory to a significant one. The name you give to the folder will become the page that your project will be accessible. For example, the`fake` project is accessible at https://school.brainhackmtl.org/project/fake. So, make sure to pick a nice and relevant short name ;). PS: if you want more than one word, replace the `space` between words by `-`.
- [ ] Now you can delete all the pictures and put the ones you want to use for you project.
- [ ] Last but not least, you need to edit the content inside the `your-project/index.md` file. Use the editor you want (e.g., nano, vim, VSC, Atom, etc.) to modify it.
  - [ ] The frontmatter section (header) contains specific parameters and it is really important to follow the format described in the instructions above each line. The frontmatter section is delimited by a `---` at the top and another one at the end of it.
  - [ ] When you edit the `content` section (below the second `---`), you can edit the markdown as you wish. Feel free to embed video, GIF, images, plots, etc.
- [ ] When you are pleased with your report, you can staged your changes after having saved them, commit them, then push them.
- [ ] You will have to go back on forked github repo to make the pull request. You should see a gree button on the right `Create pull request`. The [documentation provided by GitHub](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) is really exhaustive if you have more question.
- [ ] If you everything was done properly, an instructor will merge your pull request and inform you that you are finally done. If some changes need to be made, the instructor will ask you what should be change on you branch. If that happens, you can commit more changes and it will be automatically linked. Simply tag the instructor who reviewed your pull request and you should be finally done :tada:.

Congrats!!


# Project evaluation

You will have to present your project to the class during week 4, and finalize the deliverables of your project. Both the presentation and the written deliverables will be evaluated with the following criteria, using a 3-level scale:

* 1: does not meet expectations
* 2: partially meets expectations
* 3: totally meets expectations

Grades will be given by several instructors and averaged to obtain the
final presentation grade.

## Use of open-science best practices (1-3)

Expectation: the project uses 3 open-science tools learnt during week 1, or
provides a convincing reason to not use them. The 3 tools may be selected
in the following list, but other relevant tools will be accepted too.

* Git
* GitHub
* Containers
* Python
* BIDS
* Jupyter notebooks
* Binder

## Skills and technologies learnt (1-3)

Expectation: the project uses 1 skill, method or technology learnt by the
student during the school, through formal presentations or informal
interactions. The skill, method or technology may be selected in the following list,
but other relevant ones will be accepted too.

* Machine learning
* Multivariate statistics and matrix factorizations
* Estimation of connectivity
* High-performance computing
* DataLad

## Project relevance (1-3)

Expectation: the project is relevant to brain data analysis.

## Clarity (1-3)

Expectation: the presentation is easy to follow, and supported by
convincing material (e.g., slides).

## Bonuses

* Highly reproducible project (0-1)
* Technological achievement (0-1)
* Exciting presentation (0-1)
* Nice brain picture (0-1)
