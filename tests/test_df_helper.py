from unittest import TestCase

import pandas as pd

from data_pipeline.helpers.df_helper import get_country_from_city_state, get_address_from_ip


class Test(TestCase):
    def test_get_country_from_city_state(self):
        result = get_country_from_city_state("Kolmas linja", "Helsinki", "")
        self.assertEqual(result, "Suomi / Finland")

    def test_get_country_from_city_state_by_index(self):
        result = get_country_from_city_state("", "", "00560")
        self.assertEqual(result, "Suomi / Finland")

    def test_get_address_from_ip(self):
        geo_json = get_address_from_ip("87.92.158.88")
        geo_df = pd.read_json(geo_json, typ='series')
        self.assertEqual(geo_df.country_name, "Finland")
