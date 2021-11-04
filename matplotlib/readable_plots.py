import warnings
import matplotlib as mpl
import matplotlib.pyplot as plt


__all__ = ["set_style", "set_symmetric_horizontal_margins", "hide_ticks"]


def _crop(value, max_value, name):
    if value > max_value:
        warnings.warn(
            f"Cropping very large {name} of {value:.2f} to {max_value:.2f}")
        return max_value
    return value


def set_style(font_size=22, n_rows=1, n_cols=1, auto_layout=False):
    """
    Sets matplotlib to have larger text and suitable margins.

    :param font_size: 10 (mpl default) is small, 25 is too large
    :param n_rows: Number of subplot rows for spacing adjustment.
        Use 0 for no vertical spacing.
    :param n_cols: Number of subplot columns for spacing adjustment.
        Use 0 for no horizontal spacing.
    :param auto_layout: Turns on automatic margin adjustment. If `True`,
        other parameters aside from `font_size` will be ignored.
    """
    # Scales all texts, default size is 10
    mpl.rc('font', size=font_size)
    if auto_layout:
        # Uses tight_layout automatically on all p lots
        mpl.rc('figure', autolayout=True)
    else:
        mpl.rc("figure", figsize=(6.4, 4.8), dpi=100, autolayout=False)
        # Empirically-tested margins
        left = 0.06 + 0.07 * font_size / 10
        left = _crop(left, 0.3, "left margin")
        right = -0.05 + 0.1 * font_size / 10
        right = _crop(right, 0.3, "right margin")
        bottom = 0.06 + 0.05 * font_size / 10
        bottom = _crop(bottom, 0.3, "bottom margin")
        top = 0.02 + 0.04 * font_size / 10
        top = _crop(top, 0.3, "top margin")
        # Empirically-tested subplot spacings
        hs = n_rows * (0.15 * font_size / 10)
        hs = _crop(hs, 1, "vertical spacing")
        ws = n_cols * (0.15 * font_size / 10)
        ws = _crop(ws, 1, "horizontal spacing")
        mpl.rc("figure.subplot", left=left, right=1-right, bottom=bottom,
               top=1-top, hspace=hs, wspace=ws)


def set_symmetric_horizontal_margins():
    """
    Sets the right margin the same as the left one for the current
    figure. Useful when using more than one y-axis scale.
    """
    plt.subplots_adjust(right=1-mpl.rcParams["figure.subplot.left"])


def hide_ticks(ax, which='both'):
    """
    Hides the scale ticks (x, y or both) for the given axis. Useful with
    shared axis in subplots without spacing.
    """
    if which in ('x', 'both'):
        plt.setp(ax.get_xticklabels(), visible=False)
    if which in ('y', 'both'):
        plt.setp(ax.get_yticklabels(), visible=False)
