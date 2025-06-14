---
type: "project" # DON'T TOUCH THIS ! :)
date: "2024-06-21" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Fine-Tuning a Video Large Language Model (Vid-LLM) for Automatic Annotation of Gameplay"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Vincent Chamberland, Renaud Dagenais]

# Your project GitHub repository URL
github_repo: https://github.com/vchamberland/VidGame-LLM

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [video LLM, automatic annotation, video games, cognitive neuroscience]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project aims to develop a preprocessing pipeline to fine-tune a Video Large Language Model (Vid-LLM) for automatic annotation of gameplay recordings in cognitive neuroscience studies. Leveraging the Gym Retro ecosystem and the Courtois NeuroMod dataset, we convert event logs into video format and generate detailed annotations and timestamps to train the Vid-LLM. Deliverables include cleaned datasets, documentations and Jupyter notebooks."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "sub-01_ses-003_task-shinobi_run-01_level-1_rep-01_end_frame.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Video games provide a controlled and rich environment to observe and modulate human behavior, and have been used in various research fields, such as cognitive neuroscience, psychology, and human-computer interaction. However, analyzing gameplay recordings can be time-consuming and labor-intensive, as it often requires manual annotation of player actions and events, which can be error-prone, subjective, and challenging to scale, especially when dealing with large datasets or complex game dynamics ([Harel et al., 2023](https://osf.io/preprints/psyarxiv/uakq9)).

Recently, a growing number of large language models (LLMs) have been specialized for video understanding (Vid-LLMs), where they can generate detailed descriptions of video content, such as actions, objects, and events ([Tang et al., 2023](https://arxiv.org/abs/2312.17432)). These models can be fine-tuned on specific tasks to improve their performance and adapt them to new domains. For example, a model fine-tuned with sports videos can be used to analyze player performance, develop gameplay strategies, and provide detailed commentary. 

### Aims
Therefore, this project aims to develop a preprocessing pipeline to fine-tune a Vid-LLM for automatic annotation of gameplay recordings in order to reduce manual annotation and increase efficiency.

### Brainhack objectives
1. Gain experience with the Gym Retro ecosystem and its Python API for video game analysis
2. Gain experience in manipulation of video data (e.g., conversion, extraction, and processing) 
3. Gain experience with project and version management tools (e.g., Git, DataLad)
4. Gain experience in Python scripting (e.g., dataframes, computer vision, automation)
5. Gain experience with LLM training and testing using video data

### Dataset
The dataset is provided by the [Courtois NeuroMod project](https://www.cneuromod.ca/). It includes behavioral data recorded during gameplay of the retro video game "Shinobi III - Return of the Ninja Master", specifically capturing the movements and actions taken by three subjects. Each subject participated in four gaming sessions, with each session consisting of approximately a dozen runs. For the purposes of this project, we will focus on a subset of this dataset: analyzing runs from a single participant, specifically those in which they played level 1 of Shinobi [i.e., 89 runs].

### Tools

- Python scripting tools & packages
    - Jupyter notebooks
    - Gym Retro’s Python API (RetroEnv)
    - Dataframe handling (e.g., pandas, numpy) 
    - Computer vision (e.g., OpenCV, moviepy)
    - Machine Learning requirements for the Vid-LLM model (pytorch, CUDA, etc.,)
- Project management & versioning
    - Version controlling (Git, Github, Datalad)

## Deliverables (Week 4 results)
- Cleaned-up event dataset (```data/datasets```)
- Formatted question-answers json file for supervised fine-tuning of the Vid-LLM (```data/json_files/custom.json```)
- Jupyter notebooks for data preprocessing and exploration:
    - Dataset cleaning (```notebooks/dataset_preprocessing.ipynb```)
    - Generating training videos from all Gym Retro's bk2 files (```notebooks/training_video_generator.ipynb```)
    - Generating custom question-answers json file (```notebooks/custom_jason_generator.ipynb```)
    - Generating short testing videos (```notebooks/testing_video_generator.ipynb```)
    - Generating a single short testing video (```notebooks/single_testing_video_generator.ipynb```)
    - Generating specific frames and gifs from selected videos (```notebooks/frame_gif_generator.ipynb```)
    - Finding specific frames in a video (```notebooks/frame_finder.ipynb```)
- Documentation on the notebooks (```doc/notebook_doc.md```)
- Detailed documentation on how to download the raw dataset (```doc/how-to-download-raw-data.md```)
- Examples of training and testing videos, frames and gifs (```output/```)
- requirements.txt file for the project (```requirements.txt```)

## Collaborators
* The Pierre/Lune Bellec Lab
* The Courtois NeuroMod Project

## References
- Harel, Y., Pinsard, B., Boyle, J. A., Cyr, A., Clei, M. L., Mignot, P.-H., St-Laurent, M., Jerbi, K. and Bellec, P. (2023). Gamer in the scanner : Event-related analysis of fMRI activity during retro videogame play guided by automated annotations of game content. https://doi.org/10.31234/osf.io/uakq9
- Tang, Y., Bi, J., Xu, S., Song, L., Liang, S., Wang, T., Zhang, D., An, J., Lin, J., Zhu, R., Vosoughi, A., Huang, C., Zhang, Z., Zheng, F., Zhang, J., Luo, P., Luo, J. and Xu, C. (2023). Video Understanding with Large Language Models: A Survey. arXiv. https://doi.org/10.48550/arxiv.2312.17432