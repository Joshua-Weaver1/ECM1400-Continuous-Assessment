"""This module tests the covid data handler"""

import pytest
from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request

#Integration of the provided tests
def test_parse_csv_data():
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639


def test_process_covid_csv_data():
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(parse_csv_data('nation_2021-10-28.csv'))
    assert last7days_cases == 240_299

#Further test functions
def test_covid_API_request():
    data = covid_API_request()
    #Test to show that returned values are the same for default arguments
    assert covid_API_request("Exeter", "ltla") == covid_API_request()
    #Test to see if returned dictionary is not empty
    has_items = bool(data)
    assert has_items
