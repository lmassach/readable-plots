#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from readable_plots import *

if __name__ == "__main__":
    with PdfPages('test_results.pdf') as pdf:
        for font_sz in [10, 15, 22]:
            # Use the style setup utility
            set_style(font_size=font_sz)

            # 1D
            gauss_sample = np.random.normal(size=10000)
            x = np.linspace(-3, 3, 100)
            y = np.exp(-x**2 / 2)
            fig, ax1 = plt.subplots()
            c1 = 'tab:blue'
            ax1.set_title("1D Histogram")
            ax1.hist(gauss_sample, 100, (-3, 3), color=c1)
            ax1.set_xlabel("Value")
            ax1.set_ylabel("Counts / bin", color=c1)
            ax1.tick_params(axis='y', labelcolor=c1)
            pdf.savefig()
            ax2 = ax1.twinx()
            c2 = 'tab:red'
            ax1.set_title("1D Histogram and Function")
            ax2.plot(x, y, '-', color=c2)
            ax2.set_ylabel("Probability Density Function", color=c2)
            ax2.tick_params(axis='y', labelcolor=c2)
            set_symmetric_horizontal_margins()
            pdf.savefig()

            # 2D
            gauss_sample_x = np.random.normal(size=100000)
            gauss_sample_y = np.random.normal(size=100000)
            fig, ax = plt.subplots()
            h = ax.hist2d(
                gauss_sample_x, gauss_sample_y, (20, 20), ((-3, 3), (-3, 3)))
            ax.set_title("2D Histogram")
            ax.set_xlabel("X Value")
            ax.set_ylabel("Y Value")
            pdf.savefig()
            ax.set_title("2D Histogram (with legend)")
            cb = plt.colorbar(h[3], ax=ax)
            cb.set_label("Counts / bin")
            pdf.savefig()

            # TODO Subplots
            # TODO Also test sharex when only one subplot has symmetric margins
