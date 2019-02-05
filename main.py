
import pandas as pd

from FreqRespPy.data_search import get_target_file_list, open_target_file
from FreqRespPy.target_calc import mean_freq_response

if __name__ == '__main__':

    mean_response_output = []

    data_directory = 'data/'

    data_files = get_target_file_list(data_directory)
    print(data_files)

    for file in data_files:

        meta, df = open_target_file(data_directory, file)

        print(df)
        print(df.dtypes)

        mean_response = mean_freq_response(df)

        mean_response_output.append(mean_response)

    df_output = pd.concat(mean_response_output, axis=1)
    df_output.to_csv('output/test.csv')