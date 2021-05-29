import numpy as np
import pandas as pd

from data_processor.geo_helper import get_address_from_ip, get_country_from_city_state


def add_address_data_to_df(dataframe) -> pd.DataFrame:
    geo_dataframe = pd.DataFrame()
    for i, row in dataframe.iterrows():
        geo_json = get_address_from_ip(dataframe.ip_address[i])
        ser = pd.read_json(geo_json, typ='series')
        geo_row = ser.to_frame().transpose()
        geo_row = geo_row.drop(['IPv4'], axis=1)  # drop duplicated column with ip address
        geo_dataframe = geo_dataframe.append(geo_row, ignore_index=True)
    geo_dataframe.replace('Not found', np.NaN)
    result = dataframe.join(geo_dataframe)
    return result


def add_country_column_to_df(dataframe) -> pd.DataFrame:
    geo_dataframe = pd.DataFrame(columns=['country_name'])
    for i, row in dataframe.iterrows():
        location_row = dataframe.location.iloc[i]
        country = get_country_from_city_state(location_row['city'], location_row['street'], location_row['postcode'])
        country_row = {'country_name': country}
        geo_dataframe = geo_dataframe.append(country_row, ignore_index=True)
    result = dataframe.join(geo_dataframe)
    return result
