"""
Mike Eller
June 2018

Power Spectral Density
"""

from scipy.signal import welch
import afm
import numpy as np
import matplotlib.pyplot as plt


class PSD(object):
    def __init__(self, filename):
        self.scan = afm.Scan(filename=filename)

    def compute_psd(self, keyword, freq=1):
        if keyword == "height":
            signal = self.scan.ht
        elif keyword == "amplitude":
            signal = self.scan.amp
        elif keyword == "phase":
            signal = self.scan.ph
        elif keyword == "z":
            signal = self.scan.z
        else:
            raise ValueError
        return welch(signal[256], fs=freq, nperseg=512)


if __name__ == "__main__":
    test = PSD("C:\Users\MIchael\Dropbox (Arthur-UVA)\ArtGroup\Individual Member\Tannaz\Tannaz- AFM\\180430\\1400-S-A\X1400_S_A0002.ibw")
    f, Pxx_den = test.compute_psd("height")
    plt.figure()
    plt.semilogy(f, Pxx_den)
    test.scan.height_retrace()
