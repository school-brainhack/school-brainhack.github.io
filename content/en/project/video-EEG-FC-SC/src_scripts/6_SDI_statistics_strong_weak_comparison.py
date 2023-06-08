"""Study 1. This script compares the strong and weak conditions for each band, and plots the t-values on the surface. """

import numpy as np
from scipy.stats import ttest_rel, ttest_1samp
from statsmodels.stats.multitest import fdrcorrection
import scipy
from nilearn.plotting import plot_img_on_surf
from nilearn.regions import signals_to_img_labels
from nilearn.datasets import fetch_icbm152_2009

bands = ['wideband', 'theta', 'alpha', 'low_beta','high_beta'] 
n_ROIs = 360
HOMEDIR = "/users/local/Venkatesh/Brainhack"

for band in bands: # for each band

    first_level_Strong = np.load(f'{HOMEDIR}/Generated_data/Graph_SDI_related/1st_level_test_stats_strong/{band}_differenced.npz')['tvalues_step2']
    first_level_weak = np.load(f'{HOMEDIR}/Generated_data/Graph_SDI_related/1st_level_test_stats_weak/{band}_differenced.npz')['tvalues_step2']
    
    pvals = list()
    tvals = list()

    for roi in range(n_ROIs):
        ttest = ttest_1samp(first_level_Strong[:, roi] -first_level_weak[:, roi], popmean=0)
        tvals.append(ttest[0])
        pvals.append(ttest[1])

    pvals_corrected = fdrcorrection(pvals)[1] # FDR correction

    pval = 0.01
    n_observations = 25
    df = n_observations - 1  # degrees of freedom for the test
    thresholding_level = scipy.stats.t.ppf(
        1 - pval / 2, df
    )  # two-tailed, t distribution
    indices = np.logical_or(
        (tvals < -thresholding_level), (tvals > thresholding_level)
    )

       
    path_Glasser = f"{HOMEDIR}/src_data/Glasser_masker.nii.gz"
    mnitemp = fetch_icbm152_2009()


    s_map = signals_to_img_labels(
        indices * tvals, path_Glasser, mnitemp["mask"]
    )
    plot_img_on_surf(
    s_map,
    title=f"uncorrected tmap; tstats threshold @ 0.05; {band}; post-onset",
    threshold=0.1
    )#, output_file=f'/users/local/Venkatesh/Brainhack/Results/Figures/{band}.svg
# %%
