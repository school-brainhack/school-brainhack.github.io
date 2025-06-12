---
type: "project" 
date: "2025-06-12" 
title: "EEG-Based Odor Preference Modeling 🌹🧀️🪷🍃"

github_repo: github.com/xiao1992/BrainHack_Project

tags: [ML, EEG, odor, brainhack]

summary: "The human sense of smell plays a crucial role in emotional experience. Previous research has shown that EEG can distinguish between pleasant and unpleasant odors at an individual level (Kroupi et al.,2014), but the consistency of these preferences across individuals remain open questions. OPPD dataset: www.epfl.ch/labs/mmspg/downloads/page-119131-en-html"
---

## Project definition

### Background

Kroupi et al. (2014) demonstrated that EEG signals could classify pleasant vs. unpleasant odor perception with high accuracy in a subject-specific manner. However, subject-independent classification yielded lower performance, suggesting significant individual variation. The study did not explicitly test preference consistency across subjects or analyze EEG similarity among individuals who prefer the same odors. 

### Data

We use the OPPD (Odor Pleasantness Perception Database) delopved by Kroupi et al. (2014) from EPFL [OPPD dataset](https://www.epfl.ch/labs/mmspg/downloads/page-119131-en-html/):
The dataset includes EEG recordings from 5 male participants (ages 26–32), each exposed to four odors: valerian, lotus flower, cheese, and rosewater. For each subject, both eyes-open and eyes-closed conditions were tested. Each odor trial includes a baseline segment and an event segment (odor presentation). The EEG signals were recorded with a 256-electrode EGI system at 250 Hz. Participants rated each odor on intensity and pleasantness. The most and least pleasant odors were identified per subject.

### Project Motivation
This project investigates whether individuals share common EEG response patterns to odors they find pleasant or unpleasant, and whether these patterns can be generalized across subjects to predict preferences. The goal is to assess both subject-specific and cross-subject odor pleasantness classification and identify potential for real-world olfactory recommendation systems. Specifically, we seek to:
1) replicate existing within-subject classification of odor pleasantness.
2) Explore subjective vs objective labels correlation with brain activites. 
3) analyze whether EEG response patterns reflect those shared preferences.
4) develop and evaluate models that generalize odor preference prediction.
5) Visualize and distinguish the most active channels, bands and regions associated with different odors, eyes open vs eyes closed conditions.

### Deliverables
- Replication of Kroupi et al. (2014)'s within-subject EEG classification results of pleasant vs. unpleasant odors.
- Statistical analysis of cross-subject odor pleasantness agreement.
- Subjective vs objective labels, Eyes open vs eyes closed ML results. 
- Development of simple classifiers to predict preference class from EEG, including cross-subject generalization.
- A set of visualizations mapping EEG response patterns (channels, bands) to odors.

## Results
1) There is some alignment between what subjects rated as pleasant/unpleasant and what is objectively pleasant/unpleasant. However, the result is not statistically significant (p~0.05). This suggests individual preferences may diverge from traditional expectation.
2) Subjects are more likely to agree with the traditional (objective) odor lables when their eyes are open. This supports the idea that sensory and cognitive context (visual) influences how we evaluate smells (might be due to placebo)
3) Strongest ML performance = Eyes Open + Objective (for all models).
a) Objective Pleasantness is Much Easier to Decode. In both eyes open and eyes closed, accuracy for y_objective is consistently (90% of the case) higher across models. Best model overall: XGBoost in eyes_open (66.7%), indicating EEG contains information about odor perference.
b) Subjective Preferences Are Less Consistent. Much lower and more variable performance for y_subjective (5/5 <50% are subjective preferences).
c) Performance is model-sensitive: RF and KNN show scattered strengths (i.e. KNN best for eyes open, RF best for eyes closed).
This reflects subjectivity: people disagree with objective odor rating, and neural patterns for preferences are weaker.
4) Overall: Eyes Open - Theta, Alpha; fronto-parietal - attention,  emotion encoding;
Eyes Closed - Gamma, Beta; Temporal, occipital - internal sensory processing.

### Progress overview

Explored beyond the original paper on subjective vs objective odor labels ML results.

### Tools I learned during this project

 * **Machine Learning** Explored different kinds of ML models and compare how each suits different dataset. 
 * **Github workflow-** Interacted constantly with Github to updating on the project codes.
 * **Python Package** Made a python package for the first time NeuroSuite. 

### Results

#### Deliverable 1: ML results on subjective vs objective labels and eyes open vs eyes closed conditions

ML results: [Machine Learning Results](https://github.com/xiao1992/BrainHack_Project/blob/main/EEG_model_results.tex)

#### Deliverable 2: Figures of which channels, locations are most active during the odor sensoring experience and different conditions

You can check out the [Figures subject level and group level](https://github.com/xiao1992/BrainHack_Project/tree/main/figures)

#### Deliverable 3: NeuroSuite Package 

You can check out the [NeuroSuite Package](https://github.com/xiao1992/NeuroSuite)

## Conclusion and acknowledgement

*Kroupi, E., Yazdani, A., Vesin, J.M., & Ebrahimi, T. (2014). EEG correlates of pleasant and unpleasant odor perception. ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM), 11(1s), 1–17. [DOI: 10.1145/2637287]
*Koelstra, S. et al. (2011). DEAP: A Database for Emotion Analysis Using Physiological Signals. IEEE Transactions on Affective Computing, 3(1), 18–31.

If cross-subject generalization proves feasible, future work could work on larger and more diverse (females, different ages, more odors) pools which would improve the model’s generalization. Cross-modal integration with physiological signals (GSR, heart rate) may also enhance prediction.
