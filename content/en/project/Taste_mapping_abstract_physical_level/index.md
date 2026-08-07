---
type: "project" 
date: "2025-06-15" 
# The Transition from Physical to Abstract Taste: An fMRI Study on Sweet, Sour, and Salty
title: "The Transition from Physical to Abstract Taste: An fMRI Study on Sweet, Sour, and Salty"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Tran Cao Bang Trinh]

# Your project GitHub repository URL
github_repo: https://github.com/annamarie1509/Annamarie_BHS_2025_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [fmri, cognition, taste, visual stimuli]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This fMRI study compares two datasets: (1) taste imagery and food pictures, and (2) taste mapping (actual tastes). It examines shared neural patterns for sweet, salty, and sour across these conditions, testing whether imagined and perceived tastes activate overlapping brain regions. Visual inspections of fMRI contrasts aim to reveal universal taste representations, bridging abstract (imagery/pictures) and physical (direct tasting) processing [website](https://github.com/annamarie1509/Annamarie_BHS_2025_project)."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: ""
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
 
This fMRI study investigates how the brain processes both physical and abstract taste experiences. While we readily perceive tastes like sweet and sour, we also use taste metaphors in language (e.g., "sweet person"). Embodiment theory suggests these abstract concepts might share neural mechanisms with actual taste perception.

We analyze two datasets:  
1. **Abstract Taste**:  
   - `task-tasteimagine`: Participants imagined sweet/sour/salty tastes  
   - `task-foodpicture`: Viewed food images representing these tastes  
2. **Physical Taste**:  
   - `task-tastemapping`: Direct taste stimulation (from prior study)  

Key questions:  
- Do imagined/viewed tastes activate similar regions as physical tastes?  
- Can we identify consistent patterns despite individual variability in taste maps?  

Preliminary findings suggest partial overlaps in gustatory areas, though food images also engage object recognition networks. This project systematically compares these conditions to test embodiment in taste processing.


### Tools
This project uses **SPM12** (Statistical Parametric Mapping) for fMRI data preprocessing and analysis:  

- **SPM12 Documentation**:  
  📖 [Official Manual](https://www.fil.ion.ucl.ac.uk/spm/docs/)  
  ▶️ [Tutorial Playlist](https://www.youtube.com/playlist?list=PLwvUhR_TwpXv1aXd_LUCh7iMMLKkd5Tyx)  

- **Key Functions**:  
  ```matlab
  spm('FMRI');        % Initialize fMRI pipeline  
  spm_preproc();      % Preprocessing (realign, coregister, normalize)  
  spm_stats();        % Statistical analysis (GLM, contrasts)  

### Data

This project analyzes two fMRI datasets:

#### Study 1: Abstract Taste Processing
- **Dataset**: [OpenNeuro ds004312 v1.0.3](https://openneuro.org/datasets/ds004312/versions/1.0.3)
- **Publication**: [A common neural code for representing imagined and inferred tastes](https://pubmed.ncbi.nlm.nih.gov/36805499/)
- **Conditions**:
  - `task-tasteimagine`: Mental imagery of tastes (sweet/sour/salty)
  - `task-foodpicture`: Viewing food images representing tastes

#### Study 2: Physical Taste Processing  
- **Dataset**: [OpenNeuro ds002995 v1.0.1](https://openneuro.org/datasets/ds002995/versions/1.0.1)
- **Publication**: [Taste Quality Representation in the Human Brain](https://pubmed.ncbi.nlm.nih.gov/31836661/)
- **Condition**:  
  - `task-tastemapping`: Direct taste stimulation (sweet/sour/salty)

#### Matched Participant Pair:
|          | Dataset 1 (sub-007) | Dataset 2 (sub-072) |
|----------|---------------------|---------------------|
| **Sex**  | F                   | F                   |
| **Age**  | 24                  | 26 (+2 yrs)         |
| **Weight** | 68 kg             | 65.5 kg (-2.5 kg)   |

*Selected for minimal demographic variance in gender/age/weight*

### Deliverables

At the end of this project, we will have:
 - The current markdown document, completed and revised.
 - A gallery of the student projects at Brainhack 2020.
 - Instructions on the website about how to submit a pull request to the [brainhack school website](https://github.com/PSY6983-2021) in order to add the project description to the website.

## Results

### Progress overview

The project was swiftly initiated by P Bellec, based on the existing template created in 2019 by Tristan Glatard and improved by different students. It was really not that hard. Community feedback is expected to lead to rapid further improvements of this first version.

### Tools I learned during this project

 * **Meta-project** P Bellec learned how to do a meta project for the first time, which is developping a framework while using it at the same time. It felt really weird, but somehow quite fun as well.
 * **Github workflow-** The successful use of this template approach will demonstrate that it is possible to incorporate dozens of students presentation on a website collaboratively over a few weeks.
 * **Project content** Through the project reports generated using the template, it is possible to learn about what exactly the brainhack school students are working on.

### Results

#### Deliverable 1: Code Repository
**Preprocessing Pipeline Implementation** (MATLAB/SPM12)

| Processing Step       | Study 1 Status | Study 2 Status |
|-----------------------|----------------|----------------|
| Check Reg (Motion Correction) | ✅ Completed | ✅ Completed |
| Realign & Reslice     | ✅ Completed | ✅ Completed |
| Slice Timing          | ✅ Completed | ✅ Completed |
| Coregister T1 EPI     | ❌ Pending   | ✅ Completed |
| Segmentation          | ❌ Pending   | ✅ Completed |

**Included Files**:
- Configuration .mat files.
- Experimental conditions: 
  - 8 runs * 1 trials condition files for Study 2. 

---

#### Deliverable 2: Quality Control Visualizations

**Study 1 Outputs**:
- Motion correction results

**Study 2 Outputs**:
- Motion correction results
- Structural-functional coregistration
- GLM model specification

---

#### Deliverable 3: First-Level Analysis Specifications

**Model Configuration**:
- `1stlevel/sub-007/results/SPM.mat/` - Complete first-level model specification

**Condition Files**:
- Trial 1: `1stlevel/sub-007/results/Trial1`
- Trial 2: `1stlevel/sub-007/results/mat_conditions`


## Conclusion and Acknowledgments

### Project Status
This remains an **ongoing project** with current progress including:
- Completed preprocessing pipelines for both datasets
- Quality control visualizations
- First-level model specifications

### Future Directions
Following valuable feedback from **Brainhack School 2025**, next steps will focus on:
1. Advancing analysis:
   - 1st → 2nd level analysis
   - Statistical comparison across studies
2. Moving beyond visual inspection to:
   - Quantitative pattern analysis
   - Cross-dataset multivariate approaches
3. Ultimate goal: 
   - Demonstrate universal neural patterns in taste perception
   - Bridge abstract and physical taste representations

### Acknowledgments
Special thanks to:
- The **BHS 2025** instructors and participants for their:
  - Technical guidance on preprocessing
  - Innovative analysis suggestions
  - Encouragement to push beyond initial scope
- My BHS 2025 colleagues for their:
  - Conceptual feedback
  - Dataset recommendations
- OpenNeuro for making the datasets publicly available

*"This project was developed as part of Brainhack School 2025"*
