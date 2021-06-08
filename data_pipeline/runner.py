import data_pipeline
import helpers.db_helper as db_helper

if __name__ == '__main__':
    stages = data_pipeline.Stages('hb', '2021-04-28')
    raw_df = stages.get_data()
    df_with_geo = stages.add_geo_data(raw_df)
    stages.load_to_database(df_with_geo)
    # Testing the database - checking the gender ratio and youngest/oldest player in each country
    db_helper.get_gender_ratio('hb')
    db_helper.get_youngest_player_by_country('hb')
    db_helper.get_oldest_player_by_country('hb')
