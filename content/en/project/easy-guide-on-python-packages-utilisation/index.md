---
type: "project" # DON'T TOUCH THIS ! :)
date: "2022-07-05" # Date you first upload your project.
# Title of your project (we like creative title)
title: "An easy guide to "\not throwing your expensive computer out the window because you can't run a Python neuroimaging tool\""

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Claudéric DeRoy]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2022/deroy_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [python, scripting, packaging, replicability]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "The goal of this project was to learn how to create code that would be easy to use for unexperienced users but also to be as more open as possible while also being replicable. So I took a code already written and scripted it, packaged it, made a Docker container for it, and finally created a guide on how to use it."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "python_code.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

# Project definition

## Personnal Background
Hello there! My name is Claudéric DeRoy. I have completed a Bachelor in Cognitive Neuroscience at Université de Montréal and also a part of a Bachelor degree in Computer Science, also at Université de Montréal. I am actually a master student in psychology in the NeCS lab under the supervision of Professor Sébastien Hétu. I essential study some computer programmes and pipelines for preprocessing electrodermal activity (EDA) to propose guidelines on how to signal process EDA to the scientific community.


## Project Background
The more theoretical background is from another [project](https://github.com/brainhack-school2022/Lajoie_project/blob/main/project_description.md) of the Brainhack School 2022. The background for this project is more of a practical one. Essentially, computer programmes or computer analysis pipelines for neuroimaging are quite common and can be pretty intimidating for people who are not used to programming in general, which corresponds to a lot of undergrad and graduate students in psychology. Fortunately, there are many tools that can make the installation of libraries, modules, virtual environments and the rest easier or at least less painful. This also helps on another level of research. In 2012, Gronenschild et al. obtained a difference in percentage of volume and cortical thickness using FreeSurfer on both a Macintosh and a Hewlett-Packard machine but also between two different versions of Mac OSX (OSX 10.5 and OSX 10.6). This demonstrates the importance of packaging and containerized programmes so that scripts  are always run in the same environment, but also making those containers available so that the scientific community can use the same tools in the same environment, helping rule out the difference between software as a cause for reproducible failure.


## Objectives/Goals
The main goals of this project are to familiarise myself with scripting, packaging Python code, making Python scripts run more easily on high performance computers (HPC) for the average user, and containeraizing the whole thing. This will help make it easy for inexperienced users to get everything from my Github repository and execute the script either on HPC or their personal machine. So the main goals are : 
- Take the existing Python code for the seed to voxel correlation and make a script that will make it easy to run from the terminal.
- Do the same thing but for the machine learning algorithm that will use the seed to voxel correlation to classify.
- Use Git and Github to create version control of all the scripts.
- Getting familiar with HPC, especially Calcul Canada (Alliance), using Singularity with Docker image or file to use them on Calcul Canada.
- Containerize everything at the end so that the entire project can be easily installed on any computer or HPC.
- Make an easy-to-use guide so people with little to no knowledge of computer science would be able to use and deploy the Docker container or execute the script.


## Tools used
- Python
- Git/Github
- Script and packaging with Python
- Bash
- HPC (Calcul Canada or Brainhack ORACLE)


## Data
I won't work with data, per se but more with code. However, I will use the other [project](https://github.com/brainhack-school2022/Lajoie_project/blob/main/project_description.md) data to make sure everything works correctly.


## Deliverables
I want to produce by the end of the project :
- The script, packaging, and containerization of at least the seed to voxel correlation code.
- In the best case scenario, I will do the same for the machine learning code.
- Some sort of tutorial (either a markdown file or a video) to explain to someone who has no background in computer science how to install everything and run the code.


# Results
I do not have results in the more general term. As previously stated, my goal is to make an existing code more accessible, easy to use, open and replicatable. So, I will lay out what I accomplished in terms of these goals.

## Accessibility
I packaged everything I produced during this project. There are four important files : the `script.py`, `batch.json`, `seed_voxel.py` and `Dockerfile`. They are part of the packaging I did, which is available on TestPyPi (https://test.pypi.org/project/seed-to-voxel-neurok8050/). So, it is more accessible because anybody can install the package with a simple `pip install` (see the [`guide.md`](https://github.com/brainhack-school2022/deroy_project/blob/main/guide.md) for a full installation explication).

## Ease of use
The idea was to make the code as easy to use as possible. Often, when you have access to code that a researcher has used for a paper and you want to use it and have access to it, it is somewhat of a daunting task; you do not really know where to start or what to modify, because everything is "baked" into the code itself (variables, values, etc.). So my original idea was to use a `.txt` with all thes variables names and their values, so that the script could just parse it and plug the variables into the right places. The user would just have to modify the `.txt` file and would not have to play around in the source code (although he is more than welcome to do so). It turns out that `.txt` are not suited for such a task, but `.json` file are perfect for this purpose. That is where the `batch.json` comes from. Finally, when the user wants to run the `script.py` he only has to pass one argument (the `.json` file) instead of 20.

## Openness
This is fairly simple, everything is accessible on my GitHub repository. So feel absolutely free to `git clone` my repository and have fun with it. I really do not mind. Have fun and make it yours, that is the joy of programming.

## Replicability
Creating a Docker container (actually writing a Dockerfile) will help (in my humble opinion) to run the code more replicable. Like I said above, Gronenschild et al. (2012) have shown a certain degree of variability between different versions of the same OS and also between different versions of the same software. Using a Docker container constrains the version of software used during the execution of the code. This version constraint will be the same for every user that runs the code inside the Docker container. But also, in each run, the same user will technically have the same software version each time, thus ruling out the software as a potential point of source failure for replicated study.
Also, the `.json` also helps for replicability. For example, if I run the code with an edited version of the `batch.json` by me, I can publish the article with my edited `batch.json` so that any researcher who is trying to replicate my finding will only have to run the code with the `batch.json` I provided in my article.


## The tools I learned and used for this project

- Scripting in Python (shebang is the rule)
- Packaging Python code (setup.py, pyproject.toml) and uploading it to TestPyPi
- Docker container (This was by far the most difficult thing)
- High performance computer (I wanted to use Singularity to make the Docker container work on Compute Canada, but didn't have time to do it)

# Conclusion

To conclude, I managed to complete most of my objectives. Now I want to focus on deploying it and seeing if the users are capable of using the package, and make changes depending on the user experience with it. I did not package the machine learning algorithm part, but it is part of the next steps I want to take with this project, alongside adding the Singularity part for a good integration of the Dockerfile to HPC. I am really pleased with what I learned during Brainhack school. I have sort of a template for scripting, packaging, and containerizing all of my future projects. 

## Reference
Gronenschild, E. H. B. M., Habets, P., Jacobs, H. I. L., Mengelers, R., Rozendaal, N., van Os, J., & Marcelis, M. (2012). The Effects of FreeSurfer Version, Workstation Type, and Macintosh Operating System Version on Anatomical Volume and Cortical Thickness Measurements. PLoS ONE, 7(6), e38234. https://doi.org/10.1371/journal.pone.0038234
