from unittest import TestCase
import pytest

from data_pipeline.helpers.load_helper import get_path_from_date, load_files_to_df, load_csv_to_df, load_json_to_df


class Test(TestCase):
    def test_get_path_from_date(self):
        result = get_path_from_date("hb", "2018-12-01")
        self.assertEqual(result, "data_pipeline/user_data/hb/2018/12/01/hb")

    def test_get_path_from_date_incorrect_game(self):
        result = get_path_from_date("fake_game", "2018-12-01")
        self.assertEqual(result, " ")

    def test_get_path_from_date_incorrect_date_raises_exception(self):
        with pytest.raises(ValueError):
            get_path_from_date("hb", "0000-1111-01")

    def test_load_csv_to_df(self):
        result = load_csv_to_df('../data_pipeline/user_data/hb/2021/04/28/hb.csv')
        self.assertEqual(result.shape, (1000, 7))

    def test_load_json_to_df(self):
        result = load_json_to_df('../data_pipeline/user_data/wwc/2021/04/28/wwc.json')
        self.assertEqual(result.shape, (1000, 12))
