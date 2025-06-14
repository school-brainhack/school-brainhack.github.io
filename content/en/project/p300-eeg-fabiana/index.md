---
type: "project"
date: "2025-06-14"
title: "Exploring Emotional Modulation of the P300 in EEG Data"

names: [Fabiana Ojeda 歐瑩忻]

github_repo: https://github.com/faojeda/p300-eeg-brainhack2025

slides: https://drive.google.com/file/d/1mXoa-OyEHx_O3uHKW4EWqyjux8VKKN_g/view?usp=drive_link

tags: [eeg, erp, mne, brainhack]

summary: "This project explores how deviant auditory tones in a cross-modal oddball paradigm elicit a stronger P300 component using EEG data from the MNE sample dataset. The analysis focuses on ERP comparison and difference waves, setting the stage for future investigations on emotional modulation of P300."

image: "project/img/thumbnail.png"
---

## Project definition

### Background

The P300 is an event-related potential (ERP) component often associated with attention and stimulus evaluation. It is typically elicited by infrequent, task-relevant stimuli in oddball paradigms. This project used the MNE sample dataset to examine P300 responses to standard and deviant tones in a cross-modal oddball task.

### Tools

- Python  
- MNE-Python  
- Jupyter Notebook  
- Git & GitHub  
- EEG plotting and ERP comparison tools  

### Data

The project uses the [MNE sample dataset](https://mne.tools/stable/overview/datasets_index.html#sample), which includes auditory and visual stimuli recorded during a multimodal oddball paradigm. For this analysis, auditory standard (left) and deviant (right) tones were selected for ERP comparison.

### Deliverables

- ERP plots comparing standard and deviant tones  
- A difference wave plot showing the increased P300 amplitude for deviant tones  
- A Jupyter Notebook with complete code and results  
- README and documentation hosted on GitHub  

## Results

### Event Summary

| Event | Description               | Count |
|-------|---------------------------|--------|
| 1     | Auditory left             | 72     |
| 2     | Auditory right (standard) | 73     |
| 3     | Visual right              | 73     |
| 4     | Visual left               | 71     |
| 5     | Auditory deviant (rare)   | 15     |
| 32    | Button press              | 16     |

For this project, I focused on event 2 (auditory standard) and event 5 (auditory deviant) because they align with the auditory oddball paradigm known to elicit the P300.

### ERP Comparison

The deviant tone produced a larger positive deflection around 300 ms, consistent with the P300 component. This supports attentional engagement triggered by unexpected stimuli.

![ERP comparison](/project/img/erp_comparison.png)

### Difference Wave

Subtracting standard from deviant responses revealed a clear P300 difference peaking at ~300 ms.

![Difference wave](/project/img/difference_wave.png)

## Conclusion and Acknowledgements

This project demonstrated the classic P300 effect using auditory tones in a cross-modal oddball paradigm. It served as a practical introduction to MNE-Python, EEG data analysis, and ERP visualization. Future directions could explore emotional modulation of the P300 in similar paradigms.

Big thanks to the Brainhack School organizers, TAs, and professors!
