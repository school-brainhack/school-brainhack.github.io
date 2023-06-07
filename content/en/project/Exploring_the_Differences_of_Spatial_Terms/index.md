---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-07" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Exploring the Differences of Spatial Terms in Chinese and English Language Networks."

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Yu-Hsuan, Lin]

# Your project GitHub repository URL
github_repo: https://github.com/linyu329/Lin_Yu_Hsuan_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [spatial terms, github, fMRI, multilingual]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This project tries to explore the impact of cultural differences on language expression and perception. prior studies found correlations with the pragmatic habits of different cultures. However, existing research on spatial cognition mainly examines differences in language presentation, overlooking more fundamental brain representations. The article aims to fill this gap by analyzing the use of spatial terms in Chinese and English texts and investigating if these linguistic differences are reflected in brain representations."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "CH_up.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->
# **Exploring the Differences of Spatial Terms in Chinese and English Language Networks**
# 不同文化中的語言網路在空間詞中差異探索
### By Lin Yu-Hsuan
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Content</summary>
  <ol>
    <li>
      <a href="#project-description">Project Description</a>
      <ul>
        <li><a href="#background">Background</a></li>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#main-objectives">Main Objectives</a></li>
        <li><a href="#data">Data</a></li>
        <li><a href="#project-deliverables">Project Deliverables</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-start">Getting Start</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#project-tree">Project Tree</a></li>
      </ul>
    </li>
    <li><a href="#results">Results</a></li>
    <li><a href="#conclusions">Conclusions</a></li>
    <li><a href="#future-work">Future Work</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>


# **Project Description**
Cultures difference impact our expression in language, but does it mean our perception was also effected? Researchers have also conducted behavioral studies by grouping participants based on their native language and their first foreign language, and the results is correlated to the pragmatic habits of different cultures.

Unfortunately, current research on spatial differences in cognition mostly focuses on differences in language presentation. Whether these differences are reflected in more fundamental brain representations remains an unexplored territory. Therefore, this article aims to present the differences in the use of spatial terms in Chinese and English texts through text analysis, and further investigate whether these linguistic differences are reflected in brain representations.


## **Background**
Benjamin Lee Whorf, a American linguist, proposed the "Linguistic Relativity Hypothesis" in 1935, attempting to explain whether the rules of language affect our thinking in daily perception of various things. For example, different languages often use spatial terms to aid their understanding of the abstract concept of time. In Chinese, words associated with the front are frequently used to refer to the future, such as "前途"and "前程" (both refer to future prospects). Conversely, words associated with the back are used to refer to the past, such as "背景" (background). English exhibits similar patterns, such as "look forward to" and "background." Therefore, this article takes this as a starting point to explore how spatial terms shape the different perspectives through which humans perceive things in language.

        

## **Introduction**
Previous research has shown that when presented with infrequent stimuli, native speakers of different languages exhibit different prototypes for sounds, which can be observed electrically through the mismatch negativity (MMN) in subjects(Näätänen, et al., 1997). This suggests that different native languages have distinct prototypes for recognizing speech sounds. This information indicates that the human brain's language processing system might have diverse brain representations for the same linguistic phenomenon due to variations in language usage.

Another research on the spatial differences between Chinese and English has found that Chinese often uses vertical concepts to represent temporal sequence (Boroditsky, L. (2008)). For example, expressions like "下一周" (next week, direct translation-lower week) and "上個學期" (previous semester, direct translation-upper semester) embody this characteristic, which is also reflected in the top-to-bottom writing style prevalent in Chinese. Researchers have also conducted behavioral studies by grouping participants based on their native language and their first foreign language. They asked and studied how these participants represent their understanding of time. By asking questions like "If today is here, where is tomorrow?", the researchers identified that native Chinese speakers are more likely than native English speakers to indicate relative positions using vertical arrangements.

Unfortunately, current research on spatial differences in cognition mostly focuses on differences in language presentation. We cannot rule out the possibility that language has not developed alternative ways of expression. Whether these differences are reflected in more fundamental brain representations remains an unexplored territory. Therefore, this article aims to present the differences in the use of spatial terms in Chinese and English texts through text analysis, and further investigate whether these linguistic differences are reflected in brain representations.

## **Main Objectives**
1. &nbsp;&nbsp;✅ Investigate the collocation of various spatial terms using the bilingual text of "The Little Prince."
2. &nbsp;&nbsp;✅ By examining the differences in the frequency of spatial terms to explore the variations in how Chinese and English texts represent space.   
3. &nbsp;&nbsp;✅ Examining the differences in the collocation patterns of spatial terms between Chinese and English.
4. &nbsp;&nbsp;⬜ Matching with the fMRI Brain Database. 

## **Data**
In this research, two main methodologies are involved. Firstly, a case study is conducted using the texts of "The Little Prince" in both Chinese and English versions, aiming to understand whether there are different ways of expressing spatial concepts in these two languages. Secondly, an open brain database available on the internet is utilized to study brain representations, with the goal of investigating whether these spatial expression patterns impact our brain representations.

Based on the "spatial sentence structure" in Chinese, I will use the spatial terms identified in previous research as the basis for this study. These terms include "shang 上 'up', xia 下 'down', qian 前 'in front of', hou 後 'behind', li 裡 'in', nei 內 'in', zhong 中 'in', and wai 外 'outside'" (Chen, 2020).

Furthermore, a publicly available fMRI database on the internet contains an article that uses "The Little Prince" as cross-linguistic data. The study collected fMRI brain scans from 49 English native speakers, 35 Chinese native speakers, and 28 French native speakers while listening to the story of "The Little Prince" (Stehwien et al., 2020).

