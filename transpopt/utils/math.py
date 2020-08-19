"""Mathematical utilities.
"""

from scipy.ndimage.filters import gaussian_filter

import transpopt.utils.constants as c


def convert_signal_pdf(signal, sigma=0.0):
    """Smooths a signal into a probability density function.

    Args:
        signal (np.array): Array of signal.
        sigma (float): Standard deviation for the gaussian kernel.

    Returns:
        A smoothed signal (p.d.f.).

    """

    # Passes a gaussian filter through the input signal
    pdf = gaussian_filter(signal, sigma)

    # Normalizes the signal and adds an epsilon
    pdf = pdf / pdf.sum() + c.EPSILON

    # Re-normalizes the signal
    pdf /= pdf.sum()

    return pdf
