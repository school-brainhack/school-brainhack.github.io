# Contrastive Variational Autoencoder for ADHD-200 Brain MRI Analysis

This repository contains the code and resources for a deep learning project applying **Contrastive Variational Autoencoders (CVAEs)** to structural MRI data from the [ADHD-200 dataset](http://fcon_1000.projects.nitrc.org/indi/adhd200/). Inspired by [Aglinskas et al. (2022)](https://doi.org/10.1126/science.abm2461), the project aims to disentangle ADHD-specific neuroanatomical variations from shared population-level features, enabling interpretable modeling of heterogeneity in ADHD.

---

## 🧠 Project Goals

- Reconstruct 3D brain MRIs using CVAEs.
- Disentangle "salient" ADHD-related features from "background" features common to both ADHD and typically developing children.
- Assess how well the learned latent spaces reflect behavioral and clinical variation using:
  - **Silhouette Analysis**
  - **Representational Similarity Analysis (RSA)**

---

## 📂 Project Structure

| File / Folder                      | Description |
|-----------------------------------|-------------|
| `Train-CVAE-ADHD200.ipynb`     | Notebook for training CVAE, extracting features, and running RSA/silhouette analyses |
| `helper_funcs.py`                 | Utility functions for training, visualization, silhouette scoring, and RSA |
| `make_models2.py`                 | Defines CVAE and VAE architectures using Keras |
| `VBM_subjects_matched.csv`        | Subject IDs aligned with Burner-preprocessed MRI data |

---

## 📦 Dataset & Preprocessing

We used the **Burner Pipeline** version of the ADHD-200 dataset, a VBM-based preprocessing approach:
👉 https://www.nitrc.org/plugins/mwiki/index.php?title=neurobureau:BurnerPipeline

- Data is voxel-based morphometry (VBM) gray matter maps.
- Normalized and segmented into 3D volumes of shape 64×64×64.

---

## ⚙️ Getting Started

### Prerequisites
- python=3.8
- numpy=1.21.0
- umap-learn=0.5.1
- pandas=1.1.5
- seaborn=0.11.0
- matplotlib=3.3.4
- scikit-learn=0.24.2
- ipykernel
- jupyter
- tqdm
- scipy=1.6.2

---

## 🧪 Method Overview

### Contrastive Variational Autoencoder (CVAE)
The CVAE is trained on ADHD and control subjects to learn:
- `z`: background features (common/shared)
- `s`: salient features (ADHD-specific)

### Representational Similarity Analysis (RSA)
Latent representations are compared with clinical variables such as age, diagnosis, and IQ using Kendall’s tau-based similarity matrices.

### Silhouette Analysis
Measures how well subjects group in the latent space based on clinical labels (e.g., diagnosis, sex, age groups).

---

## 🔍 Key Findings

- **Salient (ADHD-specific)** features correlate more strongly with diagnosis and behavior-related variables.
- **ADHD features** correlate more with **ADHD Index**, **Inattentive score**, **Hyper/Impulsive score**, **Medication Status**, and **Age**.
  - **Significant correlations** were observed with **Medication Status** and **Age**.
- **Shared (background)** features correlate more with **Full IQ**, **Gender**, and **Scan Site**.
  - **Significant correlation** was observed with **Gender**.
- ADHD anatomical variation may be better described along **continuous dimensions** rather than discrete clusters, aligning with dimensional models of psychiatric disorders.

---

## 📝 Citation

If you use this code or adapt this framework, please cite:

Aglinskas, A., Hartshorne, J. K., & Anzellotti, S. (2022). *Contrastive machine learning reveals the structure of neuroanatomical variation within autism*. Science, 376(6595), 1070–1074. https://doi.org/10.1126/science.abm2461

---

## 👩‍💻 Authors

Cian-Ya Lan and Jia-Ling Sun  
National Taiwan University
