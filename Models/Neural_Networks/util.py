import numpy as np

def r_squared(y_true, y_pred):
    ss_res = np.sum(np.square(y_true - y_pred))
    ss_tot = np.sum(np.square(y_true - np.mean(y_true)))

    return 1 - (ss_res / ss_tot)
