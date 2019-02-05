
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


def open_target_file(ft_region_file):
    df = pd.read_csv(ft_region_file)

    meta = df


if __name__ == '__main__':
    data_files = get_target_files('../data/')
    print(data_files)