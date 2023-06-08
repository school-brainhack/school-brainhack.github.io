"""
Study 2
This code will compute the dynamical connectivity from a time series dataset of EEG signals for each of the 25 subjects, for each frequency band that is present in the npz data files. 
This involves adjusting parameters like fmin and fmax dynamically based on cortical signals for specific frequency bands, as well as slicing data in 1s intervals and forcing the function to compute for specific frequencies within given ranges.
This is done by using the function spectral_connectivity_epochs from the MNE-Connectivity module. 
The computed connectivity is then stored back into the original dataset dictionary, under the key 'connectivity'.

The dataset we are working with is structured as 5 separate frequency bands (high_beta, wideband, theta, alpha, and low_beta) with each band data shaped as (25, 360, 21250), corresponding to 25 subjects (defined as epochs), 360 signals per epoch (ROIs), and 21250 time points per signal. 
The frequency sample rate, sfreq, is set at 125 Hz.
This data is loaded and all stored in the dictionary named "video_watching_dataset".

See https://mne.tools/mne-connectivity/stable/generated/mne_connectivity.spectral_connectivity_epochs.html
Here we use PLI. For further analysis and comparison of different connectivity information, see https://mne.tools/mne-connectivity/stable/auto_examples/dpli_wpli_pli.html#sphx-glr-auto-examples-dpli-wpli-pli-py
"""
import numpy as np
import mne_connectivity
from nilearn import datasets, plotting, maskers
from collections import defaultdict
from tqdm import tqdm
import multiprocessing
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

HOMEDIR = "/users/local/Venkatesh/Brainhack"
n_subjects = 25

atlas_yeo_2011 = datasets.fetch_atlas_yeo_2011()
yeo = atlas_yeo_2011.thick_7
glasser = "/users2/local/Venkatesh/Multimodal_ISC_Graph_study/src_data/Glasser_masker.nii.gz"  # f"{HOMEDIR}/src_data/Glasser_masker.nii.gz"

masker = maskers.NiftiMasker(standardize=False, detrend=False)
masker.fit(glasser)
glasser_vec = masker.transform(glasser)

yeo_vec = masker.transform(yeo)
yeo_vec = np.round(yeo_vec)

matches = []
match = []
best_overlap = []
for i, roi in enumerate(np.unique(glasser_vec)):
    overlap = []
    for roi2 in np.unique(yeo_vec):
        overlap.append(
            np.sum(yeo_vec[glasser_vec == roi] == roi2) / np.sum(glasser_vec == roi)
        )
    best_overlap.append(np.max(overlap))
    match.append(np.argmax(overlap))
    matches.append((i + 1, np.argmax(overlap)))

########################################################################################################################################
# STEP 0 : DEFINE THE PARAMETERS AND DATA VARIABLES
########################################################################################################################################
n_seconds = 170  # time recording
fs = 125  # sample freq
n_ROI = 360
method = "wpli"  # for computation of connectivity measures
n_times = (
    n_seconds * fs
)  # = 21250 : The number of time points per signal (170sec at 125Hz ==> 21250 time points)
window_size = 125  # 1s

########################################################################################################################################
# STEP 1 : LOAD THE DATA INTO VARIABLE : DEFINE A DATASET DICTIONARY
########################################################################################################################################
envelope_signal = np.load(f"{HOMEDIR}/src_data/envelope_signal_bandpassed.npz")
envelope_signal_alpha = envelope_signal["alpha"]


def segregation_computation(envelope, network):
    """This function computes the segregation measure for a given network, for a given frequency band."""
    window_size = 125  # 1s

    sce_whole_size = list()
    for window_start in range(0, n_seconds * fs, window_size):
        signal = envelope[:, :, window_start : window_start + window_size]

        ########################################################################################################################################
        # STEP 2 : Compute the spectral connectivity for each frequency band.
        ########################################################################################################################################
        sce = mne_connectivity.spectral_connectivity_epochs(
            signal,
            sfreq=125,
            fmin=8,
            fmax=13,
            method=method,
            faverage=True,
            verbose=False,
        )

        connectivity_matrix = sce.get_data().reshape(n_ROI, n_ROI)
        connectivity_matrix_symmetric = connectivity_matrix + connectivity_matrix.T

        sce_whole_size.append(connectivity_matrix_symmetric)

    segregation_list = list()

    ########################################################################################################################################
    # STEP 3 : Compute Segregation; for a given network, computes the average interaction of this network with all other networks for each time window.
    ########################################################################################################################################
    for window in range(len(sce_whole_size)):

        network_indices = [np.where(np.array(match) == network)[0]][0]

        binmask_within = np.zeros((n_ROI, n_ROI))
        binmask_between_step1 = np.zeros((n_ROI, n_ROI))

        for indices in network_indices:

            binmask_within[indices, network_indices] = 1
            binmask_within[network_indices, 1] = 1

            binmask_between_step1[indices, :] = 1
            binmask_between_step1[:, indices] = 1

            binmask_between = binmask_between_step1 - binmask_within

        matrix = sce_whole_size[window]
        # Segregation is defined as the difference between the average strength of connections within a network and the average strength of connections between a network and all other networks, divided by the average strength of connections within a network.
        average_strength_within = np.sum(matrix * binmask_within) / (
            np.sum(binmask_within) - len(network_indices)
        )
        average_strength_between = np.sum(matrix * binmask_between) / np.sum(
            binmask_between
        )

        segregation = (
            average_strength_within - average_strength_between
        ) / average_strength_within

        segregation_list.append(segregation)

    return segregation_list


