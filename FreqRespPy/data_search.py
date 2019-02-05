
from os import listdir
from os.path import join

import pandas as pd

def get_target_file_list(data_directory):
    """
    A function to return a list of all .csv documents in a directory.
    :param data_directory: directory (relative or absolute) that points to .csv files of interest.
    :return: a list of the absolute file paths for each
    """
    file_list = listdir(data_directory)

    file_list = [file for file in file_list if file.endswith('.csv')]
    file_list = [file for file in file_list if file.startswith('FT_region')]

    return file_list


def open_target_file(data_directory, ft_region_file, meta_rows=6, transpose_meta=False):
    """

    :param data_directory:
    :param ft_region_file:
    :param meta_rows:
    :param transpose_meta:
    :return:
    """
    # Read .csv, drop Variable columns
    df = pd.read_csv(join(data_directory, ft_region_file))
    df.index = df['Target_index']

    df = df.drop(['Variable_index', 'Variable_name', 'Target_index'], axis=1)

    # Extract first n rows as meta data.  Optionally transpose.
    file_meta = df.head(meta_rows)
    if transpose_meta:
        file_meta = file_meta.transpose()

    # Drop the first n rows of meta data and return df of freq resp
    df.drop(df.head(meta_rows).index, inplace=True)

    return [file_meta, df]
