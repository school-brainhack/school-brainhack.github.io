---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-06-11" # Date you first upload your project.
# Title of your project (we like creative title)
title: "Combine EEG/MRI/Behavioral data-sets to learn more about Music/Auditory system"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Marcel Farres Franch]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2020/BHS-AuditoryMultimodal

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [EEG, fMRI, music, auditory-perception, preprocessing, fmriprep]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "In this project I aim to combine data from different modalities (fMRI, EEG, and behavioral) to understand more about sound and music processing. My main focus in this project was to try to reproduce some of the results from a published paper starting form raw data."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "data_pipeline.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

# Combine EEG/MRI/Behavioral data-sets to learn more about Music/Auditory system

![SEff](https://imgs.xkcd.com/comics/selection_effect.png)

<!-- ![Mri](fmri.png ) -->

## Summary

I'm currently a PhD student of the IPN at McGill University.

In this project I aim to combine data from different modalities (fMRI, EEG, and behavioral) to understand more about sound and music processing.

My main focus in this project was to try to reproduce some of the results from a published paper starting form raw data.

The overall goal of the current project is to be able to organize, pre-process and do some basic analyses form a fMRI study.

## Project definition

### Background

In my current PhD project one of the end results should be a open multimodal behavioural and neuroimaging dataset characterizing healthy human auditory processing.
It aims to allow researchers address individual differences in auditory cognitive skills across brain functions and structures, and it will serve as a baseline for comparison with clinical populations.
To achieve that, our core objectives are to create a standardized framework with which to administer a battery of curated tasks.
After acquiring the data from 70 young adults and we intend to share our framework, analysis pipelines, stimuli with linked descriptors, and metadata with the community through open data repositories. The dataset contains cognitive and psychophysical tasks, as well as questionnaires designed to assess musical abilities, speech, and general auditory perception. It also includes EEG and fMRI recorded during resting state, as well as naturalistic listening to musical stimuli and speech.

During this BrainHanks School project I wanted to understand what are the needs as a researcher to easily make use of public available data and learn the basics of pre-processing raw fMRI data.

### Learning Goals

I have good experience analyzing highly process data... but how you get there?

* Raw data → BIDS formatted raw data

* BIDS formatted raw data → BIDS formatted preprocess data

* Basic Data quality control

* Basic analysis

* Implement other people analysis and reproduce results

(but it is a 2 and a half week project...)

![Estimating Time](https://imgs.xkcd.com/comics/estimating_time.png)

### Tools

The project will rely on the following technologies:

* fmriprep

* pandas

* nipype

* bids

* bids-validator

* nilearn

* numpy

* pathlib

* jupiter lab

* [OpenNeuro](https://openneuro.org/)

### Data

The first step was to search for candidates open datasets. I prioritized music/auditory related, as it is closer to my PhD project.

Next there is a list of interesting datasets I found, which I choose 2 to work during this course:

#### Chosen

* Forrest Gump: A very interesting study that use naturalistic stimuli to understand more about how our brain interacts with the real complex world. More information in the dedicated [web-side](http://studyforrest.org/). Here you can find the [list of 29 publications](http://studyforrest.org/publications.html) that use the data made publicly available.

  I was particularly interested in the first 20 subjects that perform a music task (Listening to music (7T fMRI, cardiac & respiratory trace).

  I wanted to replicate the analyisis and findings of [this paper](https://f1000research.com/articles/4-174/v1).

  | N      | Type      | Tasks    | Comments |
  |--------|-----------|----------|----------|
  | 37     |     bold, T1w, T2w, angio, dwi, fieldmap      |   Forrest Gump, objectcategories, movielocalizer, retmapccw, retmapcon, retmapexp, movie, retmapclw, coverage, orientation, auditory perception        |    Maybe the most promising example     |

  <https://openneuro.org/datasets/ds000113/versions/1.3.0>

* Neural Processing of Emotional Musical and Nonmusical Stimuli in Depression: Study looking how people with depression process differently musical stimuli.

  Same idea as the previous study, replicate results reported in [this paper](https://pubmed.ncbi.nlm.nih.gov/27284693/) using the publicly available data.

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  39   |      T1w, bold      |     Music, Non-Music listening     |    missing stims    |

  <https://openneuro.org/datasets/ds000171/versions/00001>

#### Other Options

* A dataset recording joint EEG-fMRI during affective music listening.

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  21   |    T1w, channels, eeg, events, bold       |     GeneratedMusic, classicalMusic, genMusic01, genMusic02, washout, genMusic03     |  Could be very noisy EEG but also promising      |

  <https://openneuro.org/datasets/ds002725/versions/1.0.0>

  * Article <https://www.nature.com/articles/s41598-019-45105-2.pdf>  

* Decoding Musical Training from Dynamic Processing of Musical Features in the Brain.

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  36   |    bh bold       |  music listening        |    Non standard format    |

  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5768727/>

* Neuroimaging predictors of creativity in healthy adults

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  66   |    T1w, T2w, dwi, bold, fieldmap       |    Rest     |   Interesting to study resting state, good number of subjects     |

  <https://openneuro.org/datasets/ds002330/versions/1.1.0>

* Functional Connectivity of Music-Induced Analgesia in Fibromyalgia

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |    40 |     T1w, dwi, bold      |   pre-control, pre-music, post-control, post-music      |     healthy and Fibromyalgia patients listening to music  |

  <https://openneuro.org/datasets/ds001928/versions/1.1.0>

  <http://www.eecs.qmul.ac.uk/mmv/datasets/deap/>

* Music BCI (006-2015)

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  | 10    |    eeg       |    oddball 3 music instruments     |  not much to extract maybe      |

  <http://bnci-horizon-2020.eu/database/data-sets>

  Publication:
  * <http://doc.ml.tu-berlin.de/bbci/BNCIHorizon2020-MusicBCI/BNCI_MusicBCI.pdf>

* OpenMIIR - Music imagery information retrieval

  <https://github.com/sstober/openmiir>

  <https://academictorrents.com/details/c18c04a9f18ff7d133421012978c4a92f57f6b9c>

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  10   |   eeg        |  imagery        |   very short musical exerts      |

  Existing Publications:

  * <https://bib.sebastianstober.de/2015-01-31_NEMISIG.pdf>

  * Sebastian Stober. Towards Studying Music Cognition with Information Retrieval Techniques: Lessons Learned from the OpenMIIR Initiative. In: Frontiers in Psychology Volume 8, 2017.
  doi: 10.3389/fpsyg.2017.01255

  * Sebastian Stober. Learning Discriminative Features from Electroencephalography Recordings by Encoding Similarity Constraints. In: Proceedings of 42nd IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP’17), Pages 6175-6179, 2017.
  doi: 10.1109/ICASSP.2017.7953343

  * Sebastian Stober; Thomas Prätzlich & Meinard Müller. Brain Beats: Tempo Extraction from EEG Data. In: 17th International Society for Music Information Retrieval Conference (ISMIR’16), 2016.
  available from: <https://wp.nyu.edu/ismir2016/wp-content/uploads/sites/2294/2016/07/022_Paper.pdf>

  * Sebastian Stober; Avital Sternin; Adrian M. Owen & Jessica A. Grahn. Deep Feature Learning for EEG Recordings. In: arXiv preprint arXiv:1511.04306 2015.
  available from: <http://arxiv.org/abs/1511.04306>

  * Avital Sternin; Sebastian Stober; Jessica A. Grahn & Adrian M. Owen. Tempo Estimation from the EEG Signal during Perception and Imagination of Music. In: 1st International Workshop on Brain-Computer Music Interfacing / 11th International Symposium on Computer Music Multidisciplinary Research (BCMI/CMMR’15), 2015.
  available from: <http://bib.sebastianstober.de/bcmi2015.pdf>

* The neural basis of spoken word perception in older adults

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   61  |     T1w, T2w, bold, events       |   LISTEN02, REPEAT02, REPEAT01, LISTEN01      |    Interesting, need to read more about the data. there are 375 different monosyllabic words |

  <https://openneuro.org/datasets/ds002382/versions/1.0.0>

* A dataset recorded during development of an affective brain-computer music interface:

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  19-10-9   |    channels, eeg, events       |   music listening and reported arousal and valance      |    Low subj number but interesting data    |

  * <https://openneuro.org/datasets/ds002724/versions/1.0.1>

  * <https://openneuro.org/datasets/ds002722/versions/1.0.1>

  * <https://openneuro.org/datasets/ds002723/versions/1.1.0>

* An EEG dataset recorded during affective music listening

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  31   |   channels, eeg, events        |   music listening       |   Very little information about what files where use     |

  <https://openneuro.org/datasets/ds002721/versions/1.0.1>

  Possible article:

  * <https://www.sciencedirect.com/science/article/abs/pii/S030439401400367X>

* Sherlock_Merlin waiting bids validator

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   37  |  mri      |   listen and see movie (A/B groups)      |   Very interesting, stimuli are provided     |

  <https://openneuro.org/datasets/ds001110/versions/00003>

* Milky-Vodka - (2 different stories )

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  54   |      T1w, bold, events     |     Milky, Synonyms, Scrambled, Vodka    |    stims available,     |

  <https://openneuro.org/datasets/ds001131/versions/1.0.0>

* Audiovisual Learning MEG Dataset
  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   30  |    coordsystem, channels, events, meg       |   The auditory and visual stimuli were 12 Georgian letters and 12 Finnish phonemes      |     mapping things?   |

  <https://openneuro.org/datasets/ds002598/versions/1.0.0>

* Auditory localization with 7T fMRI

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   10  |   T1w, PD, T2star, dwi, bold, events, fieldmap        |   rest, auditory, TODO: full task name for rest, TODO: full task name for auditory      |  need to be down sampled       |

  <https://openneuro.org/datasets/ds001942/versions/1.2.0>

* FFR ?.

  <https://www-jneurosci-org.proxy3.library.mcgill.ca/content/37/4/830>

#### Interesting but not related

* Go-nogo categorization and detection task

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |     |           |         |        |

  <https://openneuro.org/datasets/ds002680/versions/1.0.0>

* A multi-modal human neuroimaging dataset for data integration: simultaneous EEG and MRI acquisition during a motor imagery neurofeedback task

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   10  |      T1w, eeg, bold     |      eegNF, fmriNF, motorloc, eegfmriNF, MIpre, MIpost   |   Not interested     |

  <https://openneuro.org/datasets/ds002336/versions/2.0.0>

  <https://openneuro.org/datasets/ds002338/versions/2.0.0>  

* TUH EEG Corpus Too big for the 3 weeks.

  <https://www.isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml>

* Dataset: rsfMRI before and after one session EEG NF vs Sham NF

<https://openneuro.org/datasets/ds001408/versions/1.0.3>

* Data relating "Alpha/beta power decreases track the fidelity of stimulus-specific information"

  <https://openneuro.org/datasets/ds002000/versions/1.0.0>

* Real-time EEG feedback on alpha power lateralization leads to behavioral improvements in a convert attention task

  <https://openneuro.org/datasets/ds002034/versions/1.0.1>

* EEG meditation study

  <https://openneuro.org/datasets/ds001787/versions/1.0.2>

* EEG study of the attentional blink; before, during, and after transcranial Direct Current Stimulation (tDCS)

  <https://openneuro.org/datasets/ds001810/versions/1.1.0>

* Simultaneous EEG-fMRI - Confidence in perceptual decisions

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |  24   |     T1map, bold, events, eeg      |  motion direction of random dot kinematograms        |        |

  <https://openneuro.org/datasets/ds002739/versions/1.0.0>

* Audiocue walking study

  <https://openneuro.org/datasets/ds001971/versions/1.1.1>

* Auditory and Visual Rhythm Omission EEG

  <https://openneuro.org/datasets/ds002218/versions/2.0.0>

* Auditory and Visual Oddball EEG-fMRI

  | N      | Type      | Tasks | Comments |
  |--------|-----------|----------|----------|
  |   17  |    T1w, inplaneT2, bold, eeg, events       |         auditory oddball with button response to target stimuli, visual oddball with button response to target stimuli|        |

  <https://openneuro.org/datasets/ds000116/versions/00003>

#### NOT Accessible

I also find some very interesting datasets that I was not able to access directly and in the period of 3 weeks I was still waiting for them.

I was a little frustrated with the process, making me realize how important is real Open Data.

* DEAP: A Database for Emotion Analysis Using Physiological Signals:

  website: [https://www.eecs.qmul.ac.uk/mmv/datasets/deap/]

  paper: [https://www.eecs.qmul.ac.uk/mmv/datasets/deap/doc/tac_special_issue_2011.pdf]

  (Not Accessible without explicit permission, which we are missing for no)

### Deliverables

At the end of this project, we have:

* Scripts to download the dataset ([HERE](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/scripts/download-for-test.sh) and [HERE](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/scripts/download-for-all.sh)).

* Scrips to pre-process the data using fmriprep in a cluster ([HERE](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/scripts/run-fmriprep-test.sh) and [HERE](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/scripts/run-fmriprep-all.sh)).

* fmriprep report on the pre-processing ([HERE](http://htmlpreview.github.io/?https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/fmri-prep-results/sub-control01.html)).

* Basic processing of 1 subject ([HERE](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/BHS_AuditoryMultimodal-ds000171.ipynb)) with some need to be improve analysis.

### Project plan / Objectives

* [x] Download multiple interesting datasets (local and to the server)

  * [x] **fMRI** studyforrest <https://openneuro.org/datasets/ds000113/versions/1.3.0>

  * [x] **fMRI** Neural Processing of Emotional Musical and Nonmusical Stimuli in Depression <https://openneuro.org/datasets/ds000171/versions/00001>

  * [x] **EEG** An EEG dataset recorded during affective music listening <https://openneuro.org/datasets/ds002721/versions/1.0.1>

  * [x] **EEG-fMRI** A dataset recording joint EEG-fMRI during affective music listening <https://openneuro.org/datasets/ds002725/versions/1.0.0>

* [x] Explore fMRI datasets

* [ ] ~~Explore EEG datasets~~ (Not enough time)

* [ ] ~~Replicate results for each dataset.~~ (Not enough time)

  * [x] ~~fMRI <https://openneuro.org/datasets/ds000113/versions/1.3.0>~~ (data need pre-processing and the dataset was not fully BIDS compatible)

  * [x] fMRI <https://openneuro.org/datasets/ds000171/versions/00001>

    * [x] Preprocess data.

    * [X] Do some basic visualizations.

    * [ ] Do connectivity and activation analysis mus/no-mus stimuli (IN Progress)

    * [ ] ~~Reproduce figures from the paper~~ (Not enough time)

  * [ ] ~~EEG <https://openneuro.org/datasets/ds002721/versions/1.0.1>~~ (Not enough time)

  * [ ] ~~EEG-fMRI <https://openneuro.org/datasets/ds002725/versions/1.0.0>~~ (Not enough time)

* [ ] ~~Extract commune information from the different datasets~~ (Not enough time)

* [ ] ~~Analyse data coming from the different datasets together~~ (Not enough time)

* [x] Proper code documentation and add necessary comments

* [x] Create and share conda env.

### Installation instructions

1. Clone the repo to your computer:

    `git clone https://github.com/brainhack-school2020/BHS-AuditoryMultimodal.git`

2. Install fMRI prep using [this instructions](https://fmriprep.readthedocs.io/en/stable/installation.html)

3. Download and preprocess the data using [these scripts](https://github.com/brainhack-school2020/BHS-AuditoryMultimodal/blob/master/scripts/) (you can grab a coffee or two... these may take a while).

4. Create a virtual-env
    `python3 -m venv bhs-auditory`

5. Install requirements
    `pip install -r requirements.txt`

6. Open the notebook
    `jupyter lab BHS_AuditoryMultimodal-ds000171.ipynb`

## Conclusion

After the multiple problems I found trying to process the data, reproduce the analyses, and limitations imposed by the missing of information form the dataset I am more aware of what I will need to do to efficiency share my data/analyses in the near future.

Don't be that researcher...

![ML](https://imgs.xkcd.com/comics/machine_learning.png)