########################################################################################################################################
### Surrogate data generation in parallel ###
########################################################################################################################################
NB_CPU = multiprocessing.cpu_count()


def parellelize(runs):

    np.random.seed(runs)
    return segregation_computation(
        envelope_signal_alpha[:, np.random.permutation(n_ROI), :], network=1
    )


surrogate_data = Parallel(n_jobs=NB_CPU - 1, max_nbytes=None)(
    delayed(parellelize)(main_parallelization)
    for main_parallelization in tqdm(range(100))
)
# surrogate_data = np.load('/users/local/Venkatesh/Brainhack/Generated_data/Connectivity_related/surrogate_alpha_visual.npz')['surrogate_data']

empirical_segregation = segregation_computation(envelope_signal_alpha, 1)


# All the empirical and the surrogate are computed and used for the following analysis.
# They are computed for over the entire video

# Test 1: Any link between segregation and ISC Correlation time-series ?
strong_ISC_timestamps = np.load(f"{HOMEDIR}/src_data/strong_ISC_timestamps.npz")[
    "timestamps"
]

plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure(plt.figure(figsize=(25, 10)))
ax1 = fig.add_subplot(211)

sig_pos = np.where(empirical_segregation > np.max(surrogate_data, axis=0))[0]
sig_neg = np.where(empirical_segregation < np.min(surrogate_data, axis=0))[0]
sig = list()
sig.append(sig_pos)
sig.append(sig_neg)
sig = np.array(sorted(np.hstack(sig)))

mask = np.zeros(170)
significance = np.unique(np.hstack(a))
mask[significance] = 1

ax1.plot(mask, label="Strong ISC", color="blue")
ax1.plot(significance, mask[significance], marker="o", ls="", color="red")


ax2 = ax1.twinx()
ax2.plot(np.array(empirical_segregation).T, color="green", label="Segregation")
ax2.plot(sig, np.array(empirical_segregation)[sig], marker="o", ls="", color="red")
ax2.axhline(0, c="orange")
ax1.legend()

ax1.set_xlabel("time (s)")
ax1.set_ylabel("binarized significance level")
ax2.set_ylabel("Segregation")

ax1.yaxis.label.set_color("blue")
ax2.yaxis.label.set_color("green")

fig.suptitle("Segregation versus Strong ISC")
fig.savefig(f"{HOMEDIR}/Results/Figures/segregation_alpha.svg")


# Test 2: Any link between Significant ISC and non-significant ISC in terms of segregation ?
isc_result = np.load(f"{HOMEDIR}/src_data/sourceCCA_ISC_8s_window.npz")["sourceISC"]
noise_floor_source = np.load(f"{HOMEDIR}/src_data/noise_floor_8s_window.npz")[
    "isc_noise_floored"
]  # Noise floor
sig_list = list()
for i in range(3):
    significance = np.where(
        np.max(np.array(noise_floor_source)[:, i, :], axis=0) < isc_result[i]
    )[0]
    sig_list.append(significance)


sig_list = np.unique(np.hstack(sig_list))
non_sig_list = list(set(range(170)) - set(sig_list))

# Grouping the segregation values during significant and non-significant ISC
segregation_during_sig_ISC = np.array(empirical_segregation)[sig_list]
segregation_during_non_sig_ISC = np.array(empirical_segregation)[non_sig_list]

# T-test to compare the segregation values during significant and non-significant ISC
ttest_ind(
    segregation_during_sig_ISC, segregation_during_non_sig_ISC, permutations=50000
)


# Visualizing the segregation values during significant and non-significant ISC
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(figsize=(8, 4))
boxplots_colors = ["yellowgreen", "olivedrab"]
data_x = [segregation_during_sig_ISC, segregation_during_non_sig_ISC]

bp = ax.boxplot(data_x, patch_artist=True, vert=False)
for patch, color in zip(bp["boxes"], boxplots_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.4)

violin_colors = ["thistle", "orchid"]
vp = ax.violinplot(
    data_x, showmeans=True, showextrema=False, showmedians=False, vert=False
)

for idx, b in enumerate(vp["bodies"]):
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    b.get_paths()[0].vertices[:, 1] = np.clip(
        b.get_paths()[0].vertices[:, 1], idx + 1, idx + 2
    )
    b.set_color(violin_colors[idx])

scatter_colors = ["tomato", "darksalmon"]
for idx, features in enumerate(data_x):
    # Add jitter effect so the features do not overlap on the y-axis
    y = np.full(len(features), idx + 0.8)
    idxs = np.arange(len(y))
    out = y.astype(float)
    out.flat[idxs] += np.random.uniform(low=-0.05, high=0.05, size=len(idxs))
    y = out
    plt.scatter(features, y, s=0.3, c=scatter_colors[idx])

plt.yticks(np.arange(1, 3, 1), ["Sig ISC", "Non-sig ISC"])  # Set text labels.
plt.title("Segregation during Significant and Non-significant ISC")
plt.savefig(f"{HOMEDIR}/Results/Figures/segregation.svg")
plt.show()
