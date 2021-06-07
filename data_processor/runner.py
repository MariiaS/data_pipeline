import pandas as pd

import df_helper

SAMPLE_NUMBER = 10


def load_files_to_df_with_country(game_name, date):
    date_split = date.split('-')
    path = "data_processor/user_data/" + game_name + "/" + date_split[0] + "/" + date_split[1] + "/" + date_split[2] + "/" + game_name
    if game_name == 'hb':
        path = path + ".csv"
        loaded_df = load_csv_to_df(path, SAMPLE_NUMBER)
        dataframe = df_helper.add_address_data_to_df(loaded_df)
    else:
        path = path + ".json"
        loaded_df = load_json_to_df(path, SAMPLE_NUMBER)
        dataframe = df_helper.add_country_column_to_df(loaded_df)
    return dataframe


def load_csv_to_df(path, rows=None):
    dataframe = pd.read_csv(path, nrows=rows)
    return dataframe


def load_json_to_df(path, rows=None):
    dataframe = pd.read_json(path, lines=True, nrows=rows)
    return dataframe


if __name__ == '__main__':
    print(load_files_to_df_with_country('hb', '2021-04-28').head())
