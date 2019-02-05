
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
    file_list = [join(data_directory, file) for file in file_list]

    return file_list


def open_target_file(ft_region_file, meta_rows=6, transpose_meta=False):
    df = pd.read_csv(ft_region_file)
    df = df.drop(['Variable_index', 'Variable_name'], axis=1)

    meta = df.head(meta_rows)
    if transpose_meta:
        meta = meta.transpose()

    df.drop(df.head(meta_rows).index, inplace=True)

    return [meta, df]


if __name__ == '__main__':
    data_files = get_target_file_list('../data/')
    print(data_files)
    file = data_files[0]
    meta, df = open_target_file(file)

    print(meta)
    print(df)