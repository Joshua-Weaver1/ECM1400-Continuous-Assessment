"""This module tests the covid news handling"""

import pytest
from covid_news_handling import news_API_request


def test_news_API_request():
    all_articles = news_API_request(covid_terms = "Covid COVID-19 coronavirus")
    #Check that the articles dictionary isn't empty
    has_items = bool(all_articles)
    assert has_items
