"""Functions to help preprocessing data for the assignment""" 


import numpy as np
import pandas as pd


def remove_xa0_and_convert_to_int64(dew_point: str) -> np.int64:
    dp = dew_point.removesuffix('\xa0')
    return pd.to_numeric(dp)
