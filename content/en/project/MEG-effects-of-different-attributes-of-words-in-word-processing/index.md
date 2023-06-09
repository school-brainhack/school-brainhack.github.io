---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-07" # Date you first upload your project.
# Title of your project (we like creative title)
title: "The Effects of Word Frequency, Orthographic Neighborhood and Part of Speech in Word Processing: A MEG Study"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Ruo-Chi Yao]

# Your project GitHub repository URL
github_repo: https://github.com/Ruo-Chi/Ruo-Chi-Yao_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [meg, github, mne, python]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Word processing is influenced by different attributes of words, which can be observed vis brain imaging techniques such as MEG. Let's find evidence of the influence of word attributes by analyzing a dataset."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background

Word processing is influenced by different attributes of words, which can be observed vis brain imaging techniques such as MEG. This project focuses on attributes of words, including word frequency, orthographic neighborhood, and part of speech.
- In word processing, high-frequency words are handled more easily and quickly than low-frequency words.
- An orthographic neighborhood refers to words that are similar to a target word by differing in only one letter (addition, deletion, or substitution of a single letter).
- Part of speech refers to the grammatical category or class that a word belongs to.

We have all learned and understood that various attributes of words impact word processing, whether from textbooks or lectures. However, many of us may not have had the opportunity to obtain evidence regarding this ourselves. The main question here is whether I can find evidence of the influence of word attributes by analyzing a dataset. Therefore, the primary question here is whether I can find evidence of the influence of word attributes by analyzing a dataset.

### Tools

The dataset processing by useing mne-python

### Methods

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/methods.png)

- Read & load raw data

 ![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Read%20%26%20Load%20raw%20data.png)
 
- Filter & down sample

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Filter%20%26%20Down%20sample.png)

- Find event id

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Find%20event%20id.png)

- Do artifact rejection & slice the data into epochs

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Do%20artifact%20rejection%20%26%20slice%20the%20data%20into%20epochs.png)

- Working with epoch metadata & visualizing evoked data

![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Working%20with%20Epoch%20metadata%20%26%20Visualizing%20Evoked%20data.png)


### Data

Dataset: [Auditory single word recognition in MEG – OpenNeuro](https://openneuro.org/datasets/ds004276/versions/1.0.0)
- There are files for 18 subjects, but 12 of them can be download successfully.
- 1000 trials for one subject, that is each subject listens to 1000 words.
- There are 97 extra words specifically for semantic probe tasks that involve go/no-go trials.
- Data are recorded using MEG.


### Deliverables

At the end of this project, we will have:
 - A GitHub repository.
 - A markdown document.
 - MEG data analysis with MNE-Python.

## Results

### Frequency effects
![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Results_Frequency%20effects.png)

### Orthographic neighborhood
![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Results_Orthographic%20neighborhood.png)

### Part of speech
![alt text](https://github.com/Ruo-Chi/Ruo-Chi-Yao_project/blob/main/images/Results_Part%20of%20speech.png)

## Conclusion

### Frequency effects
- the effect can be seen from 0ms to 200ms and 450ms to 600 ms time window
- in consistence with the result that word frequency effects become stronger and more widespread from 200ms to 300ms and 400ms to 500ms respectively (Dufau et al., 2015)

### Orthographic neighborhood
- the effect can be seen after 300ms time window
- in consistence with the result that the effects of  orthographic neighborhood size emerge around 280 ms (Dufau et al., 2015)

### Part of speech
- the effect can be seen after 250 ms time window
- in consistence with the result that verbs are more negative than nouns about 300 and 1,000 ms (Rösler et al., 2001)

## References
- Brysbaert, M., Mandera, P., & Keuleers, E. (2018). The word frequency effect in word processing: An updated review. Current Directions in Psychological Science, 27(1), 45-50.
- Dufau, S., Grainger, J., Midgley, K. J., & Holcomb, P. J. (2015). A thousand words are worth a picture: Snapshots of printed-word processing in an event-related potential megastudy. Psychological science, 26(12), 1887-1897.
- Gaston, P., Brodbeck, C., Phillips, C., & Lau, E. (2023). Auditory word comprehension is less incremental in isolated words. Neurobiology of Language, 4(1), 29-52.
- Marian, V., Bartolotti, J., Chabal, S., & Shook, A. (2012). CLEARPOND: Cross-linguistic easy-access resource for phonological and orthographic neighborhood densities.
- Rösler, F., Streb, J., & Haan, H. (2001). Event-related brain potentials evoked by verbs and nouns in a primed lexical decision task. Psychophysiology, 38(4), 694-703.





