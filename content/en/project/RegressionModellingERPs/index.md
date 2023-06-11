# Regression-Modelling ERPs (and More!)
## Background
<img src="https://github.com/amandalin047/Amanda_BrainHack_2023/blob/master/inline_img/binned_results.png" alt="Grand Average ERPs" width="900" height="400">
Emotion perception is contextualized. However, how emotional context modulates word processing is unclear. We tested 20 young native speakers who read 208 Taiwan Mandarin sentences with varied emotionality conveyed through the context. To deal with multiple covarying factors in natural language, we adopted a regression-based rERP method to titrate the contextual effects. Moreover, as we plan on conducting a subsequent experiment to follow up on the findings the present study has revealed, this project also includes the code for constructing experimental stimuli.

## Tools
This project has implemented the following programming languages and brain imaging techniques:
- EEG/ERP
- Python 
- Matlab
- JavaScript

## Data
- **EEG Analyses**: A 20-subject language experiment EEG dataset collected by a lab senior several years ago. (_The data files on this repository are currently blank dummy files._) Besides planning on adding 10 more participants to the original and recruiting 30 young adults for the following-up experiment, my advisor (Dr. Charlene Lee) and I also aim to ultimately put our lab data in BIDS.
- **Stimuli Construction**: Participant Gmails and Excel sheets sent as attachments.

## Deliverables
- This markdown README documenting the project
- Multiple Jupyter Notenooks (.ipynb), which also have the results clearly illustrated with nice data visualization
- Python scripts (.py)
- A Google Apps Script (.gs)


# Results
## Progress Overview
- **EEG Analyses**
    + The main structure of the regression models was completed during winter break (January through February), following Brouwer et al.'s 2020 method along with advice suggested by Dr. Kevin Hsu. However, rather than performing repeated-measures ANOVAs on the regression fitted values as was done by Brouwer et al., I t-tested each regression coefficient against 0 for concerns about systematic and statistically significant conditional differences among the predictors (in regression terms, everything in the predictors shows up as linear combinations in the fitted values, thus causing confounds).
    + The problem of multiple comparisons was tackled around March after a brief discussion with Dr. Joshua Goh. The Bonferonni correction was, as I realized, stringently unrealistic in the case where each (channel x time point) cell is regressed separately, rendering the statistical resulst less susceptible to individual Type I errors. I later settled (for the mean time) with the BH-procedure, but am still looking into cluster-based correction methods to better take into account the spatial relationships between 3D-configurated scalp channels.
    + Two sessions in April with Prof. Kara Federmeier from the University of Illinois Urbana-Champaign pointed me towards a new direction, namely to group the regression coefficients into spatiotemperal ROIs, which largely reduced the number of multiple comparisons for which I needed to correct.
    + The class attributes and methods in the program were substantially modified and revised soon after to improve run-time efficiency due to issues related to automatically dying Jupyter kernels in WSL2.
    + The EEG Toolbox under Matlab differs from MNE-Python in many respects. Having been initially trained in Matlab, I aspire to create Python functions with which Matlab users will feel more familiar, such as bin descriptor text files and the moving-window peak-to-peak method for artifact detection. To this aim, other EEG-related Python notebooks/scripts included in this repository were subsequently developed in late April through May.
<p>&nbsp</p><img src="https://github.com/amandalin047/Amanda_BrainHack_2023/blob/master/inline_img/rerp_coef.png" alt="rERP Coefficients" width="700" height="700">

- **Stimuli Construction**
    + I started developing the Python code for compiling ratings Excel sheets roughly around March.
    + A massive round of ratings was carried out in April, thus calling for a means to automatically label, upload, and reply to incoming participant emails.
<p>&nbsp</p><img src="https://github.com/amandalin047/Amanda_BrainHack_2023/blob/master/inline_img/apps_script.png" alt="Google Apps Script" width="700" height="300">

## Skillsets Learned
- **MNE-Python**: As a math undergraduate, I was initially trained in C++ and never formally took Python (I could read and code in Python as languages that support OOP share some similarities, yet I was far from proficient). It was not easy-peasy to start a Python program from scratch with the limited syntax I knew at the time; I'd spent countless hours Googling, sifting through threads on GitHub and Stack Overflow. As such, I genuinely find amazing how much I've leanred and matured this semester in terms of Python programming skills, not only through my own project, but also as a TA working with the students.
- **Statistical Models**: Statistics was _not_ a required undergraduate course in the Department of Mathematics (basic probablity theory was, though). I only took introductory stats as an elective, so I had but a vague idea of statistical modelling when I started off with this project. Yet as hands-on experiences often are great ways to learn, I've been implementing models I never knew before, and I do look forward to trying out different, more complicated ones.
- **JavaScript**: I really went from zero on this. The immediate need for an automated Gmail gave me an miraculous adreneline boost and had me picking up the language in several hours — not sure how I did it, but I'm glad it worked!


## Results
- **EEG Analyses**
    + A widespread effect of contextual valence from 250ms to 750ms, with words following emotional contexts showing more positive responses relative to words in neutral contexts.
    + Greater implausibility elicited more negative and then more positive responses during 250-500ms and 600-1000ms, respectively, over central-posterior regions, which well-replicated the past ERP literature on the N400 plausibility effect and thus provided justification for our regression model. Further, this plausibility effect was not modulated by context valence, suggesting no evidence for the Affective Primacy hypothesis in sentence comprehension where one would've expected a significant interaction between the two.    
    + A frontally distributed effect of word emotionality during 400ms to 700ms.
    + These findings showed that linguistic emotional context modulates subsequent word processing over and beyond sentence constraint and word emotionality, corroborating robust contextualized emotion processing in reading.
- **Stimui Construction**
    + A great learning oppurtunity as we've come to realize which response collection methods are more efficient (and less tedious). 
    + A nice, albeit still under construction, pipeline for collecting and sorting ratings responses.


## Conclusion and Acknowledgements
This has been an incredible journey in myriad ways, both academically and personally. I would like to give the biggest, most heartfelt thanks to my amazing thesis advisor, Dr. Charlene Lee at the Graduate Institue of Linguistics, National Taiwan University, without whom none of this would have been possible. I am deeply grateful not only for her sound advice, incredible support, but also for the faith she had in me when I struggled with self-doubts and didn't believe I was capable of carrying out this project or taking on this TA position. Having graded 82 module exercises, I must say I really do find reading people's code interesting. I sincerely appreciate all the students who have discussed with me their projects and code on Discord — those were the moments when I got to learn the most. There are many directions in which this project can be expanded and imporved, all of which I look forward to.
