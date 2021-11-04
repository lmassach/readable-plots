#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from readable_plots import *

if __name__ == "__main__":
    with PdfPages('test_results.pdf') as pdf:
        for font_sz in [10, 15, 22]:
            print(f"Testing font_size={font_sz}")
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

            for spc in [1, 0]:
                # Subplots (wide)
                # 2 subplots
                x = np.linspace(0, 10, 100)
                y1 = 0.5 + 0.5 * np.sin(x)
                y2 = y1 + np.random.normal(0, 0.25, x.shape)
                set_style(font_size=font_sz, n_rows=2*spc)
                fig = plt.figure()
                ax1 = plt.subplot(211)
                ax1.plot(x, y1, '-')
                ax1.set_title("2 Subplots" if spc else "2 Subplots (no space)")
                if spc:
                    ax1.set_xlabel("X Value")
                else:
                    hide_ticks(ax1, "x")
                ax1.set_ylabel("Y Value")
                plt.grid()
                ax2 = plt.subplot(212, sharex=ax1)
                ax2.plot(x, y2, '-')
                ax2.set_xlabel("X Value")
                ax2.set_ylabel("Y Value #2")
                plt.grid()
                pdf.savefig()
                # 3 Subplots
                y3 = y1 + np.random.normal(0, 0.05, x.shape)
                set_style(font_size=font_sz, n_rows=3*spc)
                fig = plt.figure()
                ax1 = plt.subplot(311)
                ax1.plot(x, y1, '-')
                ax1.set_title("3 Subplots" if spc else "3 Subplots (no space)")
                if spc:
                    ax1.set_xlabel("X Value")
                else:
                    hide_ticks(ax1, "x")
                ax1.set_ylabel("Y Value")
                plt.grid()
                ax2 = plt.subplot(312, sharex=ax1)
                ax2.plot(x, y2, '-')
                if spc:
                    ax2.set_xlabel("X Value")
                else:
                    hide_ticks(ax2, "x")
                ax2.set_ylabel("Y Value #2")
                plt.grid()
                ax3 = plt.subplot(313, sharex=ax2)
                ax3.plot(x, y3, '-')
                ax3.set_xlabel("X Value")
                ax3.set_ylabel("Y Value #3")
                plt.grid()
                pdf.savefig()
                # Subplots (tall)
                # 2 subplots
                set_style(font_size=font_sz, n_cols=2*spc)
                fig = plt.figure()
                ax1 = plt.subplot(121)
                ax1.barh(x, y1, height=0.08)
                plt.suptitle("2 Subplots" if spc else "2 Subplots (no space)")
                ax1.set_ylabel("X Value")
                ax1.set_xlabel("Y Value")
                plt.grid(axis='x')
                ax2 = plt.subplot(122, sharey=ax1)
                ax2.barh(x, y2, height=0.08)
                if font_sz < 20 and spc:  # Some common sense is still needed
                    ax2.set_ylabel("X Value")
                if not spc:
                    hide_ticks(ax2, 'y')
                ax2.set_xlabel("Y Value #2")
                plt.grid(axis='x')
                pdf.savefig()
                # 3 Subplots
                set_style(font_size=font_sz, n_cols=3*spc)
                fig = plt.figure()
                ax1 = plt.subplot(131)
                ax1.barh(x, y1, height=0.08)
                plt.suptitle("3 Subplots" if spc else "3 Subplots (no space)")
                ax1.set_ylabel("X Value")
                ax1.set_xlabel("Y Value")
                plt.grid(axis='x')
                ax2 = plt.subplot(132, sharey=ax1)
                ax2.barh(x, y2, height=0.08)
                if font_sz < 20 and spc:  # Some common sense is still needed
                    ax2.set_ylabel("X Value")
                if not spc:
                    hide_ticks(ax2, 'y')
                ax2.set_xlabel("Y Value #2")
                plt.grid(axis='x')
                ax3 = plt.subplot(133, sharey=ax2)
                ax3.barh(x, y3, height=0.08)
                if font_sz < 20 and spc:  # Some common sense is still needed
                    ax3.set_ylabel("X Value")
                if not spc:
                    hide_ticks(ax3, 'y')
                ax3.set_xlabel("Y Value #3")
                plt.grid(axis='x')
                pdf.savefig()
