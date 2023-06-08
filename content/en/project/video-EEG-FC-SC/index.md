---
type: "project" # DON'T TOUCH THIS ! :)
date: "2023-06-09" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Investigating Structure-Function Coupling and Segregation Patterns during Video-Watching: Unveiling Dynamics of Electrophysiological Activity and Functional Connectivity"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Venkatesh Subramani, Romy Beauté]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2023/subramani_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [eeg, dmri, brain-dynamics, connectivity, visual-stimuli] 

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This study investigated the Structure-Function coupling of weakly correlated electrophysiological activity during video-watching. While defining Weak Inter-Subject Correlation (ISC) based on correlation alone proved challenging, exploring Segregation analysis revealed higher segregation within the Visual network during periods of Significant ISC, highlighting the potential of this approach to capture distinct dynamics in brain connectivity during video-watching."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "paradigms_BHS.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

## Background
## Study 1
Numerous studies have extensively investigated how individuals respond to naturalistic stimuli, particularly video-watching. These studies, conducted by researchers such as Uri Hasson et al. (2004), Sonkusare et al. (2019), have provided valuable insights into the neural mechanisms underlying the processing of such stimuli. Additionally, investigations into the synchronization of brain activity among individuals during independent viewing, as explored by Uri Hasson et al. (2004) and Dmochowski et al. (2012), have revealed the remarkable coordination and shared neural responses that occur during these experiences. Furthermore, previous research has focused on quantifying the strength of the relationship between the brain's structure and its functional activity during resting-state conditions. Study by Preti M G and Van de Ville D. (2019) has shed light on this structure-function coupling, highlighting how the underlying anatomical organization influences brain function at rest. A recent study conducted by Samara et al. (2023) has compared the macro-scale cortical organization of the brain during video-watching with resting-state conditions, providing valuable insights into the similarities and differences in brain organization and functional connectivity between these two states. Collectively, these studies have significantly advanced our understanding of how the brain responds to naturalistic stimuli, the synchronization of brain activity during independent viewing, the relationship between brain structure and function during rest, and the cortical organization during video-watching and resting-state conditions.

The gap in the existing research is the exploration of how the electrophysiological activity during video-watching depends on the underlying anatomical structure.

The cortex has been observed to exhibit stereotypical responsiveness to complex naturalistic stimuli and display links to individual variability [Uri Hasson et al., 2004], referred to as Strong Inter-subject Correlation (ISC) and Weak ISC.

![image info](/strong_weak_ISC.jpg)
*Red markers indicate the significant ISC tested against bootstraping. Strong ISC has been already studied as part of the PhD work of Venkatesh. Weak ISC is investigated in the framework of BHS and they are defined based on criterion such as the period in which ISC is identified to be low*

The objective of our study is two folds: To examine the Structure-Function coupling of the electrophysiological activity during video-watching, particularly focusing on periods of weak inter-subject correlation (ISC).
To compare the Structure-Function coupling observed during Strong ISC and Weak ISC periods, shedding light on the differences in cortical organization and functional connectivity between these states.


## Study 2
Results supported by from the Study 1 points in the direction that Structure-Function coupling during Strong and Weak ISC does not vary, prompting to design and analyse the Inter-Subject Synchrony during video-watching from a different lens.

Graph Theory has emerged as a powerful tool for modeling the brain as interconnected networks, enabling the examination of functional relevance and brain organization through various measures (Sporns, 2022). The networked brain exhibits both segregation, characterized by specialized processing within specific networks, and integration, involving distributed information processing across multiple networks (Bassett and Bullmore, 2007). This highlights the dynamic interplay between specialized and distributed processing in the brain. Segregation, a measure derived from Graph Theory and emphasized by Wig (2017), quantifies the interaction level between a given network and other networks, providing insights into communication and information exchange (Wig, 2017). By leveraging Graph Theory measures such as segregation, valuable insights into the functional connectivity and information processing dynamics of the brain can be gained.


![image info](/content/en/project/video-EEG-FC-SC/Segregation.jpg)
*Segregation quantifies how much does a given network talk to other networks, e.g., Does Visual Yeo-Krienen network talk to other networks such as Default-Mode Network, Frontoparietal, Dorsal Attention ?*

Objective: Could there be a marker distinguishable in the specific periods of the video that Segregation highlight ?
We look into the Segregation of Visual network during the entire period of the video investigating whether this network possesses clear pattern of segregation/integration during specific segments of the video. 

### Tools
* Python, Scipy, Nilearn, Pandas, Matplotlib, mne_connectivity

