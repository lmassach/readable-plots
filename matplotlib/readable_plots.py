import matplotlib as mpl
import matplotlib.pyplot as plt


__all__ = ["set_style", "set_symmetric_horizontal_margins"]


def set_style(font_size=22, tight_layout=False):
    """Sets matplotlib to have larger text and suitable margins."""
    # Scales all texts, default size is 10
    mpl.rc('font', size=font_size)
    if tight_layout:
        # Uses tight_layout automatically on all p lots
        mpl.rc('figure', autolayout=True)
    else:
        mpl.rc("figure", figsize=(6.4, 4.8), dpi=100, autolayout=False)
        params = {
            "left": 0.06 + 0.06 * font_size / 10,
            "right": 1 - (-0.05 + 0.1 * font_size / 10),
            "bottom": 0.06 + 0.05 * font_size / 10,
            "top": 1 - (0.02 + 0.04 * font_size / 10)
            # TODO Set wspace and hspace
        }
        mpl.rc("figure.subplot", **params)


def set_symmetric_horizontal_margins():
    """
    Sets the right margin the same as the left one. Useful when using
    more than one y-axis scale.
    """
    plt.subplots_adjust(right=1-mpl.rcParams["figure.subplot.left"])
