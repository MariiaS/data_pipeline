import pandas as pd

SAMPLE_NUMBER = 10


def load_files_to_df(game_name, date):
    path = get_path_from_date(game_name, date)
    if game_name == 'hb':
        path = path + ".csv"
        loaded_df = load_csv_to_df(path, SAMPLE_NUMBER)
    else:
        path = path + ".json"
        loaded_df = load_json_to_df(path, SAMPLE_NUMBER)
    return loaded_df


def load_csv_to_df(path, rows=None):
    dataframe = pd.read_csv(path, nrows=rows, index_col=False)
    return dataframe


def load_json_to_df(path, rows=None):
    dataframe = pd.read_json(path, lines=True, nrows=rows)
    return dataframe


def get_path_from_date(game_name, date) -> str:
    date_split = date.split('-')
    path = "data_pipeline/user_data/" + game_name + "/" + date_split[0] + "/" + date_split[1] + "/" + date_split[
        2] + "/" + game_name
    return path