Based on the content taught in this course, I will attempt to depict the co-occurrence of various spatial terms in different languages and illustrate the corresponding brain activation patterns when these spatial terms are encountered. The source of brain imaging data is open databases within OpenNeuro. The detail of the braindata is well reported in <https://openneuro.org/datasets/ds003643>


## **Project Deliverables**
  ✅ Text collocation scripts & pics\
  ✅ Get fMRI database\
  ✅ Presentation slides\
  ✅ Project report

# **Getting Start**

## **Prerequisites**
You may use Google Colab and no modules should be installed prerequisite.
## **Project Tree**

* Collocation 
  * the_little_prince_ch / _en: The Little Prince corpus
  * Final_CH / _EN : Find collocation words, then plot and analyze
* get_fMRI_data
  * get_CH/EN_fMRI : Download fMRI data from openneuro dataset and calculate and average data then save as a zip file
* analyzing_fMRI_data 
  * fMRI_CH / _EN : Use the merged data acquired from  _get_CH/EN_fMRI_ then perform some analysis
```
├── readme.md
├── analyzing_fMRI_data 
├── Collocation
├── get_fMRI_data
└── Project_final_brainhack.pptx
```
# **Results**
1.Collocation of the context

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_up.png alt="Up" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_down.png alt="Down" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_infrontof.png alt="In Front of" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_behind.png alt="Behind" width="50%" height="100%"/>

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_up.png alt="Up" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_down.png alt="Down" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_infrontof.png alt="In Front of" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_behind.png alt="Behind" width="50%" height="100%"/>

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_in_01.png alt="in_01" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_in_02.png alt="in_02" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_in_03.png alt="in_03" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_outside.png alt="Outside" width="50%" height="100%"/>

Note that 「裡」、「內」、「中」all mean "in" in English

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_in.png alt="in_03" width="50%" height="100%"/><img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_outside.png alt="Outside" width="50%" height="100%"/>

2.Frequency of the spatial term

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/EN_freq_all.png alt="EN_freq" width="100%" height="100%"/>

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/CH_freq_all.png alt="CH_freq" width="100%" height="100%"/>

\
3. Attempt with fMRI data <br>
Below are the 1st ROI region of the average fMRI data of 9 English and Chinese participants applied with atlas masker,
you may find more fMRI analysis attempts in ``analyzing_fMRI_data\fMRI_EN`` and ``analyzing_fMRI_data\fMRI_CH``

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/brain_EN.png alt="EN_brain" width="100%" height="100%"/>

<img src=https://github.com/linyu329/Brainhack_final/blob/main/readme.pics/brain_CH.png alt="CH_brain" width="100%" height="100%"/>

# **Conclusions**
1. Tools I learned from the project
    * Python scripting
    * Use Python to analyze spatial terms in text and corpus.
    * Extract specific data from open brain database.
    * Understand the different categories between languages
   <br>
2. The relationship between various spatial terms
    * Spatial terms in EN version refer to some abstract concepts
    * The same object in different languages have preference in using spatial terms

3. Data analysis of Chinese corpus
    * Should be careful with Chinese segmentation, clean the data manually if needed
4. The connection between literatures, programming, and even neuroscience.
# **Future Work**
* Concern
  * The characteristics of fMRI (t_r=2) are not suitable for studying short-term differences in the brain (the lasting time of a spatial term may be about 0.2 sec)
* Next Steps
  * Find the corresponding spatial terms in the database
  * Compare the differences in brain responses to these spatial terms between Chinese and English language users
* Discussion
  * In order to correspond to the brain database, the accuracy of the co-location plot decrease
  * How to infer results from corpus data to brain data?


# References
1.	Whorf, Benjamin Lee (1956) [1936?]. “An American Indian model of the universe”. In Carroll, J. B. (ed.). Language, Thought, and Reality: Selected Writings of Benjamin Lee Whorf. Cambridge, Massachusetts: Technology Press of Massachusetts Institute of Technology. pp. 57–64.
2.	Boroditsky L., Gaby, A. (2010). “Remembrances of times East: Absolute Spatial Representations of time in an Australian Aboriginal Community.” Sci.
3.	Boroditsky, L. (2008). Do English and Mandarin Speakers think Differently about Time? Proceedings of the 30th annual conference of the cognitive science society. pp. 64-70
4.	Chen, Alvin Cheng-Hsien. "Words, constructions and corpora: Network representations of constructional semantics for Mandarin space particles" Corpus Linguistics and Linguistic Theory, vol. 18, no. 2, 2022, pp. 209-235. https://doi.org/10.1515/cllt-2020-0012
5.	Stehwien, S., Henke, L., Hale, J., Brennan, J., & Meyer, L. (2020, May). The Little Prince in 26 languages: Towards a multilingual neuro-cognitive corpus. In Proceedings of the Second Workshop on Linguistic and Neurocognitive Resources(pp. 43-49).
6.  Näätänen, R., Lehtokoski, A., Lennes, M., Cheour, M., Huotilainen, M., Iivonen, A., ... & Alho, K. (1997). Language-specific phoneme representations revealed by electric and magnetic brain responses. Nature, 385(6615), 432-434.
7.  Thierry, G., Athanasopoulos, P., Wiggett, A., Dering, B., & Kuipers, J. R. (2009). Unconscious effects of language-specific terminology on preattentive color perception. Proceedings of the National Academy of Sciences, 106(11), 4567-4570.
8.  Li, J., Bhattasali, S., Zhang, S., Franzluebbers, B., Luh, W. M., Spreng, R. N., ... & Hale, J. (2021). Le Petit Prince: A multilingual fMRI corpus using ecological stimuli. Biorxiv, 2021-10.

