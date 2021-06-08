import data_pipeline

if __name__ == '__main__':
    stages = data_pipeline.Stages('hb', '2021-04-28')
    raw_df = stages.get_data()
    df_with_geo = stages.add_geo_data(raw_df)
    stages.load_to_database(df_with_geo)
