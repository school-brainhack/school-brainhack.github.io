type: "project" # DON'T TOUCH THIS ! :) date: "2020-05-16" # Date you first upload your project.

**Mechanism of delusion and hallucination in schizophrenia based on the quadripartite model
[MengHuaKuo]**

**Your project GitHub repository URL**
github_repo: https://github.com/PSY6983-2021/project_template

List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the github repository, click manage topics.
Please only lowercase letters
**tags:** [res-fMRI, schizophrenia, hallucinations, delusions]

**Summarize**
A total of 341 HC and 213 SCZ patients were recruited in this study. Ensemble empirical mode decomposition was employed to decompose voxel-wised resting-state functional Magnetic Resonance Imaging (rs-fMRI) data into intrinsic mode functions (IMFs) within regions according to the quadripartite model. We trained multiple classifiers with the various features extracting from the IMFs, including instantaneous frequency, amplitude, and phase, as well as mean frequency, amplitude, standard deviation and sample entropy of rs-fMRI data.

**Background**
Delusion and hallucination are common symptoms in schizophrenia (SCZ). Despite of different constructs composed with, false belief and false perception still share some similar features to an extent. For instance, they are both characterized by the breakdown of corollary discharge, deficit of monitoring control, and aberrant salience function. Several researches also demonstrated collaborative neural underpinning regarding delusions and hallucinations. The intrinsic networks based on the triple network theory such as salience network (SAL), default mode network (DMN) and central executive network (CEN) are recruited during delusional or hallucinatory phenomena, reflecting some brain modules might be overlapped when the symptoms arise. A quadripartite model, which supports most of current evidences and provides a storyline trying to explain the process during hallucinations, might also be interpretable for delusions due to its involvement of the aforementioned triple network and hippocampus. Nonetheless, it still falls shorts of explaining the underlying mechanisms of both hallucination and delusion. Moreover, the precise prediction of these two symptoms is not yet completed nowadays. We hypothesize that the crucial differences between delusions and hallucinations might provide as key components for machine-learning techniques to distinguish delusional or hallucinatory phenomena.

**Tools**
The "project template" project will rely on the following technologies:
fMRI
Python
Matlab
Data
In this study, ensemble empirical mode decomposition (EEMD) was employed on voxel-wised resting-state functional Magnetic Resonance Imaging (rs-fMRI) data with regions of interest (ROI) according to the quadripartite model. We then trained multiple classifiers with the extracting features from the intrinsic model functions (IMFs) in order to figure out the discrepancy of delusions and hallucinations among brain works for future analysis.

**Deliverables**
At the end of this project, we will have:

Whether the absence of disease, delusion or hallucination could be predicted by machine-learning approaches
What fueatures are appropriate for predicting each target
Results
Only analysis for ROI of hippocampus is currently completed. It is showed that whether one has schizophrenia or not could only be predicted by instantaneous amplitude and instantaneous frequency. NaiveBayes model has best performance for discriminateing delusion and hallucination with original and IMF2 singal respecitively. image

**I learned during this project**
Python: Most of the scripts were run in Python and lots of new functions were learned during the process, expecially regarding machine learning techniques and statistical analysis.
MatLab: EEMD process was done by MatLab HHT & EEMD function in R20222b.
Github workflow: I am zeoro from the Github thing and somehow many challenges occured when I tried to aplly it. Due to it's a widely-used platform to share eveyone's contribution and knowledge, I am trying to improve my ability on this.
VS code: VS code helps me a lot when I tried run both jupyter notebooks to debug and pure python scripts, saving a lot of time switching between multiple screens.

**Results**
In hippocampus, the detection of SCZ could be well predicted via original voxel-based rs-fMRI signal of instantaneous amplitude and frequency with the F1-socre of 1 by multiple models (e.g., KNN, logistic and SVM models). Furthermore, linear discriminant analysis model performed best in IMF4 of instantaneous frequency with the F1-score of 0.86 for detection of delusion; while logistic model performed ideally in IMF2 of sample entropy with the F1-score of 0.95 for detection of hallucination. Naive Bayse model with IMF2 of instantaneous frequency had the F1-score of 0.87 for predicting both symptoms.
![image](https://github.com/MengHuaKuo/school-brainhack.github.io/assets/130176621/37a35186-c1fe-47c8-9300-5e1630f3f484)
![image](https://github.com/MengHuaKuo/school-brainhack.github.io/assets/130176621/b6b255f6-baf9-4aa9-a91c-e9f931e6e099)

**Conclusion and acknowledgement**
Our study shows the precise diagnosis for SCZ is feasible. In addition, the prediction of delusion and hallucination help to clarify the influence from one brain network to another, which might indirectly shed light on the network dynamics and structural connectivity.

I am grateful for the efforts from all of our instructors and TAs. The project enhanced a lot of hands-on skills and also offered me a chance to practice in actual.

