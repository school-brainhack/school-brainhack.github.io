---
type: "project" # DON'T TOUCH THIS ! :)
date: "2020-06-11" # Date you first upload your project.
# Title of your project (we like creative title)
title: "MethNet: Visualizing methods in citation networks"

# List the names of the collaborators within the [ ]. If alone, simple put your name within []
names: [Kendra Oudyk]

# Your project GitHub repository URL
github_repo: https://github.com/brainhack-school2020/koudyk_bhs_project

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/brainhack-school2020/project_template), click `manage topics`.
# Please only lowercase letters
tags: [API, text-mining, fMRI, methods]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "A Python package that create a dynamic visualization the use of methods in citation networks over time."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "visualization__example.gif"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Project definition

### Background
Methods can influence results in fMRI research (e.g., Carp, 2012; Eklund et al., 2016; Glatard et al., 2015). If methods influence results, then methodological trends may stystematically influence results. In order to explore this problem space, I thought it might be helpful to visualize methodological trends in fMRI research.

### Purpose
The purpose of this project was to make a Python package that could create a citation network for a given field, colored by methods used by papers in that field. Such a figure would be created for each year in a range, so that one can see the development of the network and the use of methods over time. Using this package to look at research using fMRI, I hope to observe whether methods correspond to groupings of papers in the citation network.

### Data
This package uses the [PubMed Central Open-Access Subset](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/)\*, which is a set of papers on PubMed Central that are available under an open licence. I chose this dataset because the package need access to the full text of journal articles in order to search for methods-related keywords.

## Results
### Progress overview
I was able to create the type of figure that I had envisioned, and I practiced using almost all of tools and skills that I'd hoped to practice. However, the figure has some glitches and was not as informative as I'd hoped. Also, I did not get as far as I'd planned in terms of packaging and testing.

### Deliverables
- [Package](https://github.com/brainhack-school2020/koudyk_bhs_project) in progress,
- [Workflow diagram](https://github.com/brainhack-school2020/koudyk_bhs_project/blob/master/images/workflow_diagrams/diagram_entire_workflow.gv.png) illustrating how the package works,
- [Example notebook](https://github.com/brainhack-school2020/koudyk_bhs_project/blob/master/methnet/example.ipynb) demonstrating how to use the package, and
- [Example gif](https://github.com/brainhack-school2020/koudyk_bhs_project/blob/master/images/visualization__example.gif), which is the output of the example notebook, and can be seen below.

![](visualization__example.gif)

### Tools and skills practiced
In this project, I practiced (more or less)
- [x] Packaging
- [x] GitHub issues & projects
- [x] API interaction, specifically, using the [NCBI Entrez Programming E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25497/)
- [x] XML
- [x] Jupytext
- [x] Python
- [x] Data visualization

## Conclusion and acknowledgement
Although the project did not end up exactly where I'd hoped, I learned a lot along the way. I appreciate all the effort made by the BHS instructors and organizers, particularly Sam, Agah, Alexa, and Loic. I'm also especially thankful to Jérôme, who helped me even though he wasn't part of the BHS.


***

#### References
- Carp, J. (2012). On the plurality of (methodological) worlds: Estimating the analytic flexibility of fMRI experiments. *Frontiers in Neuroscience, 6*, 149.
- Eklund, A., Nichols, T. E., & Knutsson, H. (2016). Cluster failure: Why fMRI inferences for spatial extent have inflated false-positive rates. *Proceedings of the National Academy of Sciences, 113*(28), 7900-7905.
- Glatard, T., Lewis, L. B., Ferreira da Silva, R., Adalat, R., Beck, N., Lepage, C., ... & Khalili-Mahani, N. (2015). Reproducibility of neuroimaging analyses across operating systems. *Frontiers in Neuroinformatics, 9*, 12.

#### \*NCBI's Disclaimer and Copyright notice
The National Center for Biotechnology Information (NCBI), who own the data and E-utilities that this package uses, requests that we make this [Disclaimer and Copyright notice](https://www.ncbi.nlm.nih.gov/home/about/policies/) evident to users.
