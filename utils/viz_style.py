import matplotlib.pyplot as plt
import seaborn as sns

RESIDUAL_STYLE = {
    "scatter_color": "#4C72B0",
    "alpha": 0.6,
    "edgecolor": "black",
    "marker_size": 40,
    "zero_line_color": "#C44E52",
    "zero_line_style": "--",
    "zero_line_width": 1.5,
    "hist_color": "#4C72B0",
    "bins": 30,
}

def set_base_style():
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        font_scale=1.0
    )
    plt.rcParams.update({
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "figure.figsize": (7, 4),
    })