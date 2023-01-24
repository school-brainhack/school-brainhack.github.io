+++
title = "Project guide"
type = "page"

github_repo = "https://github.com/school-brainhack/school-brainhack.github.io/blob/main/content/en/project/template/index.md"
+++

# Project template

The project template was added in the [BHS gallery](https://school-brainhack.github.io/project/). You can also help improve the template by posting an issue on the [template repo](https://github.com/school-brainhack/project_template). Project repositories are hosted in the Brainhack school 2023[github organization](https://github.com/school-brainhack).

For your project pitch from the week-2 onwards please follow this simple template [here](https://github.com/school-brainhack/project_template) to bring your ideas together. You can either use a Google slides or Jupyter noteook to create your slides.

## Optional New Skill Alert! 
If you would like to use and learn how to create slides with Jupyter notebook, please download the notebook template from [here](https://github.com/school-brainhack/school-brainhack.github.io/blob/main/content/en/project_guide/brainhack_project_presentation_slide_template.ipynb) to your local. Then [install Jupyter notebook](https://jupyter.org/install) Python package if you haven't done so already. 

After the installation run the Jupyter notebook by typing `jupyter notebook` at your terminal. This will open the jupyter notebook envionment at your browser. Then upload the notebook template from your local to the Jupyter environment. 

Now you can click to the book you just uploaded at your browser named as `brainhack_project_presentation_slide_template.ipynb`. This will open the template presentation at the jupyter environment and will give you a chance to edit its cell content as you go along. After you complete the presentation, save the notebook, and download it to your local. 

Finally, in order to convert your notebook to a shiny presentation, open your terminal, go to the directory where the notebook is located and run the following command:

 `jupyter nbconvert 'brainhack_project_presentation_slide_template.ipynb' --to slides --post serve`

 This will create the `.html` file of your published version of your presentation! You are ready to go! 

 The slides are adapted from a [slide deck](https://github.com/brainhack-school2022/dimitrijevic_project/blob/main/project_presentation.ipynb) of one of our 2022 students Andjela Dimitrijevic :tada:


# Adding your project to the gallery

The gallery can be found [here](project). Instructions to push your project to this gallery through a pull request to the [BHS website](https://github.com/school-brainhack/school-brainhack.github.io) are now available! Keep reading:

Last but not least, the final deliverable that will be displayed in the [Project Gallery](https://school-brainhack.github.io/project/). We don't want you to write new stuff, you have done more than enough :raised_hands:. In fact, this page should reflect your final report (aka your README.md).

PS: You don't have to install Hugo to add your document and make the pull request. The file you will have to edit has all the instruction embedded for the two different sections you need to fill in. (e.i, the frontmatter or *header* of the document, and the content section).

This document will guide you through the whole Git/Github workflow that you are probably becoming expert at ;).

- [ ] Fork the BrainHack school website repository @ https://github.com/school-brainhack/school-brainhack.github.io
- [ ] Clone your newly forked repo on your computer.
- [ ] Go in `school/content/en/project/`. Then, copy and paste the `template/` directory in `school/content/en/project/`.
- [ ] Change the name of the `template copy/` directory to a significant one. The name you give to the folder will become the page that your project will be accessible. For example, the`fake` project is accessible at https://school-brainhack.github.io/project/template/. So, make sure to pick a nice and relevant short name ;). PS: if you want more than one word, replace the `space` between words by `-`.
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
