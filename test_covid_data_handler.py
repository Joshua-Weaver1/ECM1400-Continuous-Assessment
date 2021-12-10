"""This module tests the covid data handler"""

import logging
import pytest
import logging_formatting
from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request

#Create Logger for this module
logger = logging.getLogger(__name__)

#Integration of the provided tests
def test_parse_csv_data():
    """This function will test the parse_csv_data function"""

    #Logging
    logging.debug("The test_parse_csv_data function has been called")

    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639


def test_process_covid_csv_data():
    """This function will test the process_covid_csv_data function"""

    #Logging
    logging.debug("The test_process_covid_csv_data function has been called")

    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(parse_csv_data('nation_2021-10-28.csv'))
    assert last7days_cases, current_hospital_cases; total_deaths == 240_299, 7_019, 141_544

#Further test functions
def test_covid_API_request():
    """This function will test the covid_API_request function"""

    #Logging
    logging.debug("The test_process_covid_csv_data function has been called")

    data = covid_API_request()
    #Test to show that returned values are the same for default arguments
    assert covid_API_request("Exeter", "ltla") == covid_API_request()
    #Test to see if returned dictionary is not empty
    has_items = bool(data)
    assert has_items
