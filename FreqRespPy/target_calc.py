
import pandas as pd

def mean_freq_response(target_df):
    target_df = target_df.apply(pd.to_numeric)
    row_means = target_df.mean(axis=1)

    return row_means

