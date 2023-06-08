"""Study 1. This script computes the SDI for each band, and saves the empirical and surrogate SDI."""
import numpy as np
import importlib
import os
import matplotlib.pyplot as plt
from scipy import io as sio
import scipy.linalg as la
from collections import defaultdict
from tqdm import tqdm

HOMEDIR = "/users/local/Venkatesh/Brainhack"


def graph():
    """Computing Graph Laplacian for the consensus structural graph

    Returns:
        Matrix of floats: A weight matrix for the thresholded graph
    """

    connectivity = sio.loadmat(f"{HOMEDIR}/src_data/SC_avg56.mat")["SC_avg56"]
    degree = np.diag(np.power(np.sum(connectivity, axis=1), -0.5))
    laplacian = np.eye(connectivity.shape[0]) - np.matmul(
        degree, np.matmul(connectivity, degree)
    )

    return laplacian


laplacian = graph()  # laplacian is a matrix of shape (n_ROI, n_ROI)
[eigvals, eigevecs] = la.eigh(
    laplacian
)  # eigenvalues and eigenvectors of the laplacian


def gft(signal):
    """Graph Fourier Transform"""
    assert np.shape(signal) == (subjects, regions, video_duration)
    array_of_gft = list()

    for sub in range(subjects):
        signal_for_gft = signal[sub]
        transform = np.matmul(eigevecs.T, signal_for_gft)
        array_of_gft.append(transform)

    assert np.shape(array_of_gft) == (subjects, regions, video_duration)

    return array_of_gft


def signal_filtering(g_psd, low_freqs, high_freqs):
    """Filtering the signal with low and high frequencies"""
    assert np.shape(g_psd) == (subjects, regions, video_duration)

    lf_signal = list()
    hf_signal = list()

    for subs in range(subjects):
        g_psd_for_igft = g_psd[subs]
        assert np.shape(g_psd_for_igft) == (regions, video_duration)

        low_freq_signal = np.matmul(low_freqs, g_psd_for_igft)
        high_freqs_signal = np.matmul(high_freqs, g_psd_for_igft)

        lf_signal.append(low_freq_signal)
        hf_signal.append(high_freqs_signal)

    assert np.shape(lf_signal) == (subjects, regions, video_duration)
    assert np.shape(hf_signal) == (subjects, regions, video_duration)

    return lf_signal, hf_signal


def frobenius_norm(lf_signal, hf_signal, label):
    """Frobenius norm of the signal"""
    assert np.shape(lf_signal) == (subjects, regions, video_duration)
    assert np.shape(hf_signal) == (subjects, regions, video_duration)

    if label == "baseline":
        signal_lf = np.array(lf_signal)[:, :, :baseline_in_samples]
        signal_hf = np.array(hf_signal)[:, :, :baseline_in_samples]

    if label == "post_onset":
        signal_lf = np.array(lf_signal)[:, :, baseline_in_samples:]
        signal_hf = np.array(hf_signal)[:, :, baseline_in_samples:]

    normed_lf = np.linalg.norm(signal_lf, axis=-1)
    normed_hf = np.linalg.norm(signal_hf, axis=-1)

    assert np.shape(normed_lf) == (subjects, regions)
    assert np.shape(normed_hf) == (subjects, regions)

    return normed_lf, normed_hf


def SDIndex(signal_in_dict):
    """Structural-Decoupling Index- quantifying the degree of decoupling between structure and function"""
    lf_signal, hf_signal = signal_in_dict["lf"], signal_in_dict["hf"]
    index = hf_signal / lf_signal

    return index


def surrogacy(eigvector, signal):
    """Graph-informed Surrogacy control
    Args:
        eigvector (matrix): Eigenvector
        random_signs (matrix): Random sign change to flip the phase
        signal (array): Cortical brain/graph signal
    Returns:
        reconstructed_signal: IGFTed signal; recontructed, but with phase-flipped signal
    """
    surrogate_signal = list()
    for n in range(n_surrogate):

        np.random.seed(n)
        random_signs = np.round(
            np.random.rand(
                regions,
            )
        )
        random_signs[random_signs == 0] = -1
        random_signs = np.diag(random_signs)

        g_psd = np.matmul(eigevecs.T, signal)
        eigvector_manip = np.matmul(eigvector, random_signs)
        reconstructed_signal = np.matmul(eigvector_manip, g_psd)

        surrogate_signal.append(reconstructed_signal)

    assert np.shape(surrogate_signal) == (
        n_surrogate,
        subjects,
        regions,
        video_duration,
    )

    return surrogate_signal


