"""This module tests the covid news handling"""

import logging
import pytest
import logging_formatting
from covid_news_handling import news_API_request

#Create Logger for this module
logger = logging.getLogger(__name__)

def test_news_API_request():
    """This function will test the news_API_request function"""

    #Logging
    logging.debug("The test_news_API_request function has been called")

    all_articles = news_API_request(covid_terms = "Covid COVID-19 coronavirus")
    #Check that the articles dictionary isn't empty
    has_items = bool(all_articles)
    assert has_items