### Data
* Video-watching EEG (N = 25) from Healthy Brain Network - [HBN](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/)
* Structural Connectome of N = 56 subjects from Human Connectome Project - [HCP](https://www.humanconnectome.org) constructed by Preti M G and Van de Ville D., 2019
* Pre-processed and source-localized EEG signal

### Deliverables
 - Documentation in this markdown
 - Git repo containing source code
 - OSF for all the source and generated data - https://osf.io/qjk6y/?view_only=f804a763eede498da80ba521fb1490d3
 - Wrapping up to submit at the gallery of the student projects at Brainhack 2023.

## Results

### Progress overview
In this study, we embarked on an investigation of the Structure-Function coupling of weakly correlated electrophysiological activity during video-watching, focusing on periods of weak inter-subject correlation (ISC). However, our attempt to define Weak ISC based solely on correlation encountered challenges, with no significant differences in the structure-function coupling observed between Strong and Weak ISC periods. This highlighted the intricacy of relying solely on correlation for such definitions.

Motivated by the work of Betzel et al. (2020), we transitioned to an alternative approach using Segregation analysis to identify distinctive patterns during specific video segments. To accomplish this, we computed Functional connectivity by leveraging a dynamic window based on phase coherence among all pairs of HCP-MMP ROIs (Glasser et al., 2016). Notably, we focused on assessing the level of Segregation within the Visual Yeo-Krienen network.

Subsequently, we compared Segregation between periods characterized by Significant ISC (red markers) and non-Significant ISC (null ISC). Excitingly, we observed higher segregation within the Visual network during Significant ISC periods (t(168) = 1.97; p < 0.048; 
permutation-corrected).

This transition from investigating Structure-Function coupling based on correlation alone to exploring Segregation as an alternative approach allowed us to uncover meaningful patterns during video-watching. Our findings emphasize the complexity of defining ISC periods and highlight the potential of Segregation analysis to capture distinct dynamics in the brain's functional connectivity during video-watching.

### Tools we learned during this project

 * **Meta-project**: We are delighted to have made the best use of BHS. We learned to visualize all the layers in the project starting from conception to implementation to interpretation. We observed that we are a human-variant of backpropagation algorithm tweaking the previous layers in answering an interesting research question.
 * **Git and Github**: We unlearned and relearned Git version control as part of the BHS training modules and applied the knowledge during this project


# Results

## Deliverable 1: Report
Current report in a markdown file

## Deliverable 2: Structure-Function coupling between Strong ISC and Weak ISC periods
We employed a Graph Signal Processing (GSP) measure, introduced by Preti M G and Van de Ville D [Preti M G, Van de Ville D., 2019], to quantify the relationship between structure and function. Specifically, we examined the strength of decoupling between weakly correlated electrophysiological activity and the underlying anatomical structure. Comparing the patterns observed during Strong and Weak ISC periods, we found no significant differences in the regions of interest (ROIs) (paired t-test on the ROIs with FDR-correction).

![image info](alpha.png)
*Uncorrected test statistics by comparing Strong and Weak ISC periods for the alpha band. The test statistics is thresholded at alpha = 0.05*

![image info](alpha_corrected.png)
*FDR-corrected spatial map for the alpha band*

Visual inspection of the uncorrected test statistics map revealed localized differences across the brain in the alpha band. However, the FDR-corrected spatial map demonstrated that no regions reached statistical significance. This observation suggests that the lack of significant differences between Strong and Weak ISC periods may be attributed to their close similarity. These findings underscore the complexity involved in defining Weak ISC periods and highlight the challenges associated with studying their distinct characteristics.

## Deliverable 3: Segregation analysis during video
We computed functional connectome dynamically (1s of EEG) over a non-overlapping sliding window for the cortical activity in the alpha band. The regions of interest (ROIs) defined by the HCP-MMP parcellation [Glasser et al., 2016] were grouped, and Segregation analysis [Wig G S, 2017] was performed, with a specific emphasis on the Visual Yeo-Krienen network. To establish a noise floor, we generated surrogate Segregation measures by spatially permuting the EEG cortical signal (N = 100). We compared the observed Segregation values against the surrogate Segregation measures to identify instances where the observed Segregation exceeded the noise floor.

![image info](segregation_alpha.png)
*Relating Segregation time-series to the Strong ISC. First the ISC time-series (blue) is binarized i.e., set to 1 when it is Strong. Second, the Segregation is projected alongside (green). The yellow horizontal line distinguishes the level of Segregation (high or low)*

Upon analyzing the time-series of Segregation in relation to the binarized Strong ISC (blue), we observed occasional alignment between the two, although not strictly consistent. To further explore this relationship, we categorized the Segregation into two groups.

![image info](segregation_grouping.png)*Segregation grouped to two groups*

The analysis revealed a significant difference between the two groups (two-sample t-test; t(168) = 1.97; p < 0.048; corrections with 50000 permutations), indicating that the Visual Yeo-Krienen network exhibits greater segregation during periods of significant inter-subject correlation (ISC).

Overall, these findings demonstrate that the level of Segregation in the Visual network is influenced by the strength of ISC, providing insights into the functional dynamics of the brain during video-watching.

## Deliverable 4: project gallery
The content is made ready for to be added to the project gallery of BHS 2023

## Conclusion and acknowledgement
In this project, the researchers investigated the relationship between electrophysiological activity and underlying anatomical structure during video-watching. They initially focused on periods of weak inter-subject correlation (ISC) and attempted to define weak ISC based on correlation. However, they found no significant differences in the structure-function coupling between strong and weak ISC periods. They then shifted their approach and explored segregation analysis as an alternative method to identify distinct patterns during specific video segments. They computed functional connectivity using a dynamic window and assessed the level of segregation within the Visual Yeo-Krienen network. The results showed higher segregation within the Visual network during periods of significant ISC compared to null ISC. These findings highlight the complexity of defining ISC periods and demonstrate the potential of segregation analysis to capture unique dynamics in the brain's functional connectivity during video-watching.

The authors would like to thank Austin Benn for the supervision. Nicolas Farrugia, and Giulia Lioi for the inputs along the way. Last but not the least, the authors would like to register a massive thanks and gratitude to Team Organizers of BHS 2023 for a smooth and wonderful Brainhack!