def signal_to_SDI(lf_signal, hf_signal):
    """Computing the SDI"""
    normed_baseline_signal = defaultdict(dict)  # Frob. norm of the baseline signal
    normed_post_onset_signal = defaultdict(dict)  # Frob. norm of the post-onset signal

    normed_baseline_signal["lf"], normed_baseline_signal["hf"] = frobenius_norm(
        lf_signal=lf_signal, hf_signal=hf_signal, label="baseline"
    )
    normed_post_onset_signal["lf"], normed_post_onset_signal["hf"] = frobenius_norm(
        lf_signal=lf_signal, hf_signal=hf_signal, label="post_onset"
    )

    SDIndex_baseline = SDIndex(normed_baseline_signal)
    SDIndex_post_onset = SDIndex(normed_post_onset_signal)

    assert np.shape(SDIndex_baseline) == (subjects, regions)
    assert np.shape(SDIndex_post_onset) == (subjects, regions)

    empirical_SDIndex_bc = SDIndex_post_onset - SDIndex_baseline

    return empirical_SDIndex_bc


video_duration = 88
subjects = 25
regions = 360
number_of_events = 24
baseline_in_samples = 25
post_onset_in_samples = 63
n_surrogate = 50

# Load the wideband and other bands data
wideband_and_other_bands_zscored = np.load(
    f"{HOMEDIR}/Generated_data/Cortical_surface_related/wideband_and_other_bands_zscored.npz"
)


def band_wise_SDI(band):
    """Computing the SDI for each band"""
    empirical_SDI_differenced_condition = list()
    surrogate_SDI_differenced_condition = list()

    for event in range(number_of_events):
        signal = wideband_and_other_bands_zscored[f"{band}"][:, event]
        # Compute the GFT of the signal
        psd = gft(signal)

        psd_abs_squared = np.power(np.abs(psd), 2)
        assert np.shape(psd_abs_squared) == (subjects, regions, video_duration)

        psd_abs_squared_averaged = np.mean(psd_abs_squared, axis=(0, 2))
        assert np.shape(psd_abs_squared_averaged) == (regions,)

        # Compute the median power for identifying the critical frequency (cut-off frequency)
        median_power = np.trapz(psd_abs_squared_averaged) / 2
        sum_of_freqs = 0
        i = 0
        while sum_of_freqs < median_power:
            sum_of_freqs = np.trapz(psd_abs_squared_averaged[:i])
            i += 1
        critical_freq = i - 1

        # With the critical frequency, compute the low and high frequencies
        low_freqs = np.zeros((regions, regions))
        low_freqs[:, :critical_freq] = eigevecs[:, :critical_freq]

        high_freqs = np.zeros((regions, regions))
        high_freqs[:, critical_freq:] = eigevecs[:, critical_freq:]

        # Fetch the low and high frequency components of the signal
        lf_signal, hf_signal = signal_filtering(psd, low_freqs, high_freqs)

        # Compute the SDI from the low and high frequency components
        empirical_SDIndex_bc = signal_to_SDI(lf_signal, hf_signal)

        empirical_SDI_differenced_condition.append(empirical_SDIndex_bc)

        #########################################################################
        ############ Surrogate computation#######################################
        #########################################################################
        surrogate_signal = surrogacy(eigevecs, signal)
        surrogate_psd = [gft(surrogate_signal[n]) for n in range(n_surrogate)]

        assert np.shape(surrogate_psd) == (
            n_surrogate,
            subjects,
            regions,
            video_duration,
        )

        surrogate_lf_signal, surrogate_hf_signal = zip(
            *[
                signal_filtering(surrogate_psd[n], low_freqs, high_freqs)
                for n in range(n_surrogate)
            ]
        )
        assert np.shape(surrogate_lf_signal) == (
            n_surrogate,
            subjects,
            regions,
            video_duration,
        )

        surrogate_SDIndex_bc = [
            signal_to_SDI(
                surrogate_lf_signal[n],
                surrogate_hf_signal[n],
            )
            for n in range(n_surrogate)
        ]

        assert np.shape(surrogate_SDIndex_bc) == (n_surrogate, subjects, regions)
        surrogate_SDI_differenced_condition.append(surrogate_SDIndex_bc)

    return empirical_SDI_differenced_condition, surrogate_SDI_differenced_condition


SDI_empirical = defaultdict(dict)  # Empirical SDI
SDI_surrogate = defaultdict(dict)  # Surrogate SDI

for labels, signal in tqdm(wideband_and_other_bands_zscored.items()):
    SDI_empirical[f"{labels}"], SDI_surrogate[f"{labels}"] = band_wise_SDI(f"{labels}")

# Save the empirical and surrogate SDI
np.savez_compressed(
    f"{HOMEDIR}/Generated_data/Graph_SDI_related/empirical_SDI_differenced",
    **SDI_empirical,
)
np.savez_compressed(
    f"{HOMEDIR}/Generated_data/Graph_SDI_related/surrogate_SDI_differenced.npz",
    **SDI_surrogate,
)
