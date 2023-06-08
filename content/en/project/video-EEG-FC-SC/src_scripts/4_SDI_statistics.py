"""Study 1. This script is used to compute the SDI statistics. The SDI statistics are computed using the following steps:  Ranksum test, 1st level model testing, 2nd level model testing. The 2nd level model testing is done using permutation test. The results are plotted on the surface."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rankdata, ttest_1samp
from tqdm import tqdm
from nilearn.regions import signals_to_img_labels
from nilearn.datasets import fetch_icbm152_2009
from nilearn import plotting
import mne
import scipy
import os

total_no_of_events = "30_events"
HOMEDIR = "/users/local/Venkatesh/Brainhack"


n_subjects = 25
n_events = 24
n_roi = 360
n_surrogate = 50


def stats(band, empirical_SDI, surrogate_SDI):
    """two-level permutation test for SDI"""
    empirical_one_band = empirical_SDI[f"{band}"]
    surrogate_one_band = surrogate_SDI[f"{band}"]

    test_stats_step_1 = list() #test_stats_step_1 to store the ranksum test statistics

    for subject in tqdm(range(n_subjects)):
        event_level_p = list()

        for event in range(n_events):
            roi_level_p = list()

            for roi in range(n_roi):

                data_empirical = empirical_one_band[event, subject, roi]
                data_surrogate = surrogate_one_band[event, :, subject, roi]

                stat_test = sum(
                    rankdata(np.abs(data_empirical - data_surrogate))
                    * np.sign(data_empirical - data_surrogate)
                ) # ranksum test
                stat_test_normalized = stat_test / n_surrogate # normalized ranksum test

                roi_level_p.append(stat_test_normalized)

            event_level_p.append(roi_level_p)

        test_stats_step_1.append(event_level_p)

    # Step 2 : First level Model testing for consistency of SDI across events
    pvalues_step2 = list()
    tvalues_step2 = list()

    for sub in range(n_subjects):
        sub_wise_p = list()
        sub_wise_t = list()

        for roi in range(n_roi):
            data = np.array(test_stats_step_1)[sub, :, roi]
            t, p = ttest_1samp(data, popmean=0)

            # Correcting for inf and -inf values in t and p
            if t == np.inf:
                t = 0
            if t == -np.inf:
                t = 0

            if p == np.inf:
                p = 1
            if p == -np.inf:
                p = 1

            sub_wise_p.append(p)
            sub_wise_t.append(t)

        pvalues_step2.append(sub_wise_p)
        tvalues_step2.append(sub_wise_t)


    np.savez_compressed(f'{HOMEDIR}/Generated_data/Graph_SDI_related/1st_level_test_stats_weak/{band}_{condition}', tvalues_step2=tvalues_step2)

    # Step 3 : Second level Model testing for consistency of SDI across subjects
    # Permutation test
    secondlevel_t, _, _ = mne.stats.permutation_t_test(
        np.array(np.array(tvalues_step2)), n_jobs=-1, n_permutations=50000
    )
    path_Glasser = f"{HOMEDIR}/src_data/Glasser_masker.nii.gz"

    mnitemp = fetch_icbm152_2009()

    pval = 0.0001
    n_observations = 25
    df = n_observations - 1  # degrees of freedom for the test
    thresholding_level = scipy.stats.t.ppf(
        1 - pval / 2, df
    )  # two-tailed, t distribution
    indices = np.logical_or(
        (secondlevel_t < -thresholding_level), (secondlevel_t > thresholding_level)
    )

    # thresholded map
    thresholded_tvals = np.array(secondlevel_t) * indices
    thresholded_tvals_expanded = np.expand_dims(thresholded_tvals, axis=(1, 2))
    s_map_thresholded = signals_to_img_labels(
        thresholded_tvals_expanded, path_Glasser, mnitemp["mask"]
    )

    # unthresholded map
    unthresholded_tvals = np.array(secondlevel_t)
    unthresholded_tvals_expanded = np.expand_dims(unthresholded_tvals, axis=(1, 2))
    s_map_unthresholded = signals_to_img_labels(
        unthresholded_tvals_expanded, path_Glasser, mnitemp["mask"]
    )


    np.savez_compressed(
        f"{HOMEDIR}/Generated_data/Graph_SDI_related/2nd_level_test_stats/unthresholded/unthresholded_{condition}_{band}",
        secondlevel_t=secondlevel_t,
    )
    np.savez_compressed(
        f"{HOMEDIR}/Generated_data/Graph_SDI_related/2nd_level_test_stats/thresholded/thresholded_{condition}_{band}",
        secondlevel_t_threholded=thresholded_tvals,
    )

    plotting.plot_img_on_surf(
        s_map_thresholded,
        title=f"II level; {band}; {condition}; tvalues; perm-corrected",
        threshold=0.1,
    )
    plt.show()

    s_map_thresholded.to_filename(
        f"{HOMEDIR}/Results/SDI/thresholded_SDI_spatial_map/{condition}/s_map_thresholded_{band}.nii.gz"
    )
    s_map_unthresholded.to_filename(
        f"{HOMEDIR}/Results/SDI/unthresholded_SDI_spatial_map/{condition}/s_map_unthresholded_{band}.nii.gz"
    )


conditions = ["baseline","differenced"] # conditions are baseline and differenced

for condition in conditions:
    empirical_SDI = np.load(
        f"{HOMEDIR}/Generated_data/Graph_SDI_related/empirical_SDI_{condition}.npz"
    )
    surrogate_SDI = np.load(
        f"{HOMEDIR}/Generated_data/Graph_SDI_related/surrogate_SDI_{condition}.npz"
    )

    stats("wideband", empirical_SDI, surrogate_SDI)
    stats("alpha", empirical_SDI, surrogate_SDI)
    stats("theta", empirical_SDI, surrogate_SDI)
    stats("low_beta", empirical_SDI, surrogate_SDI)
    stats("high_beta", empirical_SDI, surrogate_SDI)