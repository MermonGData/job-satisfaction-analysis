import warnings
import numpy as np
from IPython.display import HTML, display

def setup_notebook(seed: int = 42):
    warnings.filterwarnings("ignore")
    np.random.seed(seed)
    display(HTML("<style>.output_scroll { height: auto !important; }</style>"))
