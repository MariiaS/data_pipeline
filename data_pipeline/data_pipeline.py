import sys

import pandas as pd

import helpers.db_helper as db_helper
import helpers.df_helper as df_helper
import helpers.load_helper as load_helper


class Stages:

    def __init__(self, game_name, date):
        self.game_name = game_name
        self.date = date
        print("The pipeline was initialised for game %s and date %s" % (game_name, date))

    def get_data(self) -> pd.DataFrame:
        print("Given the input game name and date, finding the data and returning dataframe")
        try:
            raw_df = load_helper.load_files_to_df(self.game_name, self.date)
            print(f"Retrieved [{raw_df.shape[0]}] records")
        except Exception as error:
            print(f"Source data could not be loaded. {error}")
            sys.exit(1)
        return raw_df

    def add_geo_data(self, raw_df) -> pd.DataFrame:
        print("Given the dataframe, add the information about location")
        try:
            df_with_geo = df_helper.add_geo_data(raw_df, self.game_name)
            print(f"Columns in the dataframe are: {list(df_with_geo.columns)}")
        except Exception as error:
            print(f"Could not add geolocation data. {error}")
            sys.exit(1)
        return df_with_geo

    def load_to_database(self, df_with_geo):
        print(
            "Given the dataframe, add the data to the database table, skipping the raws for the users with the same "
            "first name and family name")
        try:
            db_helper.add_data_to_table_from_df(df_with_geo, self.game_name)
            print(f"Columns in the database table are: {db_helper.get_table_columns(self.game_name)}")
        except Exception as error:
            print(f"Could not add geolocation data. {error}")
            sys.exit(1)
