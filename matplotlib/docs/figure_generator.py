#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from readable_plots import *  # readable_plots.py must be in the working dir

FONT_SIZE = 15  # 10 is matplotlib's default, 22 is very large

if __name__ == "__main__":
    x_data = np.linspace(0, 10, 100)
    y_data = np.sin(x_data)
    x1 = x_data
    y1 = y_data
    x2 = x_data
    y2 = np.cos(x_data)

    # Basic usage example
    set_style(FONT_SIZE)  # Must be called before creating the figure
    plt.figure()
    plt.plot(x_data, y_data)
    plt.title("Title")
    plt.xlabel("Label")
    plt.ylabel("Label")
    plt.savefig("basic_usage.png")

    # Subplots example
    set_style(FONT_SIZE, n_rows=2)  # Recomputes margins and paddings
    plt.figure()
    plt.subplot(211)
    plt.plot(x1, y1)
    plt.title("Title")
    plt.xlabel("Label")
    plt.ylabel("Label")
    plt.subplot(212)
    plt.plot(x2, y2)
    plt.xlabel("Label")
    plt.ylabel("Label")
    plt.savefig("subplots.png")

    # Subplots without space example
    set_style(FONT_SIZE, n_rows=0)  # No padding
    plt.figure()
    plt.subplot(211)
    plt.plot(x1, y1)
    plt.title("Title")
    hide_ticks(plt.gca(), 'x')  # Do not display ticks on top plot
    plt.ylabel("Label")
    plt.subplot(212)
    plt.plot(x2, y2)
    plt.xlabel("Label")
    plt.ylabel("Label")
    plt.savefig("subplots_no_space.png")

    # Two y scales example
    set_style(FONT_SIZE)
    plt.figure()
    fig, ax1 = plt.subplots()
    c1 = 'tab:blue'
    ax1.set_title("Title")
    ax1.plot(x1, y1, color=c1)
    ax1.set_xlabel("Label")
    ax1.set_ylabel("Label", color=c1)
    ax1.tick_params(axis='y', labelcolor=c1)
    ax2 = ax1.twinx()
    c2 = 'tab:red'
    ax2.plot(x2, y2, color=c2)
    ax2.set_ylabel("Label", color=c2)
    ax2.tick_params(axis='y', labelcolor=c2)
    set_symmetric_horizontal_margins()  # Make room for the rightmost y axis label
    plt.savefig("two_y_axes.png")
