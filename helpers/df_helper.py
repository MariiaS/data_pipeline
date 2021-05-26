import pandas as pd

from helpers.geo_helper import get_address_from_ip, get_country_from_city_state

df = pd.read_csv("../data/hb/2021/04/28/hb.csv")
df_short = df[0:2]

df2 = pd.read_json("../data/wwc/2021/04/28/wwc.json", lines=True)
df_short2 = df2[0:2]


def add_address_data_hb(dataframe):
    geo_dataframe = pd.DataFrame()
    for i, row in dataframe.iterrows():
        geo_json = get_address_from_ip(dataframe.ip_address[i])
        ser = pd.read_json(geo_json, typ='series')
        geo_row = ser.to_frame().transpose()
        geo_row = geo_row.drop(['IPv4'], axis=1)
        geo_dataframe = geo_dataframe.append(geo_row, ignore_index=True)
    result = dataframe.join(geo_dataframe)
    return result


def add_country_wwc(dataframe):
    geo_dataframe = pd.DataFrame(columns=['country_name'])
    for i, row in dataframe.iterrows():
        location_row = dataframe.location.iloc[i]
        print(location_row)
        print(location_row['city'])
        print(location_row['state'])
        country = get_country_from_city_state(location_row['city'], location_row['street'])
        country_row = {'country_name': country}
        geo_dataframe = geo_dataframe.append(country_row, ignore_index=True)
    result = dataframe.join(geo_dataframe)
    return result


if __name__ == '__main__':
    print(add_country_wwc(df_short2).head())
